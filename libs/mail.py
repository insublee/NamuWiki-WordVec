import smtplib
from email.mime.text import MIMEText
import json


def send(title, content, start_time, end_time):
    try:
        with open('info.json', 'r') as file:
            s = file.read()
            obj = json.loads(s)

            if 'email' in obj and 'api_key' in obj:
                if obj['email'] != '' and obj['api_key'] != '':
                    verified_send(title, content, start_time, end_time, obj)
    except:
        pass


def verified_send(title, content, start_time, end_time, data):
    mail_addr = data['email']
    time_info = "\n===========\n실행 시작: %s\n실행 종료: %s\n총 %s간 실행됨."%(
        str(start_time), str(end_time), str(end_time-start_time))
    msg = MIMEText(content+time_info)

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(data['email'], data['api_key'])

    msg['Subject'] = title
    msg['To'] = mail_addr
    server.sendmail(mail_addr, mail_addr, msg.as_string())
    server.quit()
