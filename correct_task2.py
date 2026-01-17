# Write your corrected implementation for Task 2 here.
# Do not modify `task2.py`.
import re

def count_valid_emails(emails):
    """
    Counts the number of valid email addresses in a list.
    
    Args:
        emails (list): A list of potential email strings.
        
    Returns:
        int: Total number of valid emails found.
    """
    if not isinstance(emails, list):
        return 0

    count = 0
    # A simple but effective email regex: user@domain.com
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")

    for email in emails:
        # Ensure email is a string to avoid crashes on None or other types
        if isinstance(email, str) and email_pattern.match(email):
            count += 1

    return count
