import telebot


def start():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Когда', 'Где')
    keyboard.row('Сколько стоит', 'Контакты')
    keyboard.row('Частые вопросы')
    return keyboard


def start_admin():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('Когда', 'Где')
    keyboard.row('Сколько стоит', 'Контакты')
    keyboard.row('Частые вопросы')
    keyboard.row('Рассылка')
    return keyboard
