# 🌐 Instant File Transfer (Temporary, Private, No Persistent Storage)

A lightweight, privacy-focused file sharing app built using **Streamlit**. Instantly upload a file and generate a 6-character download code. Files are stored **temporarily (for 1 hour)** on the server and are automatically deleted — ensuring a minimal footprint and enhanced privacy.

🚀 **Live Demo:**  
🔗 [https://instant-file-transfer.streamlit.app](https://instant-file-transfer.streamlit.app)

---

## 📸 Preview

![Instant File Transfer Screenshot](Screenshots/Step%20(1).png)

---

## ✅ Features

- 📎 **Instant Upload**  
  Upload any file and receive a unique 6-character code for sharing.

- 📥 **Code-Based Download**  
  Enter a file code to securely retrieve the file.

- ⏳ **1-Hour Expiry**  
  Files automatically expire and are removed after 1 hour.

- 🧹 **Manual Cleanup**  
  Optional cleanup tab allows immediate deletion of expired files.

---

## ⚙️ Tech Stack

- **Frontend & Backend:** [Streamlit](https://streamlit.io/)
- **Language:** Python
- **Storage:** Local filesystem (`files/` directory), metadata stored in `file_db.json`

---

## 📁 Project Structure

```plaintext
├── app.py              # Main Streamlit app logic
├── file_db.json        # Temporary file metadata (name, type, timestamp)
├── files/              # Folder for temporarily stored files
├── LICENSE             # MIT License
├── Screenshot/         # UI preview image 
