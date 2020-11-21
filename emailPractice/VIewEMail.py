import imaplib

M = imaplib.IMAP4_SSL("imap.gmail.com")
email = 'vaibhav.nigade@gmail.com'
password = 'kanclhczwongrgbv'
print(M.login(email,password))
print(M.list())
print(M.select('inbox'))

typ, data = M.search(None, 'SUBJECT "all things" ')
print(typ)
print(data)
emailid = data[0]
result, email_data = M.fetch(email, ("RFC822"))
print(email_data)

M.close()