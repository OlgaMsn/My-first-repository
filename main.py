import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot('Здесь будет ваш токен')

@bot.message_handler(commands=['start'])
def start_massage(message):
    bot.reply_to(message, text='Привет! Я чат-бот, который будет напоминать тебе гулять и кормить Одди')
    remider_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    remider_thread.start()

@bot.message_handler(commands=['fact'])
def fact_massage(message):
    list_of_facts = ['Не забывай что Одди любит играть', 'Одди не любит сидеть один дома', 'Одди самое жизнерадостное существо на свете!']
    random_fact = random.choice(list_of_facts)
    bot.reply_to(message, text=f'Между прочим ... {random_fact}')

def send_reminders(chat_id):
    first_rem = '08:00'
    second_rem = '08:30'
    third_rem = '14:00'
    forth_rem = '20:00'
    fifth_rem = '21:00'
    while True:
        now = datetime.datetime.now().strftime('%H:%M')
        if now == first_rem or now == forth_rem:
            bot.send_message(chat_id, text= "Одди хочет кушать")
            time.sleep(61)
        elif now == second_rem or now == third_rem or now == fifth_rem:
            bot.send_message(chat_id, text="Одди хочет гулять")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)