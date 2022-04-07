from cgitb import text
from email import message
from email.message import Message
from operator import truediv
from random import randint
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

from token_b import TOKEN, URL_NASA

bool_ban = False

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

str = ['дурак', 'придурак', 'придурок', 'идиот', 'имбецил', 'дебил', 'пидорас', 'пидарас', 'пидорас', 'уебок', 'уёбок', 'долбаеб', 'долбаёб', 'сука', 'пидор', 'пидар']

str2 = "аахахахахахахахахахахахахахахахахахахахахахаххахахахахахаахахаххахахахахах аазаззазазазазазазаззазазазазазаззазазазазазазазазазазазаза очень смешно"

def getarrayimage(image):
    array1 = []
    for g in image['collection']['items']:
        array2 = []
        for h in g['data']:
            array2.append(h['description'])
        for h in g['links']:
            array2.append(h['href'])
        array1.append(array2)
    return array1    


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Ам. Старт. Напиши что нибудь")

@dp.message_handler(commands=['nasa'])
async def process_nasa_command(message: types.Message):
    imgrequaest = requests.get(URL_NASA)
    image1 = imgrequaest.json()
    array1 = getarrayimage(image1)
    asd = randint(0, len(array1) - 1)
    await bot.send_photo(message.chat.id ,array1[asd][1])
    await message.answer(array1[asd][0])

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Я отправлю тебе что нибудь то, что ты отправишь мне")


@dp.message_handler(content_types= ['text'])
async def echo_message(message: types.Message):
    global bool_ban
    if  message.text.lower() in str:
        await message.answer_sticker("CAACAgIAAxkBAAEESf5iQHvr6uZr7tob2XovC94usQJBJwAC2hUAAnahuEj3MaUDBmdYjCME")
    elif str2.find(message.text) != -1:
        await message.answer_sticker("CAACAgIAAxkBAAEEShliQIsLjwZuHFbiiOnlH3BsnYAjFQACxREAAgy9GUiVsT3tEALHciME")
    elif message.text.find("Привет!") != -1:
        await message.answer("Привет!")
        await message.answer("Спишь?")
        await message.answer("Это Дима")
        await message.answer("Ты в баню завтра идёшь?")
        bool_ban = True
    elif message.text == 'да' and bool_ban:
        await message.answer_sticker("CAACAgIAAxkBAAEESmdiQIznSkbTtU51OryOihRQyayDDwACJg4AAvW6EEiEWDQIzqqeEyME")
    elif message.text.lower().find('огонь!') != -1:
        await message.answer('🔥')
    elif message.text == 'лох':
        await message.answer_sticker("CAACAgIAAxkBAAEES-NiQXo_EKGMoGEFVFIdrDd4t_u3ggAC8RMAApRcuEiuigABLEjlMfYjBA")
    else:
        await bot.send_message(message.from_user.id, message.text)
        #await bot.send_sticker(message.from_user.id, message.sticker.file_id)
        bool_ban = False

@dp.message_handler(content_types=['sticker'])
async def echo_sticker(strik: types.Message):
    await bot.send_sticker(strik.from_user.id, strik.sticker.file_id)

if __name__ == '__main__':
    executor.start_polling(dp)

#постить фотку с насо
