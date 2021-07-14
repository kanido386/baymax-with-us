from transitions.extensions import GraphMachine
# from utils import send_text_message, send_youtube_video
from service.basic import send_text_message
from service.youtube import send_youtube_video
from service.kkbox import send_random_playlists, send_random_tracks
from service.exercise import send_exercise_video
from service.fact_checking import send_fact_checking
from service.game import send_game_options, send_random_leisure_game, send_random_challenge_game
from service.weather import send_weather
from service.email import send_email_to_kanido
from service.feature import send_feature

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_youtube(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text[:2] == "聽 "   # 聽 王藍茵 惡作劇

    def is_going_to_kkbox(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "隨機聽"   # 隨機聽

    def is_going_to_kkbox_playlist(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        # (quick reply) postback: playlist <playlist_id>
        return event.type == 'postback' and text[:9] == "playlist "

    def is_going_to_exercise(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "做運動"   # 做運動

    def is_going_to_fact_checking(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text[:3] == "查證 "   # 查證 <可疑訊息>

    def is_going_to_game_options(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "玩遊戲"   # 玩遊戲

    def is_going_to_game_leisure(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "消遣遊戲"   # 消遣遊戲

    def is_going_to_game_challenge(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "挑戰遊戲"   # 挑戰遊戲

    def is_going_to_weather(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text[-3:] == " 天氣"   # 新莊 天氣

    def is_going_to_feature_request(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text[:4] == "新功能 " and text.count(' ') >= 2   # 新功能 <name> <description>

    def is_going_to_feature_show(self, event):
        # text = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        return text == "功能"   # 功能

    # def is_going_to_state1(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state1"

    # def is_going_to_state2(self, event):
    #     text = event.message.text
    #     return text.lower() == "go to state2"

    # ==============================

    def on_enter_youtube(self, event):
        print("I'm entering youtube")

        reply_token = event.reply_token
        # query = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        query = text[2:]
        try:
            send_youtube_video(reply_token, query)
        except:
            send_text_message(reply_token, '用完每日額度了\U0001f62d')
        self.go_back()


    def on_enter_kkbox(self, event):
        print("I'm entering kkbox")

        reply_token = event.reply_token
        send_random_playlists(reply_token, 5)
        self.go_back()


    def on_enter_kkbox_playlist(self, event):
        print("I'm entering kkbox_playlist")

        reply_token = event.reply_token
        text = event.postback.data if event.type == 'postback' else event.message.text
        playlist_id = text[9:]
        send_random_tracks(reply_token, playlist_id, 5)
        # send_text_message(reply_token, text)
        self.go_back()


    def on_enter_exercise(self, event):
        print("I'm entering exercise")

        reply_token = event.reply_token
        # text = event.postback.data if event.type == 'postback' else event.message.text
        send_exercise_video(reply_token)
        self.go_back()


    def on_enter_fact_checking(self, event):
        print("I'm entering fact_checking")

        reply_token = event.reply_token
        # query = event.message.text
        text = event.postback.data if event.type == 'postback' else event.message.text
        query = text
        # query = text[3:]
        send_fact_checking(reply_token, query)
        self.go_back()


    def on_enter_game_options(self, event):
        print("I'm entering game_options")

        reply_token = event.reply_token
        send_game_options(reply_token)
        self.go_back()


    def on_enter_game_leisure(self, event):
        print("I'm entering game_leisure")

        reply_token = event.reply_token
        send_random_leisure_game(reply_token)
        self.go_back()


    def on_enter_game_challenge(self, event):
        print("I'm entering game_challenge")

        reply_token = event.reply_token
        send_random_challenge_game(reply_token)
        self.go_back()


    def on_enter_weather(self, event):
        print("I'm entering weather")

        reply_token = event.reply_token
        text = event.postback.data if event.type == 'postback' else event.message.text
        query = text
        send_weather(reply_token, query)
        self.go_back()


    def on_enter_feature_request(self, event):
        print("I'm entering feature_request")

        reply_token = event.reply_token
        text = event.postback.data if event.type == 'postback' else event.message.text
        feature_name = text.split(' ')[1]
        description = ' '.join(text.split(' ')[2:])
        send_email_to_kanido(reply_token, feature_name, description)
        self.go_back()


    def on_enter_feature_show(self, event):
        print("I'm entering feature_show")

        reply_token = event.reply_token
        send_feature(reply_token)
        self.go_back()

    # def on_enter_state1(self, event):
    #     print("I'm entering state1")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state1")
    #     self.go_back()

    # def on_exit_state1(self):
    #     print("Leaving state1")

    # def on_enter_state2(self, event):
    #     print("I'm entering state2")

    #     reply_token = event.reply_token
    #     send_text_message(reply_token, "Trigger state2")
    #     self.go_back()

    # def on_exit_state2(self):
    #     print("Leaving state2")