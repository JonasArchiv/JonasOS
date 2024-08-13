import config
import send_mail_functions


def main():
    email_key = input("Enter email configuration key (e.g., 'email_1', 'email_2'): ")
    email_config = config.get_email_config(email_key)

    if not email_config:
        print(f"Configuration for '{email_key}' not found.")
        return

    to_address = input("Enter recipient's email address: ")
    subject = input("Enter subject of the email: ")
    body = input("Enter body of the email: ")

    send_mail_functions.send_email(email_config, to_address, subject, body)


if __name__ == "__main__":
    main()
