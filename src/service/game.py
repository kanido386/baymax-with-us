import os
import random
import json

from linebot import LineBotApi
from linebot.models import (
    TextSendMessage, QuickReply, QuickReplyButton, MessageAction, FlexSendMessage
)

access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(access_token)



def send_random_challenge_game(reply_token):
    game = [
        ('見縫插針', 'http://ad.yoercn.com/chazhen/', """
全世界只有8個人玩到了30關！！！
"""),
        ('打地鼠', 'http://g.regogame.com/game/48/', """
請打一下地鼠
打地鼠很有趣
有點上癮。

如果打到40隻，70多歲
打到41-50隻，60多歲
打到51-60隻，50多歲
打到61-70隻，40多歲
打到71-80隻，30多歲
打到81-90隻，20多歲
"""),
        ('賣油翁', 'http://www.wesane.com/game/88/', """
《賣油翁》遊戲太有意思了，你等油壺對準瓢時就點瓢一下。

油進油壺，
得了500分以上證明你離老年痴呆很遠，
得600分以上你仍是中年人，
上了700分你返老還童了！
試試😄
"""),
        ('接蘋果', 'http://www.wesane.com/Public/Games/326029/201707120505335180/html5/index.html', """
接蘋果，防痴呆！

接住 5個，70歲；
接住10個，65歲；
接住15個，60歲；
接住20個，50歲；
接住25個，40歲；
接住26個，35歲；
接住27個，30歲；
接住28個，神仙 !
"""),
        ('吃蘋果', 'http://game.hg0355.com/game/xpg/', """
由最下面往上吃蘋果，
不能跳格，每格都要吃到，
且要練到吃到80個才算及格，
訓練您的反應靈活度、交感神經張力與巴金森病有無問題？
"""),
        ('射蘋果', 'http://game2.baifumeiba.com/minigame/pgdyh/', """
剛剛研發出來的遊戲，這也是老年痴呆症的檢驗標準。

射中2個，80歲，
射中5個，70歲，
射中10個，65歲，
射中15個，60歲，
射中20個，50歲，
射中25個，40歲，
射中26個，35歲，
射中27個，30歲，

射中28個是不可能的。
(其實都很難 玩一玩)

不要急！射看看就知道了！
"""),
        ('國學嘗試 卷一', 'http://www.moosasa.com.tw/ChineseTry/tw1/index.htm', """
沒事都在傳Line，國字都快不會寫了！

考考自己的國語文，
全部150題、答對100題算書沒白讀。
"""),
        ('國學嘗試 卷二', 'http://www.moosasa.com.tw/ChineseTry/tw2/index.htm', """
沒事都在傳Line，國字都快不會寫了！

考考自己的國語文，
全部150題、答對100題算書沒白讀。
"""),
        ('國學嘗試 卷三', 'http://www.moosasa.com.tw/ChineseTry/tw3/index.htm', """
沒事都在傳Line，國字都快不會寫了！

考考自己的國語文，
全部150題、答對100題算書沒白讀。
"""),
    ]

    the_game = random.choice(game)

    flex_message_json_string = """
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": \"""" + the_game[0] + """\",
        "align": "center",
        "size": "20px",
        "weight": "bold"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "wrap": true,
        "text": \"""" + the_game[2].replace('\n', '\\n') + """\"
      }
    ]
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "開始挑戰！",
          "uri": \"""" + the_game[1] + """\"
        }
      }
    ]
  }
}
"""
    flex_message_json_dict = json.loads(flex_message_json_string)
    message = FlexSendMessage(
        alt_text=f"【{the_game[0]}】挑戰一波！",
        contents=flex_message_json_dict
    )

    line_bot_api.reply_message(reply_token, message)



def send_random_leisure_game(reply_token):
    game = [
        ('恭喜發財', 'http://g.regogame.com/game/199/'),
        ('母雞下蛋', 'http://www.wesane.com/game/705/'),
        ('鬥牛', 'http://www.wesane.com/game/369/'),
        ('投籃', 'http://game2.baifumeiba.com/minigame/tq/'),
        ('見縫插針', 'http://play.ziyuantun.com/jfcz/'),
        ('錦上添花', 'http://g.regogame.com/game/3/'),
        ('見縫插車', 'http://www.wesane.com/game/295/'),
        ('堆木頭', 'http://play.ziyuantun.com/duimutou/'),
        ('刮腿毛', 'http://www.wesane.com/game/264/'),
        ('打掉磚塊', 'http://game3.baifumeiba.com/ddzk/'),
        ('旋轉吧大寶劍', 'http://game3.baifumeiba.com/dbj/'),
        ('十滴水', 'http://game3.baifumeiba.com/minigame/sds/'),
    ]

    # TODO:
    # 友誼的小船說翻就翻 http://t.cn/RcAKw8F
    # 無盡之湖 http://t.cn/A6PLFX50
    # 蛇與方塊 http://t.cn/Ev96Ras
    # 有多遠滾多遠 http://t.cn/AisiB48U
    # 羽毛球 http://t.cn/A6Pyti4P
    # 彩虹屁 http://t.cn/A6Py5a3Q
    # 烏鴉喝水 http://t.cn/RUMpO5R
    # 擦一擦 http://t.cn/A6PyZq50
    # 翻轉水瓶 http://t.cn/A6PyZq5o
    # 磁鐵粘粘 http://t.cn/A6PyqtYy
    # 旋轉飛刀 http://t.cn/A6PyLrCb
    # 守護蛋蛋 http://t.cn/A6PyZq5a
    # 無敵破壞球 http://t.cn/A6PyZq5K
    # 打泡泡 http://t.cn/A6Pq1Hoj
    # 紙牌接龍 http://t.cn/AiuR04G8
    # 六角拼拼 http://t.cn/Rtp4QDz
    # 俄羅斯方塊 http://t.cn/RcciqaX
    # 捕鳥 http://t.cn/RagxdQ0
    # 彈彈球 http://t.cn/RVbx3Dz
    # 切水果 http://t.cn/A6PGSCKb
    # 汽車華容道 http://t.cn/Ea80aIc
    # 搭橋 http://t.cn/A6P5PvvX

    the_game = random.choice(game)

    flex_message_json_string = """
{
  "type": "bubble",
  "header": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "text",
        "text": \"""" + the_game[0] + """\",
        "align": "center",
        "size": "20px",
        "weight": "bold"
      }
    ]
  },
  "body": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "image",
        "size": "80px",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Video-Game-Controller-Icon-IDV-green.svg/2048px-Video-Game-Controller-Icon-IDV-green.svg.png"
      }
    ],
    "paddingAll": "0px"
  },
  "footer": {
    "type": "box",
    "layout": "vertical",
    "contents": [
      {
        "type": "button",
        "action": {
          "type": "uri",
          "label": "開始玩！",
          "uri": \"""" + the_game[1] + """\"
        }
      }
    ]
  }
}
"""
    flex_message_json_dict = json.loads(flex_message_json_string)
    message = FlexSendMessage(
        alt_text=f"【{the_game[0]}】玩起來！",
        contents=flex_message_json_dict
    )

    line_bot_api.reply_message(reply_token, message)





def send_game_options(reply_token):

    message = TextSendMessage(
        text='想當消遣還是挑戰呢？',
        quick_reply=QuickReply(
            items=[
                QuickReplyButton(
                    action=MessageAction(
                        label='消遣遊戲',
                        text='消遣遊戲'
                    )
                ),
                QuickReplyButton(
                    action=MessageAction(
                        label='挑戰遊戲',
                        text='挑戰遊戲'
                    )
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)