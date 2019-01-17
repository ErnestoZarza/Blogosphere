from datetime import datetime


def parse_string_to_date(str_date):
    try:
        date = datetime.strptime(str_date, "%Y-%m-%d").date()
    except Exception:
        date = None

    return date