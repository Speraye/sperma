import telebot
bot = telebot.TeleBot('1121670252:AAHxgJZly_Z5KGt57UD6qxPjgyNkmXC6Zlg')
keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.row('⏮Главное Меню')
keyboard.row('🏪Магазин')
keyboard.row('👥Пригласить друга')
keyboard.row('📝Ввести код')
keyboard.row('💵Заработать с нами')
 
 
inline_keyboard = telebot.types.InlineKeyboardMarkup()
item1 = telebot.types.InlineKeyboardButton("Новотроицк", callback_data='good1')
item2 = telebot.types.InlineKeyboardButton("Орск", callback_data='bad1')
item3 = telebot.types.InlineKeyboardButton("Гай", callback_data='suka') 
item4 = telebot.types.InlineKeyboardButton("Оренбург", callback_data='lox')
item5 = telebot.types.InlineKeyboardButton("Ясный", callback_data='ahel')
 
inline_keyboard.row(item1)
inline_keyboard.row(item2)
inline_keyboard.row(item3)
inline_keyboard.row(item4)
inline_keyboard.row(item5)

inl_keyboard = telebot.types.InlineKeyboardMarkup()
vib1 = telebot.types.InlineKeyboardButton("Район1", callback_data='one')
vib2 = telebot.types.InlineKeyboardButton("Район2", callback_data='two')
vib3 = telebot.types.InlineKeyboardButton("Район3", callback_data='free')
vib4 = telebot.types.InlineKeyboardButton("Район4", callback_data='four')
vib5 = telebot.types.InlineKeyboardButton("Район5", callback_data='five')

inl_keyboard.row(vib1)
inl_keyboard.row(vib2)
inl_keyboard.row(vib3)
inl_keyboard.row(vib4)
inl_keyboard.row(vib5)

lol_keyboard = telebot.types.InlineKeyboardMarkup()
lox1 = telebot.types.InlineKeyboardButton('💎 Кокаин 1 грамм - 5500 💎', callback_data='odin')
lox2 = telebot.types.InlineKeyboardButton('💎 Шишки 2 грамма - 1700 💎', callback_data='dwa')
lox3 = telebot.types.InlineKeyboardButton('💎 Гашиш EURO 1 грамм - 900 💎', callback_data='tri')
lox4 = telebot.types.InlineKeyboardButton('💎 Амфетамин 1 грамм - 800 💎', callback_data='che')
lox5 = telebot.types.InlineKeyboardButton('💎 MDMA 1 таблетка - 900 💎', callback_data='pyat')
lox6 = telebot.types.InlineKeyboardButton('💎 Метадон 1 грамм - 1000 💎', callback_data='shest')

mon_keyboard = telebot.types.InlineKeyboardMarkup()
money1 = telebot.types.InlineKeyboardButton('QIWI', callback_data='qiwas')
money2 = telebot.types.InlineKeyboardButton('BTC', callback_data='bitok')
money3 = telebot.types.InlineKeyboardButton('Отменить покупку', callback_data='exit')

mon_keyboard.row(money1, money2)
mon_keyboard.row(money3)



