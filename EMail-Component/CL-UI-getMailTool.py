import config
import getMailTool


def main():
    email_key = input("Enter email configuration key (e.g., 'email_1', 'email_2'): ")
    email_config = config.get_email_config(email_key)

    if not email_config:
        print(f"Configuration for '{email_key}' not found.")
        return

    action = input(
        "Choose action:\n1. List unseen emails\n2. Search by keyword\n3. Search by sender\n4. List all emails in a folder\nEnter choice (1/2/3/4): ")

    if action == "1":
        getMailTool.fetch_unseen_emails(email_config)
    elif action == "2":
        search_keyword = input("Enter search keyword: ")
        getMailTool.search_emails(email_config, f'(BODY "{search_keyword}")')
    elif action == "3":
        sender_email = input("Enter sender email address: ")
        getMailTool.search_emails(email_config, f'(FROM "{sender_email}")')
    elif action == "4":
        folder_name = input("Enter folder name: ")
        getMailTool.fetch_emails_from_folder(email_config, folder_name)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
