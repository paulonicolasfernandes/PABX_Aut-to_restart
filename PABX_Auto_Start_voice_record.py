from selenium import webdriver
import time
from PIL import Image
from selenium.webdriver.chrome.options import Options
import os
import smtplib

 

#login credentials
mylogin = "Username"
myPassword = "Password"

 

#assign driver to webdriver
driver = webdriver.Chrome()

#function to fill out username, password and then login
def login(url,usernameId, username, passwordId, password, submit_buttonId):
   driver.get(url)
   driver.find_element_by_id(usernameId).send_keys(username)
   driver.find_element_by_id(passwordId).send_keys(password)
    driver.find_element_by_id(submit_buttonId).click()

 
login("http://192.168.22.250/WebMC/users/login", "UserUsernameShow", mylogin, "UserPasswordShow", myPassword, "login_submit")

#follow path to recording service

driver.find_element_by_id("maintenance").click()
driver.find_element_by_id("Fea_Uti").click()
driver.find_element_by_id("Fea_Uti_Um_Aut_Two_Way_Rec").click()
driver.find_element_by_id("Fea_Uti_Um_Aut_Two_Way_Rec_Maintenance").click() 

#find HTML text if service is running and assign it to text
element = driver.find_element_by_id('status')
text = element.get_attribute('innerText')


#to test value of "text"
#print(text)


#(IF)compare text with with string for decision making
#if a match the start button is pushed and email is sent
#sending email,recieving email and password is assigned
#(gmail allow access to unsecure apps needs to be GRANTED)
#email settings and port number assigned
#logout button is clicked and application is closed

 

#(else) decision will logout and quit program
if text == "Service is stopped":
   driver.find_element_by_xpath('//*[@id="vumcardctl_auto2way_autorec"]').click()
   time.sleep(2)
   sender_email = "botemail@gmail.com"
   rec_email = ['paulonicolasfernandes@gmail.com', 'SecondEmail@gmail.com']
   password = 'EmailPassword'
   message = "Recording service has been RESTARTED"
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(sender_email, password)
   server.sendmail(sender_email, rec_email, message)
   time.sleep(8)
   logout_button = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a[1]')
   logout_button.click()
   time.sleep(2)
   driver.quit()

else:
   driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[3]/a[1]').click()
   time.sleep(2)
   driver.quit()
