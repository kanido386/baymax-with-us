import os

from flask import Flask, request, abort
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from machine import create_machine
from service.basic import send_text_message, send_image_message

from dotenv import load_dotenv
load_dotenv()

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

# Unique FSM for each user
machines = {}

app = Flask(__name__, static_url_path="")

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        # if not isinstance(event, MessageEvent):
        #     continue
        # if not isinstance(event.message, TextMessage):
        #     continue
        # if not isinstance(event.message.text, str):
        #     continue

        # TODO:
        reply_token = event.reply_token
        user_id = event.source.user_id
        profile = line_bot_api.get_profile(user_id)
        user_name = profile.display_name
        text = event.postback.data if event.type == 'postback' else event.message.text
        if '剛到' in text:
            send_text_message(reply_token, f'杯麵永遠是{user_name}的好夥伴，有需要隨時呼喚我！')
            continue
        elif '好煩哦' in text:
            send_image_message(reply_token, 'https://www.moedict.tw/%E4%B8%8D%E7%85%A9.png')
            continue
        elif text == '人生':
            send_text_message(reply_token, '雞湯')
            continue

        # Create a machine for new user
        if event.source.user_id not in machines:
            machines[event.source.user_id] = create_machine()
        # Advance the FSM for each MessageEvent
        response = machines[event.source.user_id].advance(event)

        # print(f"\nFSM STATE: {machine.state}")
        # print(f"REQUEST BODY: \n{body}")
        # response = machine.advance(event)

    return "OK"



if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)