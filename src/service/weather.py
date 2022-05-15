import os
import json
import urllib.parse

from linebot import LineBotApi
from linebot.models import FlexSendMessage

from googlesearch import search
from .basic import send_text_message

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_weather(reply_token, query):

    # query = query.replace(' ', '+')
    query = urllib.parse.quote(query)
    uri = f'https://www.google.com/search?q={query}'
    button = f"""
          {{
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {{
              "type": "uri",
              "label": "看天氣！",
              "uri": "{uri}"
            }},
            "color": "#6ec5e9"
          }}"""

    
    flex_message_json_string = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [""" + button + """
        ],
        "paddingAll": "12px",
        "spacing": "md"
      },
      "styles": {
        "footer": {
          "separator": false
        }
      }
    }
  ]
}
"""

    # print('==============================')
    # print(flex_message_json_string)
    # print('==============================')
    flex_message_json_dict = json.loads(flex_message_json_string)
    message = FlexSendMessage(
        alt_text="幫你查好天氣囉！",
        contents=flex_message_json_dict
    )
    
    line_bot_api.reply_message(reply_token, message)