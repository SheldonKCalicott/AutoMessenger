# AutoMessenger

**Desktop Mass Messaging Automation Tool**

AutoMessenger is a custom-built desktop application that streamlines the process of sending personalized text messages to multiple recipients using Google Messages Web. Built with Python, Selenium, and Tkinter, this app automates browser interactions to deliver custom messages at scale. It is especially useful for shift coordination, outreach, or time-sensitive updates where speed, accuracy, and automation are essential.

---

## Features

- Upload contacts directly from a CSV file (requires `Name` and `Phone` columns)
- Automatically formats phone numbers and filters out invalid entries
- Customizable message preview with live updates
- Location and time range inputs for dynamic message content
- Message delivery automation using Google Messages Web
- Retry logic for failed deliveries
- Easy-to-use desktop interface
- Secure: no data is uploaded or stored externally

---

## Interface Overview

The application includes:

- CSV file selector for loading recipient contacts
- Scrollable preview of contact names
- Dropdowns for customizing location and time
- Live-updating message preview box
- "Send Messages" button to start automation

---

## Requirements

- **Python 3.8+**
- **Selenium**
- **Pandas**
- **Tkinter** (included with most Python installations)
- **Firefox Browser**
- **GeckoDriver** (added to your system PATH)

---

## CSV Format

Phone numbers must have at least 10 digits. Non-digit characters are removed automatically.
- Name,Phone
- John Doe,555-123-4567
- Jane Smith,(123) 456-7890

---

## How To Use

- Clone or download this repository.
- Ensure GeckoDriver is installed and in your system PATH.

Run the script:
- python automessenger.py

- Select your CSV file when prompted.
- Customize the location and time settings.
- Review the message preview.
- Click Send Messages.
- Follow the prompt to pair your phone with Google Messages Web.
- The app will begin sending messages automatically.

---

> You can switch to Chrome by modifying the `webdriver.Firefox()` line in the code to use ChromeDriver instead.

To install dependencies:

```bash
pip install -r requirements.txt
