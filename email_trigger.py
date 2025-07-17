import smtplib
from email.message import EmailMessage
import os

# Email configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'samavedam1999@gmail.com'
EMAIL_PASSWORD = 'ugfc nrsq zamf riff' #Use an app password for Gmail


def send_email(name):
    print("entered email function")
    excel_file = name 
    def send_report():
        print("Sending email with the report...")
        sending_email = EMAIL_ADDRESS
        msg = EmailMessage()
        msg['Subject'] = 'Wrogn Products Extraction Report'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = 'Sometemp8796@outlook.com,dattasahu515@gmail.com,send_some_try@yahoo.com'
        msg.set_content('Please find attached the latest Wrogn products extraction report.')

        # Attach Excel file
        if os.path.exists(excel_file):
            with open(excel_file, 'rb') as f:
                file_data = f.read()
                msg.add_attachment(file_data, maintype='application', subtype='vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=excel_file)
        else:
            print(f"File {excel_file} not found.")

        # Send email
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
                smtp.starttls()
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("Email sent successfully!")
        except Exception as e:
            print(f"Failed to send email: {e}")
    send_report()
