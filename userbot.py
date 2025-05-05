# from pyrogram import Client
# from pyrogram.handlers import MessageHandler
# from pyrogram.types import Message
# from pytube import YouTube
# import uvloop
# import cv2
# import shutil
#
# api_id = 23438534
# api_hash = "33037adc088e7f10dc9a726bd7ef0a14"
# uvloop.install()
# client = Client(name="me_client", api_id=api_id, api_hash=api_hash)
#
#
#
#
# async def all_message(client: Client, message: Message):
#     if (message.text.startswith == "https://youtu.be" or "https://youtube.com") and (message.text != "/yt"):
#         url = message.text
#         yt = YouTube(url)
#         stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
#         stream.download(f"{message.chat.id}", f"{message.chat.id}_{yt.title}")
#         video = cv2.VideoCapture(f"{message.chat.id}/{message.chat.id}_{yt.title}")
#         height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
#         await client.send_video("end_project_bot", video=f"{message.chat.id}/{message.chat.id}_{yt.title}", width=width, height=height)
#         shutil.rmtree(f"{message.chat.id}")
#
#
#
#
#
# client.add_handler(MessageHandler(all_message))
#
#
#
#
#
# client.run()
#
#
#

from pytube import YouTube

url = 'https://www.youtube.com/watch?v=90KZnwrVMgY'

yt = YouTube(url)
print(f'Download video {yt.title!r}: {url}')

streams = yt.streams\
    .filter(progressive=True, file_extension='mp4', resolution='720p')\
    .order_by('resolution')

video = streams[-1]
print('Stream url:', video.url)
video.download()
