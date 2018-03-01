import telebot
import const
import markups
import time
import base
from telebot import types


bot = telebot.TeleBot(const.token)


@bot.message_handler(commands=['start'])
def start(message):
    if message.chat.id in const.admins:
        markup = markups.start_admin()
    else:
        markup = markups.start()
    bot.send_message(message.chat.id, 'Привет, ' + message.from_user.first_name + '!', reply_markup=markup)
    base.add_user(message)


@bot.message_handler(content_types=['text'])
def zvonki(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn_user = telebot.types.InlineKeyboardButton(text="Купить", url="http://likebz.org/concentrat")
    markup.add(btn_user)

    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row('НАЗАД')

    if message.text == 'Когда':
        bot.send_message(message.chat.id, const.about, parse_mode='HTML')

    if message.text == 'Где':
        bot.send_message(message.chat.id, const.amenities, parse_mode='HTML')

    if message.text == 'Сколько стоит':
        bot.send_message(message.chat.id, const.contactus,
                         parse_mode='HTML', reply_markup=markup)

    if message.text == 'Контакты':
        bot.send_message(message.chat.id, const.contact,
                         parse_mode='HTML')

    if message.text == 'Частые вопросы':
        bot.send_message(message.chat.id, const.vopros,
                         parse_mode='HTML')

    if message.text == 'Рассылка':
        msg = bot.send_message(message.chat.id, "Введите текст, который хотите отправить всем не клиентам", reply_markup=keyboard)
        bot.register_next_step_handler(msg, send_to_users)

    if message.text == '/otvet_1':
        bot.send_message(message.chat.id, const.otvet_1,
                         parse_mode='HTML')

    if message.text == '/otvet_2':
        bot.send_message(message.chat.id, const.otvet_2,
                         parse_mode='HTML')

    if message.text == '/otvet_3':
        bot.send_message(message.chat.id, const.otvet_3,
                         parse_mode='HTML')

    if message.text == '/otvet_4':
        bot.send_message(message.chat.id, const.otvet_4,
                         parse_mode='HTML')

    if message.text == '/otvet_5':
        bot.send_message(message.chat.id, const.otvet_5,
                         parse_mode='HTML')

    if message.text == '/otvet_6':
        bot.send_message(message.chat.id, const.otvet_6,
                         parse_mode='HTML')


def send_to_users(message):
    if message.text.upper() == "НАЗАД":
            bot.send_message(message.chat.id, "Отменено", reply_markup=markups.start_admin())
            return
    else:
            count = 0
            for user in base.get_all_users():
                #if user[8] == 'FALSE':
                    count += 1
                    print(count)
                    if user[1] == const.admins:
                        continue
                    if count % 20 == 0:
                        time.sleep(1)
                    try:
                        bot.send_message(user[1], message.text)
                        print("message sent to %s count = %s" % (user[4], count))
                    except Exception as e:
                        continue
            bot.send_message(message.chat.id, "Сообщение успешно отправлено всем !",
                             reply_markup=markups.start_admin())

bot.polling()
