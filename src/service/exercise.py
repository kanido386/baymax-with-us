import random

from .basic import send_text_message


all_exercise = []

# 自健運動 - 5分鐘 運動組合
# https://www.youtube.com/playlist?list=PLyCHOqHnsrPfEtiJbKVICR1goTAWjh90M
exercise_5_min = [
    'https://www.youtube.com/watch?v=fcLngKFe6o8',   # J1H1T1
    'https://www.youtube.com/watch?v=gT_l55io6b0',   # J1H1T2
    'https://www.youtube.com/watch?v=uhGEUy7lkW4',   # J1H1T3
    'https://www.youtube.com/watch?v=GGNAJfYq2ug',   # J1H2T1
    'https://www.youtube.com/watch?v=LxjNP4PNS3w',   # J1H2T2
    'https://www.youtube.com/watch?v=4wIXxm68mUc',   # J1H2T3
    # TODO:
]

# 線上體育教學
# https://www.youtube.com/playlist?list=PLhuaGXxIvs0T0S-5TupVqB00bpzwebtW6
online_PE_class = [
    'https://www.youtube.com/watch?v=mVq9ZBnNvWQ',   # 動態熱身操
    'https://www.youtube.com/watch?v=CmL0-T7ryWg',   # 動態動物操(一)
    'https://www.youtube.com/watch?v=FlybGsbv8c0',   # 動態動物操(二)
    # TODO:
]

all_exercise.extend(exercise_5_min)
all_exercise.extend(online_PE_class)


def send_exercise_video(reply_token):
    video_url = random.choice(all_exercise)
    send_text_message(reply_token, video_url)