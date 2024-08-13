import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def connect_to_smtp(email_config):
    """Connect to the SMTP server using the provided email configuration."""
    server = smtplib.SMTP_SSL(email_config["smtp_server"], email_config["smtp_port"])
    server.login(email_config["username"], email_config["app_password"])
    return server


def send_email(email_config, to_address, subject, body):
    """Send an email using the provided configuration and email details."""
    server = connect_to_smtp(email_config)

    msg = MIMEMultipart()
    msg['From'] = email_config["username"]
    msg['To'] = to_address
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server.send_message(msg)
    server.quit()

    print(f"Email sent to {to_address} with subject '{subject}'")
