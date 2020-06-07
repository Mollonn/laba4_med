import telebot

bot = telebot.TeleBot('1184393666:AAF688UCMz5JUOyjE98gdI9jqurxXSgkdq8')

add_info = {'Перечень необходимых документов': ['Копия ИНН', 'Мед.справка', 'Копия паспорта', '5 фото размером 3х4см'],
            'Стоимость индивидуального урока': ['500грн/час'],
            'Акционные предложения': [
                'Только сейчас действует акция -20% на любой курс обучений!\nЗа подробностями обращайтесь по указанным контактам.'],
            'Контакты': ['Харьков, пл.Свободы 2, \nТел.: +380674672737, +380994672737']}
category = {'A': ['Стоимость полного курса составит 3000 грн.'],
            'B': ['Стоимость полного курса составит 4000 грн.'],
            'C': ['Стоимость полного курса составит 2250 грн.']}


def createKeyboard(dict):
    keyboard = telebot.types.InlineKeyboardMarkup()
    for key in dict.keys():
        keyboard.add(telebot.types.InlineKeyboardButton(text=key, callback_data=key))
    return keyboard


def printRes(l):
    text = ''
    for el in l:
        text = text + '\n' + el
    return text


@bot.message_handler(commands=['start'])
def start_message(message):
    keyboard = telebot.types.InlineKeyboardMarkup()

    keyboard.add(telebot.types.InlineKeyboardButton(text='Узнать стоимость обучения', callback_data='Price_Cat'))
    keyboard.add(telebot.types.InlineKeyboardButton(text='Дополнительные вопросы', callback_data='Info'))
    bot.send_message(message.chat.id, 'Вы зашли на информационную страницу автошколы.\nВыберите, что вас интересует: ',
                     reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def main_query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id)

    if call.data == 'Info':
        typeKey = createKeyboard(add_info)
        bot.send_message(call.message.chat.id, '\nВыберите что вас интересует:', reply_markup=typeKey)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data in add_info.keys():
        result = printRes(add_info.get(call.data))
        bot.send_message(call.message.chat.id, result)

    elif call.data == 'Price_Cat':
        typeKey = createKeyboard(category)
        bot.send_message(call.message.chat.id, '\nВыберите желаемую категорию:', reply_markup=typeKey)
        bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

    elif call.data in category.keys():
        result = printRes(category.get(call.data))
        bot.send_message(call.message.chat.id, result)


bot.polling()
