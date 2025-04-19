 #______________FOLLOW THE COMMENTS IN CAPITAL______________#
    #___________________________________________________#


from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
import winsound
from datetime import datetime
import smtplib
from dotenv import load_dotenv
import os



over_due_count = 0
content  = ""


def make_beep():                # WHEN YOU ARE OFFLINE SYSTEM WILL MAKE BEEP SOUND 3 TIMES TO INFORM YOU 
    winsound.Beep(600,1000)
    winsound.Beep(400,1000)
    winsound.Beep(350,1000)

def check_connection(url):
    time.sleep(2)
    try:
        requests.get(url)
        return True
    except Exception as ex :
        return False

def send_mail(mail_subject="Assignments",mail_content=None,receiver=os.getenv('RECEIVER_EMAIL')):       # REPLACE UR RECEIVER EMAIL ID IN THE ENV FILE TO RECEIVE MAILS

    try:
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                sender_email = os.getenv('SENDER_EMAIL')  # REPLACE WITH YOUR MAIL ID IN THE ENV FILE
                app_password = os.getenv('APP_PASSWORD')  # REPLACE WITH YOUR APP PASSWORD IN THE ENV FILE(check the readme file for more info)
                server.login(sender_email, app_password)
                msg = f"Subject: {mail_subject}\n\n{mail_content}"
                server.sendmail(sender_email, receiver, msg)
                return True
    except Exception as ex:
                return False


def fetch_content():
    global content
    global over_due_count
    df = pd.read_csv("assignments.csv")
    for index, row in df.iterrows():
        submitted = row['Submitted']
        over_due = row['Over Due']
        if not submitted and not over_due:
            content += f"""{row['Assignment Name']} , Due Date - {row['Date']}\n"""
        if over_due and not submitted:
            over_due_count+=1
        


def create_file():
    with open("assignments.csv",'w') as fd:
        fd.write("Assignment Name,Over Due,Date,Submitted\n")




def write_into_file(text,over_due,date,submitted):

    new_data = [{
        'Assignment Name': text,
        'Over Due': over_due,
        'Date': date,
        'Submitted': submitted
    }]
    pd.DataFrame(new_data).to_csv("assignments.csv",mode='a',header=False,index=False)
    df = pd.read_csv("assignments.csv")
    df.dropna(subset=['Date'], inplace=True)
    df.to_csv("assignments.csv", index=False)

def find_date(text = None):
    try:
        arr = text.split()
        due_date = new_arr = " ".join(arr[2:])
        deadline = datetime.strptime(due_date, "%A, %d %B %Y, %I:%M %p")
        current_time = datetime.now()
        if current_time>deadline :
            return True,due_date        # returns true and the deadline if assignment is overdue
        else:
            return False,due_date       # returns Fasle and deadline if the assignment is not overdue
    except Exception as ex :
        print(ex)
        return None,None

def submission_status(driver):
    try:
        date=None
        submitted = None
        over_due = None
        assign_name = WebDriverWait(driver,2).until(
            EC.visibility_of_element_located((By.TAG_NAME,'h2'))
        )

        submission_table = WebDriverWait(driver,1).until(
            EC.visibility_of_element_located((By.CLASS_NAME,"submissionstatustable"))
        )

        rows = submission_table.find_elements(By.XPATH, "//tr[@class='r0' or @class='r1']")
        for row in rows :
           row_text = row.text.lower().strip()
           if "submission status" in row_text :
               if "no attempt" in row_text:
                   submitted =False
               else:
                   submitted =True
           elif "due date" in row_text:
               over_due, date = find_date(row_text)
        write_into_file(assign_name.text,over_due,date,submitted)
    except Exception as ex:
        pass
 


def handel_assignments(driver):
    try:
        assigns = WebDriverWait(driver, 5).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "instancename"))
        )

        for i in range(len(assigns)):
            assigns = WebDriverWait(driver, 5).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "instancename"))
            )
            assignment = assigns[i]

            try:
                driver.execute_script("""
                    arguments[0].scrollIntoView({block: 'center'});
                    arguments[0].click();
                """, assignment)
                submission_status(driver)
                driver.back()
            except Exception as e:
                print("Assignment click error:", e)

    except Exception as ex:
        print("Error in handel_assignments:", ex)

    


def handel_course(driver, course):
    try:
        link = course.find_element(By.TAG_NAME, 'a')
        href = link.get_attribute("href")

        # Open course in a new tab
        driver.execute_script(f"window.open('{href}', '_blank');")

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[-1])

        # Handle assignments in the new tab
        handel_assignments(driver)

        # Close the tab and switch back
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        return True
    except Exception as ex:
        print("Error in handel_course:", ex)
        return False

    
            

if __name__  == "__main__":
    try:

        url = "http://etcm.ticollege.org/cms/"  # COLLEGE PORTAL URL

        if not check_connection(url):       # CHECK IF YOU HAVE AN INTERNET CONNECTION
            make_beep()
            exit(0)

        load_dotenv()

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(url)

        user = os.getenv("STUDENT_ID")            # AHH , NOW REPLACE THIS WITH YOUR COLLEGE ID (IN THE ENV FILE)
        password = os.getenv("PASSWORD")     # REPLACE WITH YOUR PASSWORD IN THE ENV FILE
        my_courses = os.getenv("COURSES").split(',')     # ** SELECT THE COURSES YOU WANT , ENTER COURSES IN THE SAME FORMAT AS SHOWN IN THE EXAMPLE (ENV FILE )**

        user_box = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,".//input[@name = 'username']"))
        )

        pass_box = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,".//input[@name = 'password']"))
        )

        submit_btn = WebDriverWait(driver,10).until(
            EC.visibility_of_element_located((By.XPATH,".//input[@type = 'submit']"))
        )

        user_box.send_keys(user)
        pass_box.send_keys(password)
        submit_btn.click()



        tags = WebDriverWait(driver,10).until(
            EC.visibility_of_all_elements_located((By.TAG_NAME,'h3'))
        )
        create_file()
        for course in my_courses:
            for tag in tags :
                if course in tag.text.lower().strip():
                    handel_course(driver,tag)

        fetch_content()     # FOR FETCHING TOTAL NUMBER OF OVERDUE ASSIGNMENTS WHICH CAN BE SUBMITTED
        if content == "":
            content =f"You have 0 due assignments and {over_due_count} overdue assignments\n"
        else:
            content +=f"""\n submit these assignments asap.
                             You have {over_due_count} overdue assignments\n"""
        send_mail(mail_content=content)

        driver.quit()
    except Exception as ex :
        print("error occured, exiting...")
        print(ex)

        exit(1)