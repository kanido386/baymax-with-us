import os

from linebot import LineBotApi
from linebot.models import (
    TextSendMessage, TemplateSendMessage, MessageTemplateAction, CarouselTemplate,
    CarouselColumn
)

from googleapiclient.discovery import build

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)



def send_text_message(reply_token, text):
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


# TODO: 好像太過度包裝了，不太需要的感覺
# def send_template_message(reply_token, setting):

#     setting = {
#         'alt_text': 'Carousel template',
#         'num_col': 3,
#         'carousel_columns': [
#             {
#                 'thumbnail_image_url': Videos[0]['snippet']['thumbnails']['high']['url'],
#                 'title': 'This one?',
#                 'text': Videos[0]['snippet']['title'][:60],
#                 'num_action': 1,
#                 'actions': [

#                 ]
#             }
#         ]
#     }

#     alt_text = setting['alt_text']
#     num_col = setting['num_col']
#     carousel_columns = setting['carousel_columns']

#     columns = []
#     for i in range(num_col):
#         columns.append(
#             CarouselColumn(
#                 thumbnail_image_url=carousel_columns[i]['thumbnail_image_url'],
#                 title=carousel_columns[i]['title'],
#                 text=carousel_columns[i]['text'],
#                 actions=[
#                     MessageTemplateAction(
#                         label='Listen to this',
#                         text=videoUrls[0]
#                     )
#                 ]
#             )
#         )

#     message = TemplateSendMessage(
#         alt_text=alt_text,
#         template=CarouselTemplate(
#             columns=[
#                 CarouselColumn(
#                     thumbnail_image_url=Videos[0]['snippet']['thumbnails']['high']['url'],
#                     title='This one?',
#                     text=Videos[0]['snippet']['title'][:60],
#                     actions=[
#                         MessageTemplateAction(
#                             label='Listen to this',
#                             text=videoUrls[0]
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url=Videos[1]['snippet']['thumbnails']['high']['url'],
#                     title='This one?',
#                     text=Videos[1]['snippet']['title'][:60],
#                     actions=[
#                         MessageTemplateAction(
#                             label='Listen to this',
#                             text=videoUrls[1]
#                         )
#                     ]
#                 ),
#                 CarouselColumn(
#                     thumbnail_image_url=Videos[2]['snippet']['thumbnails']['high']['url'],
#                     title='Or this one?',
#                     text=Videos[2]['snippet']['title'][:60],
#                     actions=[
#                         MessageTemplateAction(
#                             label='Listen to this',
#                             text=videoUrls[2]
#                         )
#                     ]
#                 )
#             ]
#         )
#     )



def send_youtube_video(reply_token, query):
    youTubeApiKey = os.getenv("YOUTUBE_API_KEY", None)
    youtube = build('youtube', 'v3', developerKey=youTubeApiKey)
    query = query[2:]
    request = youtube.search().list(part='snippet', q=query, type='video')
    response = request.execute()
    Videos = response['items'][0:3]
    videoIds = [Videos[i]['id']['videoId'] for i in range(3)]
    videoUrls = [f'https://www.youtube.com/watch?v={videoId}' for videoId in videoIds]

    message = TemplateSendMessage(
        alt_text='選歌聽吧！',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url=Videos[0]['snippet']['thumbnails']['high']['url'],
                    title='是這首？',
                    text=Videos[0]['snippet']['title'][:60],
                    actions=[
                        MessageTemplateAction(
                            label='聽這首！',
                            text=videoUrls[0]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=Videos[1]['snippet']['thumbnails']['high']['url'],
                    title='這首？',
                    text=Videos[1]['snippet']['title'][:60],
                    actions=[
                        MessageTemplateAction(
                            label='聽這首！',
                            text=videoUrls[1]
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url=Videos[2]['snippet']['thumbnails']['high']['url'],
                    title='還是這首呢？',
                    text=Videos[2]['snippet']['title'][:60],
                    actions=[
                        MessageTemplateAction(
                            label='聽這首！',
                            text=videoUrls[2]
                        )
                    ]
                )
            ]
        )
    )

    line_bot_api.reply_message(reply_token, message)

    return "OK"