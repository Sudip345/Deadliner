# 📚  Assignment Tracker (For Techno Main Only)

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
## There are predefined times in the env file you can change them as well , but the format must be the same  (24 hour).
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
**Don't forget to change the folder path with your folder path (where you are downloading this repo)**
---

## VBS ??
👉 for full automation . why to run it everytime ? just open your system and let it check itself .
just replace your folder path (where you have downloaded this repo) with the path mentioned in the **vbs** file.

---

# Finally 
**For windows**
press Win+R to open Run dialog box , enter "shell:startup" and paste the vbs file there .
Now whenever you open your system it it will automatically open your portal at your preferred time and check for due assignments

**Don't worry the program is light-weight and will not take much resources**

---

### ✅ Now You Are All Set 



