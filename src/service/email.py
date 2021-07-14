# https://www.learncodewithmike.com/2020/02/python-email.html

import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from .basic import send_text_message

gmail_password = os.getenv("GMAIL_PASSWORD", None)

def send_email_to_kanido(reply_token, feature_name, description):

    content = MIMEMultipart()
    content['subject'] = '【杯麵】新功能請求'                        # 標題
    content['from'] = 'Baymax'                                    # 寄件者
    content['to'] = 'kanido386@gmail.com'                         # 收件者
    content.attach(MIMEText(f'{feature_name}\n\n{description}'))  # 內容

    with smtplib.SMTP(host='smtp.gmail.com', port='587') as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()                                            # 驗證SMTP伺服器
            smtp.starttls()                                        # 建立加密傳輸
            smtp.login('kanido386@gmail.com', gmail_password)  # 登入寄件者gmail
            smtp.send_message(content)                             # 寄送郵件
            send_text_message(reply_token, f'{feature_name}能讓我成為更好的小幫手\U0001f914')
        except Exception as e:
            send_text_message(reply_token, '增加新功能的服務出了點狀況，去問問我的好麻吉彥廷哥哥吧！')