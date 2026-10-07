import streamlit as st
from PIL import Image
import pytesseract
import re
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image):

    text = pytesseract.image_to_string(image)

    return text

def get_date(text):
    pattern1 = r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}'
    match = re.search(pattern1, text, re.IGNORECASE)

    if match:
        return match.group()
    pattern2 = (
        r'\d{1,2}\s+'
        r'(January|February|March|April|May|June|July|August|'
        r'September|October|November|December)\s+\d{4}'
    )

    match = re.search(
        pattern2,
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return "Not Found"

def get_time(text):

    pattern = r'\d{1,2}:\d{2}\s*(AM|PM|am|pm)?'

    match = re.search(pattern, text, re.IGNORECASE)

    if match:
        return match.group()

    return "Not Found"

def get_venue(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if "venue" in line.lower():

            if ":" in line:
                return line.split(":", 1)[1].strip()

            return line

    for line in lines:

        line = line.strip()

        if (
            "auditorium" in line.lower()
            or "hall" in line.lower()
            or "campus" in line.lower()
            or "college" in line.lower()
        ):

            return line

    return "Not Found"

def get_event_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 5:

            if not re.search(r'\d', line):

                return line

    return "Event Not Found"

def get_reminder(date):

    try:

        # Convert 15/10/2026
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

            return f"{days} days remaining"

        elif days == 0:

            return "Event is TODAY!"

        else:

            return "Event completed"

    except:

        return "Reminder unavailable"

st.set_page_config(
    page_title="Smart Event Reminder",
    page_icon="🎫"
)


st.title("🎫 Smart Event Reminder")

st.write(
    "Upload an event poster and get the event details automatically."
)

file = st.file_uploader(
    "📤 Upload Event Poster",
    type=["jpg", "jpeg", "png"]
)


if file:

    image = Image.open(file)

    st.image(
        image,
        caption="Your Event Poster",
        use_container_width=True
    )

    if st.button("🔍 Scan Poster"):

        text = extract_text(image)

        event_name = get_event_name(text)

        date = get_date(text)

        time = get_time(text)

        venue = get_venue(text)

        reminder = get_reminder(date)

        st.success(
            "🎉 Event details found!"
        )


        st.subheader("✨ Event Details")


        st.write(
            "🎯 **Event:**",
            event_name
        )

        st.write(
            "📅 **Date:**",
            date
        )

        st.write(
            "⏰ **Time:**",
            time
        )

        st.write(
            "📍 **Venue:**",
            venue
        )

        st.write(
            "🔔 **Reminder:**",
            reminder
        )

        st.subheader("📝 Event Summary")

        st.info(
            f"{event_name} will be held on "
            f"{date} at {time} in {venue}."
        )


        with st.expander("📄 View OCR Text"):

            st.write(text)