import imaplib
import email
from email.header import decode_header


def connect_to_mail(email_config):
    """Connect to the IMAP server using the provided email configuration."""
    mail = imaplib.IMAP4_SSL(email_config["imap_server"], email_config["imap_port"])
    mail.login(email_config["username"], email_config["app_password"])
    return mail


def fetch_unseen_emails(email_config):
    """Fetch and display all unseen emails."""
    mail = connect_to_mail(email_config)
    mail.select("inbox")
    status, messages = mail.search(None, "UNSEEN")
    mail_ids = messages[0].split()

    for i in mail_ids:
        status, msg_data = mail.fetch(i, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                display_email_info(msg)

    mail.logout()


def search_emails(email_config, search_criteria):
    """Search and display emails based on search criteria."""
    mail = connect_to_mail(email_config)
    mail.select("inbox")
    status, messages = mail.search(None, search_criteria)
    mail_ids = messages[0].split()

    for i in mail_ids:
        status, msg_data = mail.fetch(i, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                display_email_info(msg)

    mail.logout()


def display_email_info(msg):
    """Display the email information."""
