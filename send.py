import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def read_client_details(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            yield row['email'], row['first_name'], row['last_name']

def get_text_from_file(text_files_folder, first_name, last_name):
    file_path = os.path.join(text_files_folder, f"{first_name}_{last_name}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def send_emails(csv_file, text_files_folder):
    smtp_server = 'smtp.gmail.com'  # Gmail SMTP server
    smtp_port = 587  # Port for TLS
    sender_email = 'testprojectdaa@gmail.com'  # Your email
    password = 'nlng axzs dfru dnsn'  # Your app password

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)

        for email, first_name, last_name in read_client_details(csv_file):
            receiver_email = email
            text = get_text_from_file(text_files_folder, first_name, last_name)

            message = MIMEMultipart()
            message['From'] = sender_email
            message['To'] = receiver_email
            message['Subject'] = 'Test Email'

            body = text
            message.attach(MIMEText(body, 'plain'))

            server.sendmail(sender_email, receiver_email, message.as_string())

def main():
    csv_file = 'D:\\CustomMail\\data\\clients_medium.csv'  # CSV file path
    text_files_folder = 'D:\\CustomMail\\output'  # Folder containing text files

    send_emails(csv_file, text_files_folder)

if __name__ == "__main__":
    main()