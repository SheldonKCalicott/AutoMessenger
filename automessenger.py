# AutoMessenger - Automated Mass Messaging Tool using Google Messages Web

import time
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Global variable to hold the CSV file path
file_path = None

# Format hour and minute into 12-hour AM/PM format
def format_time(hour, minute=0):
    suffix = "AM" if hour < 12 or hour == 24 else "PM"
    display_hour = hour % 12 or 12
    return f"{display_hour}:{minute:02} {suffix}"

# Prompt user to select a CSV file and return the path
def csv_filepath():
    root = tk.Tk()
    root.withdraw()
    root.focus_force()
    return filedialog.askopenfilename(
        title='Select a CSV file',
        filetypes=[('CSV files', '*.csv'), ('All files', '*.*')]
    )

# Send messages to phone numbers in the provided CSV file using Selenium
def send_messages(msg, file_path):
    driver = webdriver.Firefox()
    driver.get("https://messages.google.com/web/conversations")
    messagebox.showinfo("Pairing Required", "Please pair a device to Google Messages and then click OK to continue.")

    if file_path:
        df = pd.read_csv(file_path)
        if "Phone" not in df.columns or "Name" not in df.columns:
            messagebox.showerror("Invalid File", "CSV must contain 'Name' and 'Phone' columns.")
            driver.quit()
            return

        df["Phone"] = df["Phone"].astype(str)
        phone_list = df["Phone"].str.replace(r'\D', '', regex=True)
        phone_list = phone_list[phone_list.str.len() >= 10]
    else:
        messagebox.showinfo("No File Selected", "Please select a CSV file.")
        driver.quit()
        return

    for phone_number in phone_list:
        retries = 10
        while retries > 0:
            try:
                start_chat = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".fab-label")))
                start_chat.click()

                search_box = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".input")))
                search_box.clear()
                search_box.send_keys(phone_number)
                time.sleep(2)
                search_box.send_keys(Keys.ENTER)

                message_box = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.input")))
                message_box.send_keys(msg)
                message_box.send_keys(Keys.ENTER)
                time.sleep(2)
                break
            except Exception:
                retries -= 1
                if retries == 0:
                    messagebox.showinfo("Failed", f"Max retries reached for: {phone_number}")
                    break
                continue

    messagebox.showinfo("Success", "Messages sent successfully!")
    driver.quit()

