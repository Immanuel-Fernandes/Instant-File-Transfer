# 🌐 Instant File Transfer (No Storage)

A lightweight, privacy-first file sharing web app built using **Streamlit**. Instantly upload and share files using a simple 6-character code. Files are stored temporarily and auto-deleted after 1 hour — no permanent storage, no login, no fuss.

🚀 **Live Demo:**  
🔗 [https://instant-file-transfer.streamlit.app](https://instant-file-transfer.streamlit.app)

---

## 🚀 Features

- 📎 **Send Files Instantly**  
  Upload any file and share a 6-character code to enable download.

- 📥 **Download by Code**  
  Enter a unique code to securely retrieve your file.

- 🧹 **Auto-Expiry & Cleanup**  
  Files automatically expire after **1 hour**. Manual cleanup supported for expired files.

- 🛡 **Privacy Focused**  
  No cloud storage or user tracking — everything stays local.

- 🧩 **Modular Design**  
  Cleanly separated logic for file handling, metadata, and UI.

---

## 🔧 Tech Stack

- **Frontend & Backend:** [Streamlit](https://streamlit.io/)
- **Language:** Python
- **Storage:** Local filesystem with JSON-based file database

---

## 📁 Project Structure

```plaintext
├── app.py              # Main Streamlit app
├── file_db.json        # Stores file metadata (name, type, timestamp)
├── files/              # Directory to store uploaded files
