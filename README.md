# AutoMessenger

**Desktop Mass Messaging Automation Tool**

AutoMessenger is a custom-built desktop application that streamlines the process of sending personalized text messages to multiple recipients using [Google Messages Web](https://messages.google.com/web/). Built with Python, Selenium, and Tkinter, this app automates browser interactions to deliver custom messages at scale. It is especially useful for shift coordination, outreach, or time-sensitive updates where speed, accuracy, and automation are essential.

---

## Features

- Upload contacts directly from a CSV file (`Name` and `Phone` columns required)
- Automatically formats phone numbers and filters invalid entries
- Sends personalized messages via Google Messages Web
- Customize location and time ranges through a user-friendly interface
- Live message preview that updates based on input
- Retry logic for message delivery failures
- Confirmation dialogs and user prompts to guide the process

---

## Interface Overview

The application includes:

- A CSV file selector
- A recipient preview window
- Message settings for location and time
- A message preview text box
- A "Send Messages" button to initiate the process

---

## Requirements

- Python 3.8 or higher
- Google Chrome or Firefox browser (Google Messages Web must be paired with your phone)
- Selenium WebDriver (currently configured for Firefox via GeckoDriver)

Install the required Python l
