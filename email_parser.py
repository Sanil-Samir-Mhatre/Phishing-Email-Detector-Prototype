import email
from email.policy import default

def parse_email(file_path):
    import email
    from email import policy

    with open(file_path, "r") as f:
        msg = email.message_from_file(f, policy=policy.default)

    # Extract metadata and content
    email_data = {
        "From": msg["From"],
        "To": msg["To"],
        "Subject": msg["Subject"],
        "Date": msg["Date"],
        "Content": msg.get_body(preferencelist=("plain")).get_content() if msg.is_multipart() else msg.get_payload()
    }
    return email_data
