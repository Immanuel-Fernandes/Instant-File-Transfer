# app.py

import streamlit as st
import uuid
import json
import os
import time
from io import BytesIO

# Constants
DB_FILE = "file_db.json"
FILE_DIR = "files"
EXPIRY_SECONDS = 3600  # 1 hour

# Ensure file directory exists
os.makedirs(FILE_DIR, exist_ok=True)

# --- Helper Functions ---

def load_db():
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            return json.load(f)
    return {}

def save_db(db):
    with open(DB_FILE, "w") as f:
        json.dump(db, f)

def store_file(file_bytes, file_name, file_type):
    file_id = str(uuid.uuid4())[:6]
    filepath = os.path.join(FILE_DIR, file_id)
    with open(filepath, "wb") as f:
        f.write(file_bytes)
    db = load_db()
    db[file_id] = {
        "name": file_name,
        "type": file_type,
        "timestamp": time.time()
    }
    save_db(db)
    return file_id

def retrieve_file(file_id):
    db = load_db()
    file_info = db.get(file_id)
    if not file_info:
        return None

    # Check if expired
    if time.time() - file_info["timestamp"] > EXPIRY_SECONDS:
        delete_file(file_id, silent=True)
        return None

    filepath = os.path.join(FILE_DIR, file_id)
    if not os.path.exists(filepath):
        return None

    with open(filepath, "rb") as f:
        content = f.read()
    return file_info["name"], file_info["type"], content

def delete_file(file_id, silent=False):
    db = load_db()
    if file_id in db:
        try:
            os.remove(os.path.join(FILE_DIR, file_id))
        except:
            if not silent:
                st.warning(f"Could not delete file: {file_id}")
        del db[file_id]
        save_db(db)
        if not silent:
            st.info(f"Deleted file: {file_id}")

def delete_expired_files():
    db = load_db()
    now = time.time()
    expired = []
    for file_id, info in list(db.items()):
        if now - info["timestamp"] > EXPIRY_SECONDS:
            delete_file(file_id, silent=True)
            expired.append(file_id)
    return expired

# --- Streamlit App ---

st.set_page_config(page_title="Instant File Transfer", page_icon="📤", layout="centered")
st.title("🌐 Instant File Transfer (No Storage)")

tab1, tab2, tab3 = st.tabs(["📎 Send File", "📥 Receive File", "🧹 Manage"])

# --- Tab 1: Send ---
with tab1:
    st.header("Upload and Share")

    file = st.file_uploader("Choose a file to send")
    if file and st.button("Upload"):
        file_id = store_file(file.read(), file.name, file.type)
        st.success("✅ File uploaded!")
        st.code(file_id, language="text")
        st.markdown(f"🔗 Share this ID to allow download")

# --- Tab 2: Receive ---
with tab2:
    st.header("Enter Code to Download")

    file_code = st.text_input("Enter 6-character file code").strip()
    if st.button("Download"):
        result = retrieve_file(file_code)
        if result:
            name, mime, content = result
            st.success(f"🎉 File found: {name}")
            st.download_button("⬇️ Download File", data=BytesIO(content), file_name=name, mime=mime)
        else:
            st.error("❌ Invalid or expired code")

# --- Tab 3: Manage / Cleanup ---
with tab3:
    st.header("🧹 Expired File Cleanup")
    if st.button("Clean Expired Files Now"):
        deleted = delete_expired_files()
        if deleted:
            st.success(f"🗑 Deleted {len(deleted)} expired files")
        else:
            st.info("✅ No expired files found")

    st.caption("Files expire after 1 hour and will be removed.")

