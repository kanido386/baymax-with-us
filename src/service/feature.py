import os
import requests
import random
import json

from linebot import LineBotApi
from linebot.models import (
    TextSendMessage, QuickReply, QuickReplyButton, MessageAction
)

# from dotenv import load_dotenv
# load_dotenv()

client_id = os.getenv("KKBOX_CLIENT_ID", None)
client_secret = os.getenv("KKBOX_CLIENT_SECRET", None)

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def get_feature():
    feature = [
        ('想聽某首歌', '聽 王藍茵 惡作劇'),
        ('聽點不一樣的', '隨機聽'),
        ('為久坐感到困擾？', '做運動'),
        ('想查證可疑訊息', '查證 手被刺扎到了，千萬別用針去挑，教你一招，不痛不癢，輕輕鬆鬆讓刺自己跑出來。\nhttps://youtu.be/cDW29J00yEY'),
        ('玩遊戲殺時間', '玩遊戲'),
        ('查看天氣', '新莊 天氣'),
        ('希望能加新功能', '新功能 記錄體重 希望能順便幫我用圖表來呈現我的體重變化'),
    ]
    return feature


def send_feature(reply_token):
    feature = get_feature()

    items = []
    N = len(feature)
    for i in range(N):
        button = QuickReplyButton(
            action=MessageAction(label=feature[i][0], text=feature[i][1]),
        )
        items.append(button)

    message = TextSendMessage(
        text='選一個功能試試吧！',
        quick_reply=QuickReply(
            items=items
        )
    )
    line_bot_api.reply_message(reply_token, message)