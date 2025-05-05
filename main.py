###############################################################################################
BOT_TOKEN = "Token"
PAYMENTS_TOKEN = "P_Token"

from random import randint
import sqlite3
import os

import logging
from aiogram.types.message import ContentType
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text, Command
from aiogram.types import Message, ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton

import os

from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()


logging.basicConfig(level=logging.INFO)

bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())



def bj_gamer():
    global pik
    global cross
    global bub
    global cher
    global soc
    global count_gamer
    x = randint(0, 3)
    if x == 0:
        mast = "пик"
    elif x == 1:
        mast = "треф"
    elif x == 2:
        mast = "бубн"
    elif x == 3:
        mast = "черв"
    index = randint(0, len(soc[x]) - 1)
    current = soc[x].pop(index)
    count_gamer += int(current)
    if 2 <= current <= 10:
        current = str(current)
    elif current == 10.1:
        current = 'валет'
    elif current == 10.2:
        current = 'дама'
    elif current == 10.3:
        current = 'король'
    elif current == 11:
        current = 'туз'
    return [current, mast, count_gamer]



def bj_dealer():
    global pik
    global cross
    global bub
    global cher
    global soc
    global count_dealer
    x = randint(0, 3)
    if x == 0:
        mast = "пик"
    elif x == 1:
        mast = "треф"
    elif x == 2:
        mast = "бубн"
    elif x == 3:
        mast = "черв"
    index = randint(0, len(soc[x]) - 1)
    current = soc[x].pop(index)
    count_dealer += int(current)
    if 2 <= current <= 10:
        current = str(current)
    elif current == 10.1:
        current = 'валет'
    elif current == 10.2:
        current = 'дама'
    elif current == 10.3:
        current = 'король'
    elif current == 11:
        current = 'туз'
    return [current, mast, count_dealer]
###############################################################################################
















###############################################################################################
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Баланс")
        ],
        [
            KeyboardButton(text="Игры"),
            KeyboardButton(text="Остальное")
        ]
    ],
    resize_keyboard = True
)

keyboard_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад в меню")
        ]
    ],
    resize_keyboard=True
)



keyboard_games = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="BlackJack"),
            KeyboardButton(text="Угадайка"),
        ],
        [
            KeyboardButton(text="Назад в меню")
        ]
    ],
    resize_keyboard = True
)

keyboard_other = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Предсказание судьбы"),
        ],
        [
            KeyboardButton(text="Перевод SofN"),
            KeyboardButton(text="Генератор пароля"),
        ],
        [
            KeyboardButton(text="Назад в меню")
        ]
    ],
    resize_keyboard = True
)

keyboard_generator = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ],
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в остальное")
        ]
    ],
    resize_keyboard = True
)

keyboard_back_2_other = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в остальное")
        ]
    ],
    resize_keyboard = True
)

keyboard_fate = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="50")
        ],
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в остальное")
        ]
    ],
    resize_keyboard = True
)

keyboard_laky = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1"),
            KeyboardButton(text="2"),
            KeyboardButton(text="3"),
        ],
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в игры")
        ]
    ],
    resize_keyboard = True
)

keyboard_back_games = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в игры")
        ]
    ],
    resize_keyboard = True
)


keyboard_bj = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Хватит"),
            KeyboardButton(text="Ещё")
        ],
        [
            KeyboardButton(text="Назад в меню"),
            KeyboardButton(text="Назад в игры")
        ]
    ],
    resize_keyboard = True
)


keyboard_video = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="YouTube")
        ],
        [
            KeyboardButton(text="Назад в меню")
        ]
    ],
    resize_keyboard = True
)
###############################################################################################

















###############################################################################################
"""*****************************************************************************************"""
@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Menu:\nУзнать состояние баланса\nПоиграть в игры\nВоспользоваться другими сервисами\n(Чтобы быстро вернуться в Menu, напиши команду /menu)", reply_markup=keyboard)

