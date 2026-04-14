File Monitoring & WhatsApp Alert System

This project automatically monitors a folder and sends a WhatsApp alert whenever a new file is detected and processed.

🚀 What This Project Does
Continuously checks a folder for new files
Processes unprocessed files
Sends a WhatsApp alert using Twilio
Keeps track of processed files to avoid duplication
🧠 Real-World Example

Imagine your college uploads student data files daily into a folder.

👉 This system:

Detects new files automatically
Reads them
Sends you a WhatsApp alert like:
"File NOT processed: students_data.csv"

So you never miss any important data updates 📊

⚙️ How It Works (Step-by-Step)
Load Environment Variables
Reads sensitive data (like API keys) from .env file
Track Processed Files
Uses processed.txt to store already processed filenames
Scan Folder
Continuously checks the folder using os.listdir()
Check File Status
If file is already processed → skip
If new → process it
Process File
Reads and prints file content
Send WhatsApp Alert
Uses Twilio API to send message
Save File as Processed
Adds filename to processed.txt
Repeat
Waits for 10 seconds and runs again
🛠️ Technologies Used
Python 🐍
Twilio (WhatsApp API)
python-dotenv
OS & File Handling
📂 Project Structure
project-folder/
│
├── main.py
├── .env
├── processed.txt
└── README.md
🔑 Setup Instructions
1. Install Dependencies
pip install twilio python-dotenv

3. Create .env File
Add the following:

TWILIO_ACCOUNT_SID=your_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_WHATSAPP_FROM=whatsapp:+14155238886
TWILIO_WHATSAPP_TO=whatsapp:+91XXXXXXXXXX
FOLDER_PATH=your_folder_path

3. Run the Program
python main.py

⚠️ Notes
Make sure your Twilio WhatsApp sandbox is activated
Ensure folder path exists
Keep .env file private

🧾 Summary

This project is a simple automation system that:

Monitors files
Processes them
Sends WhatsApp alerts
Avoids duplicate work
