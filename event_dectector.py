import re
from datetime import datetime


def get_date(text):

    match = re.search(
        r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}',
        text
    )

    return match.group() if match else "Not Found"


def get_time(text):

    match = re.search(
        r'\d{1,2}:\d{2}\s*(AM|PM|am|pm)?',
        text
    )

    return match.group() if match else "Not Found"


def get_venue(text):

    for line in text.split("\n"):

        if "venue" in line.lower():

            return line.strip()

    return "Not Found"


def get_reminder(date):

    try:

        event_date = datetime.strptime(
            date,
            "%d/%m/%Y"
        )

        today = datetime.now()

        days = (
            event_date.date()
            - today.date()
        ).days

        if days > 0:
            return f"⏳ {days} days remaining"

        elif days == 0:
            return "🔔 Event is Today!"

        else:
            return "⚪ Event completed"

    except:
        return "📅 Reminder unavailable"