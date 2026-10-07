import streamlit as st
from PIL import Image

from ocr import extract_text

from event_detector import (
    get_date,
    get_time,
    get_venue,
    get_reminder
)

import re


def get_event_name(text):

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 5:

            if not re.search(r'\d', line):

                return line

    return "Event Not Found"


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

        st.success("🎉 Event details found!")

        st.subheader("✨ Event Details")

        st.write("🎯 **Event:**", event_name)

        st.write("📅 **Date:**", date)

        st.write("⏰ **Time:**", time)

        st.write("📍 **Venue:**", venue)

        st.write("🔔 **Reminder:**", reminder)

        st.subheader("📝 Event Summary")

        st.info(
            f"{event_name} will be held on "
            f"{date} at {time} in {venue}."
        )

        with st.expander("📄 View OCR Text"):

            st.write(text)