lol_keyboard.row(lox1)
lol_keyboard.row(lox2)
lol_keyboard.row(lox3)
lol_keyboard.row(lox4)
lol_keyboard.row(lox5)
lol_keyboard.row(lox6)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, '💎Приветствую тебя в нашем магазине💎\n\n👉Для быстрого перемещения по разделам используйте кнопки снизу👇\n\nРазработчик бота @badboyee', reply_markup=keyboard)
 
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '⏮Главное Меню':
        bot.send_message(message.chat.id, '💎Приветствую тебя в нашем магазине💎\n\n👉Для быстрого перемещения по разделам используйте кнопки снизу👇\n\nРазработчик бота @badboyee')
    if message.text == '🏪Магазин':
        bot.send_message(message.chat.id, '<b>ВНИМАНИЕ</b>\n\n📊У нас самые низкие цены📊\n\nСамые большие скидки\n\nАдекватные операторы\n\nНе переплачивай на гидре за переводы, бери разумно, оплачивай как тебе хочется\n\nИз списка ниже выберите ваш город', parse_mode='html',reply_markup=inline_keyboard)
    if message.text == '👥Пригласить друга':
        bot.send_message(message.chat.id, 'Допустимы только цифры')
    if message.text == '📝Ввести код':
        bot.send_message(message.chat.id, '👍Введите реферальный код')
    if message.text == '💵Заработать с нами':
        bot.send_message(message.chat.id, '💎Хотите работать с нами?💎\nВот что мы предлагаем:\n\n💲Высокий уровень ЗП\n🕜Гибкий трафик на выбор\n💰Активный карьерный рост\n\nНам нужны:\n<b>🚶Курьеры пешие\n🚕Водители(личный транспорт, загран паспорт\n💊Химики (с опытом и без)</b>', parse_mode='html')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good1':
                bot.send_message(call.message.chat.id, 'Выберите район', reply_markup=inl_keyboard)
            if call.data == 'bad1':
                bot.send_message(call.message.chat.id, 'Выберите район', reply_markup=inl_keyboard)
            if call.data == 'suka':
                bot.send_message(call.message.chat.id, 'Выберите район', reply_markup=inl_keyboard)
            if call.data == 'lox':       
                bot.send_message(call.message.chat.id, 'Выберите район', reply_markup=inl_keyboard)
            if call.data == 'ahel':      
                bot.send_message(call.message.chat.id, 'Выберите район', reply_markup=inl_keyboard)   
            if call.data == 'one':
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'two':
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'free':
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'four': 
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'five':
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'odin':
                bot.send_message(call.message.chat.id, '🛒  Покупка Амфетамин 1 грамм\n💲  Цена 800₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)
            if call.data == 'dwa':
                bot.send_message(call.message.chat.id, '🛒  Покупка Шишки 2 грамма\n💲  Цена 1700₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)
            if call.data == 'tri':
                bot.send_message(call.message.chat.id, '🛒  Покупка Гашиш EURO 1 грамм\n💲  Цена 900₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)
            if call.data == 'che':
                bot.send_message(call.message.chat.id, '🛒  Покупка Амфетамин 1 грамм\n💲  Цена 800₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)
            if call.data == 'pyat':
                bot.send_message(call.message.chat.id, '🛒  Покупка MDMA 1 таблетка\n💲  Цена 900₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)
            if call.data == 'shest':
                bot.send_message(call.message.chat.id, '🛒  Покупка Метадон 1 грамм\n💲  Цена 1000₽\n\n💳  Выберите способ оплаты  💳', reply_markup=mon_keyboard)  
            if call.data == 'qiwas':
                bot.send_message(call.message.chat.id, '📄  Номер заказа #00000\n\n🛒  Товар Метадон 1 грамм\n💲  К оплате 1000₽\n\n💰 Реквизиты QIWI +79586278070\n📌  Комментарий к переводу 12345\n\nКонтакты оператора')            
            if call.data == 'bitok':
                bot.send_message(call.message.chat.id, '📄  Номер заказа #00000\n\n🛒  Товар Метадон 1 грамм\n💲  К оплате 1000₽\n\n💰 Реквизиты <b>1LBqr2jRUWF6ZzMqpGapqDaApj79U7Cssv</b>\n\n📌 Контакты оператора ', parse_mode='html')
            if call.data == 'exit':
                bot.send_message(call.message.chat.id, '<b>Покупка успешно отменена</b>', parse_mode='html')
            
            
            
            
            
            
            
            
            
            if call.data == 'six':  
                bot.send_message(call.message.chat.id, '💉Выберите товар', reply_markup=lol_keyboard)
            if call.data == 'qiwas':
                bot.send_message(call.message.chat.id, '📄  Номер заказа #00000\n\n🛒  Товар Кокаин 1 грамм\n\n💲  К оплате 5500₽\n\n💰 Реквизиты QIWI <b>+79586278070</b>\n\n📌  Комментарий к переводу 12345\n\nКонтакты оператора ', parse_mode='html')
            if call.data == 'bitok':
                bot.send_message(call.message.chat.id, '📄  Номер заказа #00000\n\n🛒  Товар Метадон 1 грамм\n\n💲  К оплате 1000₽\n\n💰 Реквизиты <b>1LBqr2jRUWF6ZzMqpGapqDaApj79U7Cssv</b>\n\n📌 Контакты оператора ', parse_mode='html')  
            if call.data == 'exit':
                bot.send_message(call.message.chat.id, '<b>Покупка успешно отменена</b>', parse_mode='html')            


               
    except Exceptions:
        pass

bot.polling(none_stop=True)