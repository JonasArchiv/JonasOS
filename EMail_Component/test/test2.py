import imaplib
import email
from email.header import decode_header
import config

email_key = "email_1"
email_config = config.get_email_config(email_key)

if email_config:
    username = email_config["username"]
    app_password = email_config["app_password"]
    imap_server = email_config["imap_server"]
    imap_port = email_config["imap_port"]

    mail = imaplib.IMAP4_SSL(imap_server, imap_port)
    mail.login(username, app_password)

    status, folders = mail.list()

    for folder in folders:
        folder_name = folder.decode().split(' "/" ')[-1]
        mail.select(folder_name)
        status, messages = mail.search(None, "UNSEEN")
        mail_ids = messages[0].split()

        print(f"--- Search in Folder: {folder_name} ---")

        for i in mail_ids:
            status, msg_data = mail.fetch(i, "(RFC822)")

            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    from_ = msg.get("From")
                    print("From:", from_)

                    subject, encoding = decode_header(msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding if encoding else "utf-8")
                    print("Subject:", subject)

                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))

                            try:
                                body = part.get_payload(decode=True).decode()
                                if content_type == "text/plain" and "attachment" not in content_disposition:
                                    print("Message:", body)
                            except:
                                pass
                    else:
                        content_type = msg.get_content_type()
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                            print("Message:", body)

            print("=" * 50)

    mail.logout()
else:
    print(f"Konfiguration für '{email_key}' nicht gefunden.")
