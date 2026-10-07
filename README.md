# Smart Event Reminder

A beginner-friendly AI-based web application that extracts event details from event posters using OCR and provides a simple event reminder.

## Project Overview

Smart Event Reminder allows users to upload an event poster image and automatically extract important event information such as:

- Event Name
- Date
- Time
- Venue
- Reminder Status

The application uses Optical Character Recognition (OCR) to read the text from the uploaded poster.

## Demo Link :

https://5hgwspxx69zzi7g8nu3xm2.streamlit.app/

## Features

- Upload event posters in JPG, JPEG, and PNG formats
- Extract text automatically from images
- Detect event name
- Detect event date
- Detect event time
- Detect venue
- Calculate remaining days for the event
- Display event summary
- View complete OCR text
- Simple and beginner-friendly Streamlit interface

## Technologies Used

- Python
- Streamlit
- Tesseract OCR
- Pytesseract
- Pillow
- Regular Expressions

## Project Structure

Smart Event Reminder/
│
├── app.py
├── ocr.py
├── event_detector.py
├── requirements.txt
├── packages.txt
└── README.md

## How It Works

Upload Event Poster
        ↓
Read Image
        ↓
OCR using Tesseract
        ↓
Extract Text
        ↓
Detect Event Details
        ↓
Calculate Reminder
        ↓
Display Event Information

## File Description

### app.py

This is the main Streamlit application.

It handles:

- User interface
- Image upload
- Poster preview
- Scan button
- Event details display
- Event summary
- OCR text display

### ocr.py

This file handles Optical Character Recognition.

It uses Pytesseract and Tesseract OCR to extract text from the uploaded event poster.

### event_detector.py

This file contains the event information detection functions.

It detects:

- Date
- Time
- Venue
- Reminder status

### requirements.txt

This file contains the Python dependencies required for the application.

streamlit
pytesseract
Pillow

### packages.txt

This file installs the Tesseract OCR system package when deploying the application on Streamlit Cloud.

tesseract-ocr

## Installation

### Step 1: Clone the Repository

git clone https://github.com/yuvashrisasikala-ctrl/-smart-event-reminder.git

### Step 2: Open the Project

Open the project folder in Visual Studio Code.

### Step 3: Install Python Packages

Open the terminal and run:

py -m pip install -r requirements.txt

### Step 4: Install Tesseract OCR

For Windows, install Tesseract OCR on your system.

The application uses:

C:\Program Files\Tesseract-OCR\tesseract.exe

### Step 5: Run the Application

Run the following command in the VS Code terminal:

py -m streamlit run app.py

The application will open in the browser.

## Usage

1. Open the Smart Event Reminder application.
2. Click Upload Event Poster.
3. Select an event poster image.
4. Preview the uploaded poster.
5. Click Scan Poster.
6. The application extracts text using OCR.
7. Event details are detected automatically.
8. The event name, date, time, venue, and reminder status are displayed.
9. The complete OCR text can be viewed using the OCR Text section.

## Example Output

Event: Tech Symposium

Date: 15/10/2026

Time: 10:00 AM

Venue: College Auditorium

Reminder: 8 days remaining

The actual output depends on the text available in the uploaded event poster.

## Reminder Logic

The application compares the detected event date with the current date.

### Future Event

⏳ X days remaining

### Today's Event

🔔 Event is Today!

### Completed Event

⚪ Event completed

### Invalid or Unsupported Date

📅 Reminder unavailable

## OCR

OCR stands for Optical Character Recognition.

It is used to convert text present in an image into machine-readable text.

In this project:

Event Poster Image
        ↓
Tesseract OCR
        ↓
Extracted Text

The extracted text is then processed to identify event information.

## Deployment

The application can be deployed using Streamlit Cloud.

For Streamlit Cloud deployment, the repository should contain:

app.py
ocr.py
event_detector.py
requirements.txt
packages.txt

The packages.txt file is important because Tesseract OCR is a system-level dependency.

## Limitations

- OCR accuracy depends on the quality of the event poster.
- Blurry or low-resolution images may produce incorrect text.
- Unusual fonts may affect OCR results.
- Complex poster layouts may affect text extraction.
- Date and time formats may vary.
- Venue detection currently depends on the presence of the word "venue".

## Future Enhancements

- Better event name detection
- Multiple date format support
- More time format support
- Automatic calendar integration
- Email reminders
- Notification alerts
- Google Calendar integration
- Better OCR preprocessing
- Support for multiple languages
- AI-based event information extraction
- Countdown timer
- Downloadable event details

## Learning Outcomes

Through this project, I learned:

- Python programming
- Streamlit application development
- OCR using Tesseract
- Image processing using Pillow
- Text extraction from images
- Regular expressions
- Python modules and imports
- Deploying applications using Streamlit Cloud
- Managing project dependencies

## Conclusion

Smart Event Reminder is a simple AI-based application that makes it easier to obtain important information from event posters. By combining OCR, Python, and Streamlit, the application automatically extracts event details and provides a reminder status based on the event date.

## License

This project is created for educational and learning purposes.
