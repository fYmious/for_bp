import telebot
import webbrowser
import openai
from telebot import types
from googletrans import Translator

TOKEN = '6198347508:AAGJRmdq8xHU6htOt9CygGBNPSy9wa9dIAI'
bot = telebot.TeleBot(TOKEN)
openai.api_key = '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'


# ______________________________________________________________________________________________________________________
# _______________________________________СТАРТ С КНОПКАМИ_______________________________________________________________
# ______________________________________________________________________________________________________________________

@bot.message_handler(commands=['start'])
def main(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Поиск в интернете')
    btn2 = types.KeyboardButton('Полезные ссылки')
    btn3 = types.KeyboardButton('Видео')
    btn6 = types.KeyboardButton('О боте')
    btn5 = types.KeyboardButton('Чат с ИИ-экспертом')
    markup.add(btn1, btn2, btn3, btn5, btn6)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!',
                     reply_markup=markup)


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'видео')
def handle_video_request(message):
    bot.reply_to(message, 'Введите запрос для поиска видео на YouTube.')
    bot.register_next_step_handler(message, search_youtube_video)


def search_youtube_video(message):
    query = message.text
    youtube_url = f'https://www.youtube.com/results?search_query={query}'
    webbrowser.open(youtube_url)
    bot.reply_to(message, f'Вот результаты поиска видео на YouTube по запросу "{query}".')


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'поиск в интернете')
def handle_search_request(message):
    bot.reply_to(message, 'Введите запрос для поиска в браузере.')
    bot.register_next_step_handler(message, search_yandex)


def search_yandex(message):
    query = message.text
    yandex_url = f'https://www.yandex.com/search/?text={query}'
    webbrowser.open(yandex_url)
    bot.reply_to(message, f'Вот результаты поиска в Яндексе по запросу "{query}".')


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'чат с ии-экспертом')
def handle_search_request(message):
    bot.reply_to(message, 'Введите запрос для ИИ-эксперта.')
    bot.register_next_step_handler(message, search_ai)


def search_ai(message):
    user_input = message.text

    response = openai.Completion.create(
        engine='text-davinci-003',  # Выбор движка ChatGPT
        prompt=user_input,
        max_tokens=1000,  # Максимальное количество токенов в ответе
        n=1,  # Количество вариантов ответа
        # stop=None,  # Символы, сигнализирующие о конце ответа
        # temperature=0.7,  # Параметр, определяющий "творчество" ответа
        # top_p=1.0,  # Режим обрезки распределения вероятностей ответов
        # frequency_penalty=0.0,  # Параметр для управления повторами в ответе
        # presence_penalty=0.0,  # Параметр для управления ответами, связанными с вопросом
    )

    bot_response = response.choices[0].text.strip()
    bot.send_message(message.chat.id, bot_response)


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'о боте')
def handle_search_request(message):
    bot.reply_to(message, 'Бот создан в рамках решения кейса в конкурсе Большая перемена Дощенниковым Никитой. Это '
                          'тестовый проект, а значит присутствие багов не исключено. Обо всех найденных ошибках прошу '
                          'сообщать мне. Перед использованием бота настоятельно рекомендую ознакомиться с небольшой '
                          'инструкцией. Мои контакты: VK: https://vk.com/ne_vlad_no_marmelad Telegram: @zxccursed9937 '
                          'Mail: nikitadoshennikov@yandex.ru Phone: +79002054832. Мини-инструкция: бот принимает '
                          'только сообщения из выпадающего списка(KeyboardButtons), для каждого нового запроса '
                          'следует заново нажать на кнопку. Если Вы где-то запутались, всегда можете прописать '
                          'команду /start.')
#_______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'полезные ссылки')
def handle_search_request(message):
    bot.reply_to(message, 'Хочу поделиться некоторыми ссылками, которые могут помочь при обучении: codewars.com - '
                          'образовательный сайт, на котором вы можете найти огромное количество задач на многих '
                          'языках программирования с различными решениями от множества пользователей; leetcode.com - '
                          'платформа для подготовки к профессиональным интервью для программистов, путем решения '
                          'задачек, которые встречаются многим, кто устраивается на работу. также на сайте '
                          'присутсвуют подробнейшие видеорешения для каждой задачи от прфессиональных программистов;'
                          'stackoverflow.com - один из крупнейших форумов для программистов, где Вы можете найти ответы'
                          'на большинство своих вопросов, так как на них ответят матерые кодеры;'
                          ' github.com - крупнейший веб-сервис для хостинга IT-проектов и их совместной разработки, где '
                          'вы можете составлять портфолио своих работ;'
                          ' cyberforum.ru - русскоязычный форум программистов и системных администраторов, схожий со '
                          'stackoverflow')
# ______________________________________________________________________________________________________________________
# _______________________________________КОНЕЦ__________________________________________________________________________
# ______________________________________________________________________________________________________________________

bot.polling()
