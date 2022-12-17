# import smtplib
# from email.message import EmailMessage
# from string import Template
# from pathlib import Path
#
# html = Template(Path('indexx.html').read_text())
# email = EmailMessage()
# email['from'] = 'Hogwarts School of Witchcraft and Wizardry'
# email['to'] = '###@#.com' #you need to add an email id here to whom you need to send the mail
# email['subject'] = 'Partial Horcrux'
# #email.set_content('Python here')
# email.set_content(html.substitute({'name': 'Harry','namee':'Voldemort'}), 'html')
#
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login('#mail', '#pass') #mail-> your mail id #pass-> your password
#     smtp.send_message(email)
#     print('All good Boss!')

import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sony789632145@gmail.com", "bboonnooOO7@")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sony789632145@gmail.com", "savepostyheroine@gmail.com", message)

# terminating the session
s.quit()