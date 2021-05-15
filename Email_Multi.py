
import smtplib 
#importing smtplib which is used for sending mail over net.

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 


# sender mail and password
#no input will be asked ,write explicitly here
sender_address="enter the sender email id"
sender_pass="enter the sender password"

list_receiver_email=["theirregular704@gmail.com","learnapply12345@gmail.com","adityasingh.rawat2020@vitstudent.ac.in"] #Planning to import excel sheet .csv file

length=len(list_receiver_email)

# here iterating the loop and send msg oen by one to the receiver

for i in range(length):
    X=list_receiver_email[i]
    receiver_mail=X
    print(receiver_mail)

    message=MIMEMultipart()
    message['From']=sender_address
    message['To']=receiver_mail
    message['Subject']='Mail using Python'

    content_mail='''Hello Myself K,
    This is a mail , I have written using python '''

    message.attach(MIMEText(content_mail,'plain')) 

    #to know the directory 
    import os

    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))

    #this code is for attachment purpose

    ##Create SMTP session for sending the mail
    # open the file to be sent  
    
    # filename = "enter the file name here!"

    # # Open PDF file in binary mode
    # # The file is in the directory same as where you run your Python script code from 
    
    # with open(filename, "rb") as attachment:
    #     # MIME attachment is a binary file for that content type "application/octet-stream" is used
    #     part = MIMEBase("application", "octet-stream")
    #     part.set_payload(attachment.read())
    
    # # encode into base64 
    # encoders.encode_base64(part) 

    # part.add_header('content-Disposition',"attachment;filename=%s" % filename)

    # message.attach(part) #attach the instance 'part' to instance 'message'


    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(sender_address,sender_pass)
    text=message.as_string()
    s.sendmail(sender_address,receiver_mail,text)
    s.quit()

    print("Mail Sent")
