"""*****************************************************************************************"""





"""*****************************************************************************************"""
@dp.message_handler(Command("menu"))
@dp.message_handler(Text(equals=["Назад в меню"]))
async def move(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Menu:\nУзнать состояние баланса\nПоиграть в игры\nВоспользоваться другими сервисами\n(Чтобы быстро вернуться в Menu, напиши команду /menu)", reply_markup=keyboard)

"""*****************************************************************************************"""




"""*****************************************************************************************"""
@dp.message_handler(Text(equals=["Назад в остальное"]))
async def move(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Остальное:\nПредсказание судьбы\nПеревод из одной систимы счисления в другую\nГенератор пароля\n(Чтобы быстро вернуться в Остальное, напиши команду /other)", reply_markup=keyboard_other)

"""*****************************************************************************************"""






"""*****************************************************************************************"""
@dp.message_handler(Text(equals=["Баланс"]))
@dp.message_handler(Command("count"))
async def show_menu(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    user_id = message.chat.id
    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
    connect.commit()
    await message.answer("Состояние баланса: %s\n(Чтобы быстро узнать состояния баланса, напиши команду /count)" %count, reply_markup=keyboard_back)

"""*****************************************************************************************"""





"""*****************************************************************************************"""
@dp.message_handler(Text(equals=["Остальное"]))
@dp.message_handler(Command("other"))
async def show_menu(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Остальное:\nПредсказание судьбы\nПеревод из одной систимы счисления в другую\nГенератор пароля\n(Чтобы быстро вернуться в Остальное, напиши команду /other)", reply_markup=keyboard_other)

"""*****************************************************************************************"""




"""*****************************************************************************************"""
@dp.message_handler(Text(equals=["Скачать видео"]))
@dp.message_handler(Command("video"))
async def show_menu(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Скачать видео:\nВыбери платформу с какой ты будешь скачивать\nYouTube\nTikTok\n(Чтобы быстро вернуться в Остальное, напиши команду /video)", reply_markup=keyboard_video)

"""*****************************************************************************************"""





"""*****************************************************************************************"""
@dp.message_handler(Text(equals=["Игры"]))
@dp.message_handler(Command("games"))
async def show_menu(message: Message):
    global cursor
    global connect
    connect = sqlite3.connect('count.db')
    cursor = connect.cursor()
    try:
        data = cursor.fetchone()
        if data is None:
            cursor.execute('CREATE TABLE IF NOT EXISTS {}(id INTEGER PRIMARY KEY, count_id INTEGER)'.format('data'))
            connect.commit()

            user_id = message.chat.id
            cursor.execute("INSERT INTO data VALUES(?, ?)", (user_id, 0))
            connect.commit()
    except sqlite3.Error as error:
        print("Error", error)
    await message.answer("Игры:\nBlackJack\nУгадайка\n(Чтобы быстро вернуться в Игры, напиши команду /games)", reply_markup=keyboard_games)

"""*****************************************************************************************"""








"""*****************************************************************************************"""
# Выход из состояний
@dp.message_handler(state="*", commands='Назад в меню')
@dp.message_handler(Text(equals='Назад в меню', ignore_case=True), state="*")
async def cancel_menu(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Menu:\nУзнать состояние баланса\nПоиграть в игры\nВоспользоваться другими сервисами\n(Чтобы быстро вернуться в Menu, напиши команду /menu)", reply_markup=keyboard)

@dp.message_handler(state="*", commands='Назад в остальное')
@dp.message_handler(Text(equals='Назад в остальное', ignore_case=True), state="*")
async def cancel_other(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Остальное:\nПредсказание судьбы\nПеревод из одной систимы счисления в другую\nГенератор пароля\n(Чтобы быстро вернуться в Остальное, напиши команду /other)", reply_markup=keyboard_other)


@dp.message_handler(state="*", commands='Назад в игры')
@dp.message_handler(Text(equals='Назад в игры', ignore_case=True), state="*")
async def cancel_other(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.answer("Игры:\nBlackJack\nУгадайка\n(Чтобы быстро вернуться в Игры, напиши команду /games)", reply_markup=keyboard_games)

"""*****************************************************************************************"""
###############################################################################################

























































###############################################################################################
class FSMfate(StatesGroup):
    ask = State()
    ver = State()

@dp.message_handler(Text(equals=["Предсказание судьбы"]), state=None)
@dp.message_handler(commands=["fate"], state=None)
async def fate_start(message: types.Message):
    await FSMfate.ask.set()
    await message.answer("Задай вопрос\nНе забудь про '?' в конце\n(Чтобы быстро перейти в эту вкладку используй /fate)", reply_markup=keyboard_back_2_other)

@dp.message_handler(content_types=['text'], state=FSMfate.ask)
async def fate_mid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text[-1] == '?':
            if len(message.text) >= 6:
                data['ask'] = message.text
                await FSMfate.next()
                await message.answer("На сколько процентов уверен в этом?\nВведи число от 1 до 99, где 1 не уверен, а 99 полностью уверен\nВведи '50', чтобы уравнять вероятность", reply_markup=keyboard_fate)
            else:
                await message.answer("Вопрос должен состоять минимум из 6 символов")
        else:
            await message.answer("Вопрос должен содержать '?' в конце...")

@dp.message_handler(content_types=['text'], state=FSMfate.ver)
async def fate_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect
        positive = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да", "Можешь быть уверен в этом", "Да"]
        indecpositive = ["Мне кажется - да", "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да, но можно перепроверить"]
        neutral = ["Скорее нет, чем да", "Я был бы против", "Ммм, нет?", "Думаю не стоит", "Вероятнее нет"]
        negative = ["Даже не думай", "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
        try:
            if 1 <= int(message.text) <= 99:
                data['ver'] = int(message.text)
                a = data['ver'] * 5
                b = 500 - a
                c = a / 5
                a = a - c
                d = b / 5
                b = b - d
                mass = []
                for _ in range(int(a)):
                    mass.append(0)
                for _ in range(int(b)):
                    mass.append(1)
                for _ in range(int(c)):
                    mass.append(2)
                for _ in range(int(d)):
                    mass.append(3)
                l = randint(0, len(mass) - 1)
                k = mass[l]
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) + 5
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", ( count, user_id))
                connect.commit()
                if k == 0:
                    await message.answer(positive[randint(0, len(positive) - 1)], reply_markup=keyboard_other)
                if k == 1:
                    await message.answer(indecpositive[randint(0, len(indecpositive) - 1)], reply_markup=keyboard_other)
                if k == 2:
                    await message.answer(neutral[randint(0, len(neutral) - 1)], reply_markup=keyboard_other)
                if k == 3:
                    await message.answer(negative[randint(0, len(negative) - 1)], reply_markup=keyboard_other)

                await state.finish()

            else:
                await message.answer("Введи число от 1 до 99...")
        except ValueError:
            await message.answer("Для чего тут буквы?\nВведи число от 1 до 99")
###############################################################################################






















###############################################################################################
class FSMgen(StatesGroup):
    k = State()
    status = State()

@dp.message_handler(Text(equals=["Генератор пароля"]), state=None)
@dp.message_handler(commands=["gen"], state=None)
async def gen_start(message: types.Message):
    await FSMgen.k.set()
    await message.answer("Введи длину пароля\nВведи число от 6 до 32\n(Чтобы быстро перейти в эту вкладку используй /gen)", reply_markup=keyboard_back_2_other)

@dp.message_handler(content_types=['text'], state=FSMgen.k)
async def gen_mid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            if 6 <= int(message.text) <= 32:
                data['k'] = int(message.text)
                await FSMgen.next()
                await message.answer("Нужно использовать спец символы?\nТакие: ! @ # $ % ^ & ? * _ = +\nНапиши 'Да' или 'Нет'", reply_markup=keyboard_generator)
            else:
                if int(message.text) < 6:
                    await message.answer("Не думаю, что это надежно\nДа и нигде вроде неьзя поставить таком маленький пароль\nВведи число от 6 до 32")
                else:
                    await message.answer("Слишком надёжный\nНадеюсь не для одноклассников?\nВведи число от 6 до 32")
        except ValueError:
            await message.answer("Для чего тут буквы?\nВведи число от 6 до 32")

@dp.message_handler(content_types=['text'], state=FSMgen.status)
async def gen_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect
        if message.text.lower() == "да" or message.text.lower() == "нет":
            data['status'] = message.text

            app = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]
            bad = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
            cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            den = ["!", "@", "#", "$", "%", "^", "&", "?", "*", "_", "=", "+"]

            guf = [app, bad, cap, den]
            fuck = [app, bad, cap]

            password = ""
            if data['status'].lower() == 'да':
                for _ in range(data['k']):
                    k = randint(0, 3)
                    i = len(guf[k]) - 1
                    j = randint(0, i)
                    password += guf[k][j]
            elif data['status'].lower() == 'нет':
                for _ in range(data['k']):
                    k = randint(0, 2)
                    i = len(fuck[k]) - 1
                    j = randint(0, i)
                    password += fuck[k][j]
            user_id = message.chat.id
            count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
            count = int(count[0]) + 5
            cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
            connect.commit()
            await message.answer(password, reply_markup=keyboard_other)

            await state.finish()
        else:
            await message.answer("Просто напиши 'Да' или 'Нет', ничего сложного")
###############################################################################################























###############################################################################################
class FSMtss(StatesGroup):
    num = State()
    basein = State()
    baseout = State()

@dp.message_handler(Text(equals=["Перевод SofN"]), state=None)
@dp.message_handler(commands=["tsofn"], state=None)
async def tss_start(message: types.Message):
    await FSMtss.num.set()
    await message.answer("Какое число перевести\n(Чтобы быстро перейти в эту вкладку используй /tsofn)", reply_markup=keyboard_back_2_other)

@dp.message_handler(content_types=['text'], state=FSMtss.num)
async def tss_mid_1(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count_tss_alp = 0
        for i in range(len(message.text)):
            if message.text[i].upper() in alpha:
                count_tss_alp += 1
        if count_tss_alp == len(message.text):
            data['num'] = message.text.upper()
            await FSMtss.next()
            await message.answer("Из какой системы переводить?")
        else:
            await message.answer("Число должно состоять из цифр и латинских букв")

@dp.message_handler(content_types=['text'], state=FSMtss.basein)
async def tss_mid_2(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            if 2 <= int(message.text) <= 36:
                alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                max_index_tss = 2
                for i in range(len(data['num'])):
                    if alpha.find(data['num'][i]) > max_index_tss:
                        max_index_tss = alpha.find(data['num'][i]) + 1
                if max_index_tss > int(message.text):
                    await message.answer("Ну вообще-то тут минимальное основание %d, но я исправил ТВОЮ ошибку" %(max_index_tss))
                    data['basein'] = max_index_tss
                else:
                    data['basein'] = int(message.text)
                await FSMtss.next()
                await message.answer("В какую систему перевести?")
            else:
                await message.answer("Введи число от 2 до 36\nТолько такие основания существуют...")
        except ValueError:
            await message.answer("Для чего тут буквы?\nВведи число от 2 до 36")

@dp.message_handler(content_types=['text'], state=FSMtss.baseout)
async def tss_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect
        try:
            if 2 <= int(message.text) <= 36:
                data['baseout'] = int(message.text)

                def toBASE(num, base):
                    alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                    b = alpha[num % base]
                    while num >= base:
                        num = num // base
                        b += alpha[num % base]
                    return b[::-1]
                a = int(data['num'], data['basein'])
                a = toBASE(a, data['baseout'])
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) + 5
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await message.answer(a, reply_markup=keyboard_other)

                await state.finish()
            else:
                await message.answer("Введи число от 2 до 36\nТолько такие основания существуют...")
        except ValueError:
            await message.answer("Для чего тут буквы?\nВведи число от 2 до 36")
###############################################################################################

























###############################################################################################
class FSMlaky(StatesGroup):
    level = State()
    game = State()
@dp.message_handler(Text(equals=["Угадайка"]), state=None)
@dp.message_handler(commands=["laky"], state=None)
async def laky_start(message: types.Message):
    await FSMlaky.level.set()
    await message.answer("Выбери уровень 1,2 или 3\n(Чтобы быстро перейти в эту вкладку используй /laky)", reply_markup=keyboard_laky)

@dp.message_handler(content_types=['text'], state=FSMlaky.level)
async def laky_mid(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == "1" or message.text == "2" or message.text == "3":
            data['level'] = message.text
            data['count_attempst'] = "0"
            if message.text == "1":
                await message.answer("Твоя задача угадать число от 1 до 100 за 6 попыток\nЕсли ты используешь больше, то выигрыш будет уменьшаться на 10 процентов\nВведи число в промежутке от 1 до 100", reply_markup=keyboard_back_games)
                data['rand'] = randint(1, 100)
                await FSMlaky.next()
            elif message.text == "2":
                await message.answer("Твоя задача угадать число от 1 до 500 за 8 попыток\nЕсли ты используешь больше, то выигрыш будет уменьшаться на 10 процентов\nВведи число в промежутке от 1 до 500", reply_markup=keyboard_back_games)
                data['rand'] = randint(1, 500)
                await FSMlaky.next()
            elif message.text == "3":
                await message.answer("Твоя задача угадать число от 1 до 1000 за 9 попыток\nЕсли ты используешь больше, то выигрыш будет уменьшаться на 10 процентов\nВведи число в промежутке от 1 до 1000", reply_markup=keyboard_back_games)
                data['rand'] = randint(1, 1000)
                await FSMlaky.next()
        else:
            await message.answer("Выбери уровень 1, 2 или 3")

@dp.message_handler(content_types=['text'], state=FSMlaky.game)
async def laky_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect
        try:
            if data['level'] == "1":
                if int(message.text) == data['rand']:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    user_id = message.chat.id
                    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                    if int(data['count_attempst']) <= 6:
                        priz = 100
                        count = int(count[0]) + 100
                    else:
                        priz = int(100 * (0.9**(int(data['count_attempst'])-6)))
                        count = int(count[0]) + priz
                    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                    connect.commit()
                    await message.answer(f"Ты угадал!!! Твой выигрыш равен {priz}", reply_markup=keyboard_games)
                    await state.finish()
                elif int(message.text) < 1:
                    await message.answer("Как-то мало. Минимальное число 1")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    print(data['count_attempst'])
                elif int(message.text) > 100:
                    await message.answer("Как-то много. Максимальное число 100")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    print(data['count_attempst'])
                elif int(message.text) < data['rand']:
                    await message.answer("Мало. Попробуй ввести число побольше")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    print(data['count_attempst'])
                elif int(message.text) > data['rand']:
                    await message.answer("Много. Попробуй ввести число поменьше")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    print(data['count_attempst'])

            elif data['level'] == "2":
                if int(message.text) == data['rand']:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    user_id = message.chat.id
                    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                    if int(data['count_attempst']) <= 8:
                        count = int(count[0]) + 500
                        priz = 500
                    else:
                        priz = int(500 * (0.9**(int(data['count_attempst'])-8)))
                        count = int(count[0]) + priz
                    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                    connect.commit()

                    await message.answer(f"Ты угадал!!! Твой выигрыш равен {priz}", reply_markup=keyboard_games)
                    await state.finish()
                elif int(message.text) < 1:
                    await message.answer("Как-то мало. Минимальное число 1")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                elif int(message.text) > 500:
                    await message.answer("Как-то много. Максимальное число 500")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                elif int(message.text) < data['rand']:
                    await message.answer("Мало. Попробуй ввести число побольше")
                    data['count_attempst'] = int(data['count_attempst']) + 1
                elif int(message.text) > data['rand']:
                    await message.answer("Много. Попробуй ввести число поменьше")
                    data['count_attempst'] = int(data['count_attempst']) + 1

            elif data['level'] == "3":
                if int(message.text) == data['rand']:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    user_id = message.chat.id
                    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()

                    if int(data['count_attempst']) <= 9:
                        count = int(count[0]) + 1000
                        priz = 1000
                    else:
                        priz = int(1000 * (0.9 ** (int(data['count_attempst']) - 9)))
                        count = int(count[0]) + priz

                    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                    connect.commit()

                    await message.answer(f"Ты угадал!!! Твой выигрыш равен {priz}", reply_markup=keyboard_games)
                    await state.finish()
                elif int(message.text) < 1:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    await message.answer("Как-то мало. Минимальное число 1")
                elif int(message.text) > 1000:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    await message.answer("Как-то много. Максимальное число 1000")
                elif int(message.text) < data['rand']:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    await message.answer("Мало. Попробуй ввести число побольше")
                elif int(message.text) > data['rand']:
                    data['count_attempst'] = int(data['count_attempst']) + 1
                    await message.answer("Много. Попробуй ввести число поменьше")
        except ValueError:
            await message.answer("Для чего тут буквы?\nВведи число")
###############################################################################################





"""******************************************************************************************"""
@dp.message_handler(Text(equals=["Лиса"]))
@dp.message_handler(Command("fox"))
async def ez_count(message: Message):
    global cursor
    global connect
    user_id = message.chat.id
    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
    count = int(count[0]) + 10000
    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
    connect.commit()

"""******************************************************************************************"""





















###############################################################################################
class FSMbj(StatesGroup):
    level = State()
    stavka = State()
    game = State()

@dp.message_handler(Text(equals=["BlackJack"]), state=None)
@dp.message_handler(commands=["bj"], state=None)
async def bj_start(message: types.Message):
    global cursor
    global connect
    user_id = message.chat.id
    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
    connect.commit()
    if int(count[0]) == 0:
        await message.answer("Твой баланс равен 0. Воспользуйся другими сервисами, чтобы его пополнить")
        return
    else:
        await FSMbj.level.set()
        await message.answer("Выбери количество колод от 1 до 8\n(Чтобы быстро перейти в эту вкладку используй /bj)", reply_markup=keyboard_back_games)

@dp.message_handler(content_types=['text'], state=FSMbj.level)
async def bj_stavka(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect
        try:
            if 1 <= int(message.text) <= 8:
                data['level'] = int(message.text)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                connect.commit()
                await message.answer("Сделай ставку\nСтавка не должна превышать твой баланс\nТвой баланс: %s" %int(count[0]))
                await FSMbj.next()
            else:
                await message.answer("Введи число от 1 до 8")
        except ValueError:
            await message.answer("Буквы тут ни к чему...\nВведи число от 1 до 8")

@dp.message_handler(content_types=['text'], state=FSMbj.stavka)
async def bj_game(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect

        global pik
        global cross
        global bub
        global cher
        global soc
        global count_gamer
        global count_dealer
        pik = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10.1, 10.2, 10.3, 11] * data['level']
        cross = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10.1, 10.2, 10.3, 11] * data['level']
        bub = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10.1, 10.2, 10.3, 11] * data['level']
        cher = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10.1, 10.2, 10.3, 11] * data['level']
        soc = [pik, cross, bub, cher]
        count_gamer = 0
        count_dealer = 0
        user_id = message.chat.id
        count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
        connect.commit()
        try:
            key = True
            if int(message.text) > int(count[0]):
                await message.answer("Ставка превышает состояние баланса. Попробуй ещё раз")
            elif int(message.text) < 0:
                await message.answer("Ставка не может быть отрицательной. Попробуй ещё раз")
            elif int(message.text) <= int(count[0]):
                await message.answer("Ставка сделана!")
                data['stavka'] = int(message.text)
                d = bj_gamer()
                l = bj_dealer()
                p = bj_gamer()
                await message.answer("Тебе попалась карта - %s %s. Твой счёт: %d\nДилеру попалась карта - %s %s. Счёт дилера: %d\nТебе попалась карта - %s %s. Твой счёт: %d\nДилер положил себе карту рубашкой вверх" %(d[0],d[1],d[2],l[0],l[1],l[2],p[0],p[1],p[2]))
                if p[2] < 21:
                    await message.answer("Хватит или ещё?", reply_markup=keyboard_bj)
                elif p[2] == 21:
                    await message.answer("BlackJack! Ты победил   :)\nВыигрыш увеличен", reply_markup=keyboard_games)
                    user_id = message.chat.id
                    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                    count = int(int(count[0]) + data['stavka'] * 1.5)
                    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                    connect.commit()
                    key = False
                    await state.finish()
                else:
                    await message.answer("Ты проиграл   :(", reply_markup=keyboard_games)
                    user_id = message.chat.id
                    count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                    count = int(count[0]) - data['stavka']
                    cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                    connect.commit()
                    key = False
                    await state.finish()
                if key == True:
                    await FSMbj.next()
        except ValueError:
            await message.answer("Буквы тут ни к чему...\nСделай ставку\n(Ставка не должна превышать твой баланс)")




@dp.message_handler(content_types=['text'], state=FSMbj.game)
async def bj_end(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        global cursor
        global connect

        global pik
        global cross
        global bub
        global cher
        global soc
        global count_gamer
        global count_dealer
        key_dealer = False
        if message.text.lower() == 'ещё':
            d = bj_gamer()
            key = True
            await message.answer("Тебе попалась карта - %s %s. Твой счёт: %d" %(d[0],d[1],d[2]))
            if count_gamer > 21:
                key = False
                await message.answer("Ты проиграл   :(", reply_markup=keyboard_games)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) - data['stavka']
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await state.finish()
            if key == True:
                await message.answer("Ещё или хватит?")
        elif message.text.lower() == "хватит":
            key_dealer = True
            d = bj_dealer()
            await message.answer("Дилеру открыл карту - %s %s. Счёт дилера: %d" % (d[0], d[1], d[2]))
            while count_dealer < 17:
                d = bj_dealer()
                await message.answer("Дилеру попалась карта - %s %s. Счёт дилера: %d" %(d[0],d[1],d[2]))
        if key_dealer == True:
            if count_gamer > 21:
                await message.answer("Ты проиграл   :(", reply_markup=keyboard_games)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) - data['stavka']
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await state.finish()
            elif count_gamer == count_dealer:
                await message.answer("Ничья   :|", reply_markup=keyboard_games)
                await state.finish()
            elif count_dealer > 21:
                await message.answer("Ты выиграл!   :)", reply_markup=keyboard_games)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) + data['stavka']
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await state.finish()
            elif count_gamer > count_dealer:
                await message.answer("Ты выиграл!   :)", reply_markup=keyboard_games)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) + data['stavka']
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await state.finish()
            elif count_dealer > count_gamer:
                await message.answer("Ты проиграл   :(", reply_markup=keyboard_games)
                user_id = message.chat.id
                count = cursor.execute("SELECT count_id FROM data WHERE id == ?", (user_id,)).fetchone()
                count = int(count[0]) - data['stavka']
                cursor.execute("UPDATE data SET count_id == ? WHERE id == ?", (count, user_id))
                connect.commit()
                await state.finish()
###############################################################################################



















executor.start_polling(dp, skip_updates=True)