import os
from twilio.rest import Client
from dotenv  import load_dotenv
import time
load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_from = os.getenv("TWILIO_WHATSAPP_FROM")
whatsapp_to = os.getenv("TWILIO_WHATSAPP_TO")

client = Client(account_sid, auth_token)

def load_processed_files():

    try:
        with open("processed.txt", "r") as f:
            return set(f.read().splitlines())
    except FileNotFoundError:
        return set()

def save_processed_file(filename):

    with open("processed.txt", "a") as f:
        f.write(filename + "\n")
def send_whatsapp_alert(filename):
    client.messages.create(
        body=f"🚨 ALERT 🚨\nFile NOT processed: {filename}",
        from_=whatsapp_from,
        to=whatsapp_to
    )

def process_file(filepath):
    with open(filepath, "r") as f:
        data = f.read()
        print("File content:")
        print(data)

folder_path = os.getenv("FOLDER_PATH")
CHECK_INTERVAL=10
while True:
    processed_files = load_processed_files()

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if file in processed_files:
            print("Already processed:", file)
        else:
            print("Not processed:", file)

            # FILE PROCESSING
            process_file(file_path)

            # SEND ALERT
            send_whatsapp_alert(file)

            # MARK AS PROCESSED
            save_processed_file(file)

    print(f"⏳ Sleeping for {CHECK_INTERVAL} seconds...\n")
    time.sleep(CHECK_INTERVAL)