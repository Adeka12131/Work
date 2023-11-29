from config import *
from aiogram import types, Bot, Dispatcher, executor
from aiogram.types import InputFile

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    await bot.send_message(chat_id=OWNER_ID,text='''Привет,я бот-помощник команды WorkBench.
Задай интересующий тебя вопрос и я на него отвечу.
Также с моей помощью ты можешь посмотреть наши работы.Что бы начать нажмите /start''')

main_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
b_quest3 = types.KeyboardButton('Кто вы такие?')
b_quest4 = types.KeyboardButton('Как с вами связаться?')
b_quest5 = types.KeyboardButton('Наши работы')
tg = types.KeyboardButton('Наши отзывы')
main_keyboard.row(b_quest3).add(b_quest4).add(b_quest5).add(tg)

back_kb = types.InlineKeyboardMarkup()
back1 = types.InlineKeyboardButton(text="Вернуться назад",callback_data="back")
back_kb.add(back1)

question1_kb = types.InlineKeyboardMarkup()
question1 = types.InlineKeyboardButton(text="О нас 🧑🏻‍💻",callback_data="Занимаемся чем то")
question2 = types.InlineKeyboardButton(text="Чем мы занимаемся❔",callback_data="Что мы делаем")
question4 = types.InlineKeyboardButton(text="Наши особенности✨",callback_data="почему именно мы")
question1_kb.add(question1).add(question2).add(question4)

question3_kb = types.InlineKeyboardMarkup()
question3 = types.InlineKeyboardButton(' По Whatsapp',url = 'https://web.whatsapp.com/:')
question5 = types.InlineKeyboardButton(' По Telegram',url = 'https://web.telegram.org/')
question6 = types.InlineKeyboardButton(' По Instagram',url = 'https://www.instagram.com/:')
question10 = types.InlineKeyboardButton(' По Viber',url = 'https://www.viber.com/ru/')
question3_kb.add(question3).add(question5).add(question6).add(question10)

question4_kb = types.InlineKeyboardMarkup()
question7 = types.InlineKeyboardButton(text="1 работа",callback_data="1 работа")
question8 = types.InlineKeyboardButton(text="2 работа",callback_data="2 работа")
question9 = types.InlineKeyboardButton(text="3 работа",callback_data="3 работа")
question4_kb.add(question7).add(question8).add(question9)

tg1_kb = types.InlineKeyboardMarkup()
tg1 = types.InlineKeyboardButton(text="Наши отзывы",url = "https://t.me/kosti")
tg1_kb.add(tg1)


def back(update, context):
    query = update.callback_query
    query.edit_message_text(text="Вернулись назад!")


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    photo_path = (r"C:\Users\User\OneDrive\Рабочий стол\кот\7ff3de4c-fb2c-4d66-bd23-40f9e0e26bc2.jpg")
    await bot.send_photo(message.chat.id, InputFile(photo_path), caption='Здравствуйте! Я бот команды WorkBench. Чем могу помочь сегодня?', reply_markup=main_keyboard)

@dp.callback_query_handler(lambda callback_query: True)
async def handle_callback_query(callback_query: types.CallbackQuery):
    if callback_query.data == "Занимаемся чем то":
        await bot.send_message(callback_query.from_user.id, '''Мы - сообщесво IT-специалистов🌐
Занимаемся созданием веб-интерфейсов, мобильных приложений, телеграмм-ботов.  
Также у нас происходит оплачиваемая стажировка(т.е. обучение) с будущей возможностью присоединиться к нам в команду! ⚡''')
    elif callback_query.data == "Что мы делаем":
        await bot.send_message(callback_query.from_user.id, '''Мы разрабатываем сайты и мобильные приложения, пишем телеграмм боты,а также создаем UI/UX дизайн👩🏻‍🎨''')
    elif callback_query.data == "почему именно мы":
        await bot.send_message(callback_query.from_user.id,
'''Наш главный плюс - это бесплатное предоставление логотипа компании при любом заказе🤘
В своих задачах,мы используем креативный и индивидуальный подход, тщательно проанализируя продукт и конкурентов.😎 
У нас есть несколько этапов разработки. Прежде чем пустить продукт на рынок,мы качественно тестируем его. Также у нас очень короткие сроки выполнения, низкие цены и отличное качество💰☺️
        ''' )
    elif callback_query.data == "1 работа":
        await bot.send_message(callback_query.from_user.id, "1 работа https://github.com/",reply_markup=back_kb)
    elif callback_query.data == "2 работа":
        await bot.send_message(callback_query.from_user.id, "2 работа https://github.com/",reply_markup=back_kb)
    elif callback_query.data == "3 работа":
        await bot.send_message(callback_query.from_user.id, "3 работа https://github.com/",reply_markup=back_kb)
    elif callback_query.data == "back":
        await bot.send_message(callback_query.from_user.id, "Вот наши работы:",reply_markup=question4_kb)

@dp.message_handler()
async def main_message(message: types.Message):
    if message.text == 'Кто вы такие?':
        await message.answer('Выберите интересующий вас вопрос:', reply_markup=question1_kb)
    elif message.text == 'Как с вами связаться?':
        await message.answer('Вы можете связаться с нами по:',reply_markup=question3_kb)
    elif message.text == 'Наши работы':
        await message.answer('Вот наши работы:',reply_markup=question4_kb)
    elif message.text == 'Наши отзывы':
        await message.answer('Вот наши отзывы',reply_markup=tg1_kb)
    
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    
    