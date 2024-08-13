# Email configurations

email_configurations = {
    "email_1": {
        "username": "EMAIL_1",
        "app_password": "PASSWORD_1",
        "imap_server": "imap.server1.com",
        "imap_port": 993
    },
    "email_2": {
        "username": "EMAIL_2",
        "app_password": "PASSWORD_2",
        "imap_server": "imap.server2.com",
        "imap_port": 993
    }
}


def get_email_config(email_key):
    return email_configurations.get(email_key)
