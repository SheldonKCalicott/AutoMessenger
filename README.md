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

> You can switch to Chrome by modifying the `webdriver.Firefox()` line in the code to use ChromeDriver instead.

To install dependencies:

```bash
pip install -r requirements.txt
