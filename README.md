# 📚 Techno Main Assignment Tracker

Automated Python script to check and notify students of **pending** or **overdue assignments** from the official Techno Main Salt Lake College portal.

---

## 🚀 Features

✅ Logs in automatically using your TMSL credentials  
✅ Opens selected courses and scans for assignments  
✅ Detects due dates and submission status  
✅ Sends an email report with pending & overdue assignments  
✅ Alerts you with a **beep** if you're offline  
✅ Smartly filters out already submitted tasks  
✅ Fully automated & customizable

---

## 🏫 Made for

🎓 **Techno Main Salt Lake**  
URL: [http://etcm.ticollege.org/cms](http://etcm.ticollege.org/cms)

---

## 🔧 How It Works

1. Reads your **Student ID**, **Password**, and **Course List** from a secure file  
2. Logs into your student portal  
3. Goes through each course one by one  
4. Opens assignments and checks:
   - **Due Date**
   - **Submission Status**
5. Stores assignment info in a CSV file  
6. Sends you a **summary email** like this:

---

## 🔧 Requirments 
**open terminal and paste the following**

**pip install selenium pandas requests python-dotenv pyinstaller**


# 🔧 Set your App Password

## 🔐 Step-by-Step: How to Get a Gmail App Password
**🔹 Step 1:** Go to Google Account Security Settings
👉 Visit: https://myaccount.google.com/security

**🔹 Step 2:** Enable 2-Step Verification (if not already)
Scroll down to **"Signing in to Google"**

**Click 2-Step Verification**

Set it up with your phone number or Google Prompt

**🔹 Step 3 :** Generate App Password
Once 2FA is enabled:

Go back to **https://myaccount.google.com/security**

Scroll to "Signing in to Google"

**Click "App Passwords"**

You may need to enter your password again.

Under "Select app", choose Mail

Under "Select device", choose Other (Custom name)
👉 Type something like AssignmentBot

Click Generate

**🔹 Step 4:** Copy the 16-character password
🔑 Google will give you a code like:

### abcd efgh ijkl mnop
👉 Use this in your env file like:

**APP_PASSWORD = "abcd efgh ijkl mnop"**

---
### Set your other creditnals in the env file 
---
### ✅ Now You Are All Set 

