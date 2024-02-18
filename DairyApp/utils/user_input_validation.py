import re

def is_valid_indian_mobile_number(number):
    # Regular expression pattern for Indian mobile numbers
    pattern = re.compile(r'^[7-9][0-9]{9}$')
    # Check if the number matches the pattern
    if pattern.match(number):
        return True
    else:
        return False