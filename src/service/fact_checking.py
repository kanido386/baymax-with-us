import os
import json

from linebot import LineBotApi
from linebot.models import FlexSendMessage

from googlesearch import search
from .basic import send_text_message

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)


def send_fact_checking(reply_token, query):
    links = search(query, num_results=11, lang='zh-Hant')

    tfc_taiwan = []
    cofacts = []
    mygopen = []
    fact_checker = []
    rumtoast = []
    other = []

    links_source = [tfc_taiwan, cofacts, mygopen, fact_checker, rumtoast, other]
    link_source = [
        'tfc-taiwan.org.tw', 'cofacts.tw', 'mygopen.com', 'fact-checker.line.me',
        'rumtoast.com', ''
    ]
    name_source = [
        '台灣事實查核中心', 'Cofacts 真的假的', 'MyGoPen', 'LINE訊息查證', '蘭姆酒吐司', '其他'
    ]

    color_source = [
        '#333333', '#fed035', '#ef8e36', '#1bb71f', '#19a499', '#c8c8c8'
    ]

    # for link in links:
    #     # 台灣事實查核中心
    #     if 'tfc-taiwan.org.tw' in link:
    #         tfc_taiwan.append(link)
    #     # Cofacts 真的假的
    #     elif 'cofacts.tw' in link:
    #         cofacts.append(link)
    #     # MyGoPen
    #     elif 'mygopen.com' in link:
    #         mygopen.append(link)
    #     # LINE訊息查證
    #     elif 'fact-checker.line.me' in link:
    #         fact_checker.append(link)
    #     # 蘭姆酒吐司
    #     elif 'rumtoast.com' in link:
    #         rumtoast.append(link)
    #     else:
    #         other.append(link)

    num_source = len(link_source)

    for link in links:
        for i in range(num_source):
            if link_source[i] in link:
                links_source[i].append(link)
                break

    
    # result = ""
    result = []

    # for i in range(num_source):
    for i in range(num_source - 1):   # TODO: 先不顯示其他類的（因為很多垃圾）
        for link in links_source[i]:
            # result += f'{name_source[i]}：\n{link}\n\n'
            result.append((name_source[i], link, i))
            # TODO:
            break

    # result.append(('進行測試', 'https://www.mygopen.com', 0))
    # result.append(('進行測試', 'https://www.mygopen.com', 3))
    # result.append(('進行測試', 'https://www.mygopen.com', 5))
    
    contents = ""
    num_result = len(result)
    for i in range(num_result):
        color = color_source[result[i][2]]
        button = f"""
          {{
            "type": "button",
            "style": "primary",
            "height": "sm",
            "action": {{
              "type": "uri",
              "label": "{result[i][0]}",
              "uri": "{result[i][1]}"
            }},
            "color": "{color}"
          }},"""
        contents += button
    contents = contents[:-1]   # 去除多餘的逗號

    flex_message_json_string = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "kilo",
      "header": {
        "type": "box",
        "layout": "vertical",
        "contents": [
          {
            "type": "text",
            "text": "幫你查證囉！",
            "align": "center",
            "weight": "bold"
          }
        ],
        "backgroundColor": "#87cefa"
      },
      "body": {
        "type": "box",
        "layout": "vertical",
        "contents": [""" + contents + """
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

    # print(flex_message_json_string)

    flex_message_json_dict = json.loads(flex_message_json_string)
    # print('==============================')
    # print(flex_message_json_dict)
    # print(links_source)
    # print('==============================')

    message = FlexSendMessage(
        alt_text="幫你查證囉！",
        contents=flex_message_json_dict
    )

    if num_result == 0:
        send_text_message(reply_token, '找不太到欸\U0001f605')
    else:
        line_bot_api.reply_message(reply_token, message)

    # if result == '':
    #     result = '找不太到欸'

    # send_text_message(reply_token, result)