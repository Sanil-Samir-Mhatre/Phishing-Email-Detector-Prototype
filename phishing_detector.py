import re


def detect_phishing(email_content):
    phishing_indicators = {
        "Suspicious Links": r"https?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+",
        "Urgent Language": r"(urgent|immediately|action required)",
        "Sender Spoofing": r"(noreply@|admin@)"
    }

    flags = {}
    for key, pattern in phishing_indicators.items():
        flags[key] = bool(re.search(pattern, email_content, re.IGNORECASE))
    return flags


# Example Usage:
if __name__ == "__main__":
    content = "Please visit https://malicious-link.com immediately for urgent action."
    flags = detect_phishing(content)
    print(flags)