# Main function to run the GUI
def main():
    global file_path

    root = tk.Tk()
    root.title("AutoMessenger")
    root.geometry("900x700")
    root.configure(bg="#2C2F33")

    # App header and subtitle
    header = tk.Label(
        root,
        text="AutoMessenger",
        font=("Helvetica", 22, "bold"),
        bg="#2C2F33",
        fg="#FFFFFF"
    )
    header.pack(pady=(20, 5))

    subheader = tk.Label(
        root,
        text="Smart automation for sending personalized group messages from CSV contacts.",
        font=("Helvetica", 12),
        bg="#2C2F33",
        fg="#CCCCCC"
    )
    subheader.pack(pady=(0, 15))

    # Layout frames for organization
    content_frame = tk.Frame(root, bg="#2C2F33")
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    left_frame = tk.Frame(content_frame, bg="#2C2F33")
    left_frame.pack(side="left", fill="y", padx=(0, 30))

    right_frame = tk.Frame(content_frame, bg="#2C2F33")
    right_frame.pack(side="left", fill="both", expand=True)

    # File selection and recipient name list
    def select_file(textbox, label):
        global file_path
        file_path = csv_filepath()
        if file_path:
            try:
                df = pd.read_csv(file_path)
                if "Name" not in df.columns or "Phone" not in df.columns:
                    raise ValueError
                names = df["Name"].dropna().tolist()
                textbox.delete("1.0", tk.END)
                for name in names:
                    textbox.insert(tk.END, name + "\n")
                label.config(text=f"Recipient Names ({len(names)})")
            except Exception:
                messagebox.showerror("Invalid File", "CSV must contain 'Name' and 'Phone' columns.")

    file_button = tk.Button(
        left_frame, text="Select CSV File", command=lambda: select_file(names_textbox, names_label),
        bg="#4E91F7", fg="white", font=("Helvetica", 10, "bold")
    )
    file_button.pack(pady=(0, 10), fill="x")

    names_label = tk.Label(left_frame, text="Recipient Names", font=("Helvetica", 11, "bold"), bg="#2C2F33", fg="white")
    names_label.pack(anchor="w")

    names_textbox = tk.Text(left_frame, height=25, width=30, wrap=tk.WORD, bg="#F0F0F0", fg="#333333")
    names_textbox.pack(pady=(5, 0), side="left", fill="y")

    names_scrollbar = tk.Scrollbar(left_frame, command=names_textbox.yview)
    names_scrollbar.pack(side="right", fill="y")
    names_textbox.config(yscrollcommand=names_scrollbar.set)

    # Settings section: location and time selection
    settings_box = tk.LabelFrame(right_frame, text="Message Settings", font=("Helvetica", 11, "bold"), bg="#2C2F33", fg="white")
    settings_box.pack(fill="x", padx=10, pady=(0, 10))

    location_label = tk.Label(settings_box, text="Location:", bg="#2C2F33", fg="white")
    location_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    location_var = tk.StringVar()
    location_var.set("Location 1")
    location_dropdown = ttk.OptionMenu(settings_box, location_var, "Location 1", "Location 1", "Location 2", command=lambda _: update_message())
    location_dropdown.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    start_label = tk.Label(settings_box, text="Start Time:", bg="#2C2F33", fg="white")
    start_label.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    start_time_var = tk.StringVar()
    time_values = [format_time(h, m) for h in range(24) for m in (0, 15, 30, 45)]
    start_time_var.set(format_time(11))
    start_time_dropdown = ttk.Combobox(settings_box, textvariable=start_time_var, values=time_values, state="readonly", width=12)
    start_time_dropdown.grid(row=1, column=1, padx=10, pady=5)
    start_time_dropdown.bind("<<ComboboxSelected>>", lambda _: update_message())

    end_label = tk.Label(settings_box, text="End Time:", bg="#2C2F33", fg="white")
    end_label.grid(row=0, column=2, padx=10, pady=5, sticky="w")

    end_time_var = tk.StringVar()
    end_time_var.set(format_time(15))
    end_time_dropdown = ttk.Combobox(settings_box, textvariable=end_time_var, values=time_values, state="readonly", width=12)
    end_time_dropdown.grid(row=1, column=2, padx=10, pady=5)
    end_time_dropdown.bind("<<ComboboxSelected>>", lambda _: update_message())

    # Message preview area
    msg_label = tk.Label(right_frame, text="Message Preview", font=("Helvetica", 11, "bold"), bg="#2C2F33", fg="white")
    msg_label.pack(anchor="w", padx=10)

    msg_text = tk.Text(right_frame, height=10, wrap=tk.WORD, bg="#F8F8F8", fg="#333333")
    msg_text.pack(fill="both", padx=10, pady=5, expand=True)

    msg_scrollbar = tk.Scrollbar(msg_text, command=msg_text.yview)
    msg_text.config(yscrollcommand=msg_scrollbar.set)
    msg_scrollbar.pack(side="right", fill="y")

    # Auto-update preview message when settings change
    def update_message():
        location = location_var.get()
        start_time = start_time_var.get()
        end_time = end_time_var.get()
        default_msg = (
            f"Hello!\n\n"
            f"We’d like to invite you to an upcoming opportunity at {location}. "
            f"You’re welcome to join us anytime between {start_time} and {end_time}.\n\n"
            f"Spots are limited, so please reply if you're interested. "
            f"Looking forward to hearing from you!"
        )
        msg_text.config(state="normal")
        msg_text.delete("1.0", tk.END)
        msg_text.insert(tk.END, default_msg)

    update_message()

    # Run button to send messages
    def run_program():
        msg = msg_text.get("1.0", tk.END).strip()
        if file_path:
            send_messages(msg, file_path)
        else:
            messagebox.showinfo("No File Selected", "Please select a CSV file before running the program.")

    run_button = tk.Button(root, text="Send Messages", command=run_program, bg="#28A745", fg="white", font=("Helvetica", 11, "bold"))
    run_button.pack(pady=10)

    root.mainloop()

# Start the application
if __name__ == "__main__":
    main()
