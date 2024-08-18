from datetime import datetime


def calculate_age(birthdate_str):
    birthdate = datetime.strptime(str(birthdate_str), '%Y-%m-%d %H:%M:%S')
    today = datetime.now()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))


def safe_float(value):
    try:
        return float(value)
    except ValueError:
        return 0.0
