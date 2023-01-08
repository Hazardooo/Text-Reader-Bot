from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ContentType, Message
from piceye import ImgToStr
from config import Settings_config, New_User

print("status: Bot started!...")
Settings_config().check_settings()
try:
    bot = Bot(Settings_config().TOKEN_API())
except:
    print("You have not inserted the token into the file config.txt!")
    exit(input("press Enter..."))
dp = Dispatcher(bot)
Lang_Pointer = ImgToStr(Settings_config().path_way())


@dp.message_handler(commands=["start"])
async def encho(message: Message):
    await message.answer(text="Приветсвую друг!", reply_markup=ReplyKeyboardMarkup(resize_keyboard=True).add(KeyboardButton("🇷🇺"), KeyboardButton("🇺🇸")))


@dp.message_handler(content_types=ContentType.PHOTO)
async def re_return(message: Message):
    user = New_User(message.from_user.id)
    await message.photo[-1].download(destination_file=user.catalog()+'/image.png')
    await message.answer(text=Lang_Pointer.recognition_text(user.catalog()+'/image.png'))
    user.clear_catalog()


@dp.message_handler()
async def Lang(message: Message):
    if message.text == '🇷🇺':
        await message.answer(text="RU!")
        Lang_Pointer.lang_point(True)

    elif message.text == '🇺🇸':
        await message.answer(text="USA!")
        Lang_Pointer.lang_point(False)


if __name__ == "__main__":
    executor.start_polling(dp)
