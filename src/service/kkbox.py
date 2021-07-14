import os
import requests
import random
import json

from linebot import LineBotApi
from linebot.models import (
    TextSendMessage, FlexSendMessage, QuickReply, QuickReplyButton, PostbackAction
)

# from dotenv import load_dotenv
# load_dotenv()

client_id = os.getenv("KKBOX_CLIENT_ID", None)
client_secret = os.getenv("KKBOX_CLIENT_SECRET", None)

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)



def send_random_playlists(reply_token, N):
    playlists = get_chart_playlists(N)

    items = []
    for i in range(N):
        # button = QuickReplyButton(
        #     action=MessageAction(label=f"{playlists[i][1]}", text=f"{playlists[i][1]}")
        # )
        button = QuickReplyButton(
            action=PostbackAction(label=playlists[i][1], data=f'playlist {playlists[i][0]}', text=playlists[i][1])
        )
        items.append(button)

    message = TextSendMessage(
        text='選一個你感興趣的排行榜吧！',
        quick_reply=QuickReply(
            items=items
        )
    )
    line_bot_api.reply_message(reply_token, message)



def send_random_tracks(reply_token, playlist_id, N):

    tracks = get_tracks_of_chart_playlist(playlist_id, N)

    contents = ""
    for i in range(N):
        color = generate_random_color()
        label = f"{tracks[i][0]} - {tracks[i][1]}"[:40]
        button = f"""
          {{
            "type": "button",
            "height": "sm",
            "action": {{
              "type": "message",
              "label": "{label}",
              "text": "聽 {tracks[i][0]} {tracks[i][1]}"
            }},
            "color": "{color}"
          }},"""
        contents += button
    contents = contents[:-1]   # 去除多餘的逗號

    # TODO: 若想更改介面
#     flex_message_json_string = """
# {
#   "type": "carousel",
#   "contents": [
#     {
#       "type": "bubble",
#       "size": "giga",
#       "body": {
#         "type": "box",
#         "layout": "vertical",
#         "contents": [
#           {
#             "type": "text",
#             "text": "這是誰唱的"
#           },
#           {
#             "type": "text",
#             "text": "哪一首歌呢"
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "text",
#             "text": "這是誰唱的"
#           },
#           {
#             "type": "text",
#             "text": "哪一首歌呢"
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "text",
#             "text": "這是誰唱的"
#           },
#           {
#             "type": "text",
#             "text": "哪一首歌呢"
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "text",
#             "text": "這是誰唱的"
#           },
#           {
#             "type": "text",
#             "text": "哪一首歌呢"
#           },
#           {
#             "type": "separator"
#           },
#           {
#             "type": "text",
#             "text": "這是誰唱的"
#           },
#           {
#             "type": "text",
#             "text": "哪一首歌呢"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "試試這首",
#               "text": "聽進行測試"
#             },
#             "position": "absolute",
#             "offsetEnd": "5px",
#             "offsetTop": "10px"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "試試這首",
#               "text": "聽進行測試"
#             },
#             "position": "absolute",
#             "offsetEnd": "5px",
#             "offsetTop": "80px"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "試試這首",
#               "text": "聽進行測試"
#             },
#             "position": "absolute",
#             "offsetTop": "150px",
#             "offsetEnd": "5px"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "試試這首",
#               "text": "聽進行測試"
#             },
#             "position": "absolute",
#             "offsetEnd": "5px",
#             "offsetBottom": "80px"
#           },
#           {
#             "type": "button",
#             "action": {
#               "type": "message",
#               "label": "試試這首",
#               "text": "聽進行測試"
#             },
#             "position": "absolute",
#             "offsetEnd": "5px",
#             "offsetBottom": "10px"
#           }
#         ],
#         "spacing": "md",
#         "paddingAll": "15px"
#       },
#       "styles": {
#         "footer": {
#           "separator": false
#         }
#       }
#     }
#   ]
# }
# """

    flex_message_json_string = """
{
  "type": "carousel",
  "contents": [
    {
      "type": "bubble",
      "size": "giga",
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
    message = FlexSendMessage(
        alt_text="選一首試試吧！",
        contents=flex_message_json_dict
    )

    line_bot_api.reply_message(reply_token, message)



def get_access_token():
  
    url = 'https://account.kkbox.com/oauth2/token'

    headers = {
        'Host': 'account.kkbox.com',
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    data = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    access_token = requests.post(url, headers=headers, data=data)
    return access_token.json()['access_token']



# https://docs-en.kkbox.codes/#get-/charts
def get_chart_playlists(N):

    playlists = []
  
    access_token = get_access_token()

    url = 'https://api.kkbox.com/v1.1/charts'

    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {access_token}'
    }

    params = {
        'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
        'offset': 0,
        'limit': 30
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
        # print(item['id'], item['title'])
        # print('==============================')
        playlists.append((item['id'], item['title']))
    # print(playlists)
    
    # return random.choices(playlists, k=N)
    return random.sample(playlists, k=N)



# https://docs-en.kkbox.codes/#get-/charts/{playlist_id}/tracks
def get_tracks_of_chart_playlist(playlist_id, N):

    tracks = []

    access_token = get_access_token()

    url = f'https://api.kkbox.com/v1.1/charts/{playlist_id}/tracks'

    headers = {
        'accept': 'application/json',
        'authorization': f'Bearer {access_token}'
    }

    params = {
        'territory': 'TW',    # Allowed: HK, JP, MY, SG, TW
        'offset': 0,
        'limit': 30
    }

    response = requests.get(url, headers=headers, params=params)
    result = response.json()["data"]
    for item in result:
        # print(item)
        # print(get_cleaner_name(item['album']['artist']['name']))
        # print(get_cleaner_name(item['name']))
        # print('==============================')
        tracks.append((
            get_cleaner_name(item['album']['artist']['name']),
            get_cleaner_name(item['name'])
        ))

    # return random.choices(tracks, k=N)
    return random.sample(tracks, k=N)


def get_cleaner_name(name):

    cleaner_name = name

    # turn
    # "想見你想見你想見你 (Miss You 3000) - 電視劇<想見你>片尾曲"
    # to
    # "想見你想見你想見你 (Miss You 3000)"
    cleaner_name = cleaner_name.split(' -')[0]

    # turn
    # "想見你想見你想見你 (Miss You 3000)"
    # to
    # "想見你想見你想見你"
    cleaner_name = cleaner_name.split(' (')[0]

    return cleaner_name


# get_chart_playlists(5)
# get_tracks_of_chart_playlist('5Xqy37UtCAvDGWMiO_', 5)


def generate_random_color():
    r = g = b = lambda: random.randint(0, 255)
    return '#%02X%02X%02X' % (r(),g(),b())