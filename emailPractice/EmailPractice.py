import smtplib
import getpass
smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
print(smtp_obj.ehlo())
print(smtp_obj.starttls())
email = 'vaibhav.nigade@gmail.com'
password = 'kanclhczwongrgbv'
print(smtp_obj.login(email,password))
fromemail = email
toemail = 'vaibhav.nigade@gmail.com'
subject = "all things "
message  = "hi durgesh kasa ahes "

msg = "Subject: " + subject + '\n' +message


print(smtp_obj.sendmail(fromemail,toemail,msg))
smtp_obj.quit()
smtp_obj.close()