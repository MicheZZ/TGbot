
from pytube import YouTube
import asyncio
import aiogram

API_TOKEN = 'Token'

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)

async def download_video(video_url):
    try:
        yt = YouTube(video_url)
        yt.streams.filter(progressive=True, file_extension='mp4').first().download()
        return yt.title
    except:
        return None

@dp.message_handler(commands=['start'])
async def send_welcome(message: aiogram.types.Message):
    await message.reply("Привет! Отправь мне ссылку на видео на YouTube, и я скачаю его для тебя.")

@dp.message_handler()
async def download(message: aiogram.types.Message):
    video_url = message.text
    loop = asyncio.get_event_loop()
    title = await loop.run_in_executor(None, download_video, video_url)
    if title:
        await bot.send_document(message.chat.id, aiogram.types.InputFile(title+'.mp4'))
    else:
        await message.reply("Возникла ошибка при скачивании видео. Попробуйте еще раз.")

if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)
