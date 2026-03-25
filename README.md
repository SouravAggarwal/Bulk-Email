# Automated Bulk Email System

A robust, production-ready backend system built in Python to read recipient email addresses from an Excel file, iteratively send a customized, professional email (using both plain-text and custom HTML templates), and log the delivery status to an output Excel file.

## Features
- **Batch Email Sending**: Parse an Excel file and cleanly iterate over it to send emails.
- **Dual-Format Templates**: Automatically sends a `MIMEMultipart` email containing both a fallback plain-text body and a styling-rich HTML body.
- **Dynamic PDF Attachments**: Automatically scans the `data/` directory and attaches your PDF document securely.
- **Config-Driven**: Environment variables control sensitive credentials and operational parameters.
- **Data Validation**: Automatically ignores duplicates and invalid email formats.
- **Self-Healing Retries**: Retries up to a configured threshold if sending fails before logging as FAILED.
- **Rate-Limiting Built In**: Respects strict rate limits using artificial delays to reduce the chance of spam blocking by ESPs.
- **Audit Logging**: Keeps an exact timestamped record of every email attempted and its outcome.

---

## 🚀 Setup Requirements

### 1. Prerequisites
- **Python Version**: Python 3.8+ is recommended.
- Git installed on your system.

### 2. Installation
Clone this repository and install the required dependencies:
```bash
git clone https://github.com/YourUsername/Bulk-Email.git
cd Bulk-Email
pip install -r requirements.txt
```

### 3. Environment Configuration
Copy the provided example `.env` file to create your local `.env`. 
```bash
cp .env.example .env
```
Open `.env` and configure your settings:
*   `SENDER_EMAIL`: Your full email address (e.g., `you@gmail.com`).
*   `SENDER_PASSWORD`: Your unique App Password (see instructions below).
*   `DELAY_BETWEEN_EMAILS_SECONDS`: Rate limit delay (default 5 seconds).

#### ⚠️ Gmail App Password Setup (CRITICAL)
If you are using a standard Gmail account to send these emails, **you cannot use your standard login password** due to Google's strict security restrictions. You must generate a dedicated App Password:

1. Enable **2-Step Verification** for your Google Account.
2. Go to your Google Account Settings -> **Security**.
3. Under the "How you sign in to Google" section, search for **App passwords**.
4. Give the app a custom name (e.g., "Python Bulk Email").
5. Click **Generate**.
6. Google will provide a **16-character password**. Copy this and paste it directly into your `.env` file under `SENDER_PASSWORD`. *(Note: Ignore the spaces when copying).*

---

## 💡 How to Use

### Step 1: Prepare Your Recipient Data
Place your list of target recipient emails in an Excel file at `data/input_emails.xlsx`. 
- **Requirement:** The file must contain at least one column titled exactly `email`. 
- *Tip: If you want to test the system first without creating a list, run `python generate_sample.py` to auto-generate a mock file with valid and invalid dummy emails.*

### Step 2: Customize Your Templates
Open `email_templates.py`. This file contains three generic templates:
1. `EMAIL_SUBJECT_TEMPLATE`: The subject line.
2. `EMAIL_BODY_TEMPLATE`: The fallback plain-text version of your email.
3. `EMAIL_HTML_TEMPLATE`: A premium, professionally designed HTML version of your email.

**Action needed**: Replace all the generic bracketed placeholders (e.g., `[Your Name]`, `[Your Main Message]`) with your actual content and links.

### Step 3: Attach Your Document
Simply drop your target PDF file into the `data/` directory. 
The system (`email_sender.py`) will automatically scan this folder, find the first `.pdf` file, and securely attach it to every outbound email.

### Step 4: Run the Engine
Execute the main orchestration script:
```bash
python main.py
```
The console will output the progress live as it navigates the list, waits for the configured rate-limit delay, and processes the queue.

### Step 5: Review the Logs
After completion, examine the `data/log.xlsx` file. It will contain an exact audit history of every email attempted, the timestamp, and whether it succeeded (`SUCCESS`) or failed (`FAILED`).
