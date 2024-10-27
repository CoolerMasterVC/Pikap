from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import json
import os

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота, полученный у @BotFather
BOT_TOKEN = '7882305908:AAFuWhjoT9tOKTCNLLnE6AJJjR4Z4nxU3cE'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

with open(os.path.join("users_settings.json"),"r", encoding="utf-8") as file:
    users_settings = json.load(file)

def users_settings_change():
    with open(os.path.join("users_settings.json"),"w") as file:
        json.dump(users_settings,file)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):

    if not str(message.from_user.id) in users_settings:
        users_settings[str(message.from_user.id)] = {
            "name": "",
            "status_registred": True,
            "wins": 0,
            "loses": 0
        }
        await message.answer(f"Добрый день.\nВведите своё имя.")
    else:
        name = users_settings[str(message.from_user.id)]["name"]
        await message.answer(f"Привет, {name}")
    #await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=['help']))
async def process_help_command(message: Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ '
        'я пришлю тебе твое сообщение'
    )


# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    try:

        if users_settings[str(message.from_user.id)]["status_registred"] == True:
            users_settings[str(message.from_user.id)]["name"] = message.text
            users_settings[str(message.from_user.id)]["status_registred"] = False
            await message.reply(text="Регистрация завершена")
            users_settings_change()
        else:
            name = users_settings[str(message.from_user.id)]["name"]
            await message.reply(text=f"{name}: {message.text}")
    except:
        await message.reply(text="Напишите /start, чтобы пройти регистрацию")


if __name__ == '__main__':
    dp.run_polling(bot)