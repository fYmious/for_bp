import telebot
import webbrowser
import openai
from telebot import types
import random

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
    btn4 = types.KeyboardButton('Решение задач')
    btn6 = types.KeyboardButton('О боте')
    btn5 = types.KeyboardButton('Чат с ИИ')
    markup.add(btn1, btn3, btn5, btn4, btn2, btn6)
    if message.from_user.last_name:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!',
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!',
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
    bot.reply_to(message, f'Вот результаты поиска видео на YouTube по запросу "{youtube_url}".')


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'поиск в интернете')
def handle_search_request(message):
    bot.reply_to(message, 'Введите запрос для поиска в браузере.')
    bot.register_next_step_handler(message, search_yandex)


def search_yandex(message):
    query = message.text
    yandex_url = f'https://www.yandex.com/search/?text={query}'
    webbrowser.open(yandex_url)
    bot.reply_to(message, f'Вот результаты поиска в Яндексе по запросу "{yandex_url}".')


# ______________________________________________________________________________________________________________________
@bot.message_handler(func=lambda message: message.text.lower() == 'чат с ии')
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
                          'команду /start. Также для решения задач вам потребуется аккаунт на таких сайтах, '
                          'как codewars.com'
                          'и leetcode.com')


# ______________________________________________________________________________________________________________________
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
@bot.message_handler(func=lambda message: message.text.lower() == 'решение задач')
def katas(message):
    tasks = ['https://leetcode.com/problems/two-sum/',
             'https://leetcode.com/problems/palindrome-number/',
             'https://leetcode.com/problems/integer-to-roman/',
             'https://leetcode.com/problems/roman-to-integer/',
             'https://leetcode.com/problems/longest-common-prefix/',
             'https://leetcode.com/problems/valid-parentheses/',
             'https://leetcode.com/problems/merge-two-sorted-lists/',
             'https://leetcode.com/problems/remove-duplicates-from-sorted-array/',
             'https://leetcode.com/problems/remove-element/',
             'https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/',
             'https://leetcode.com/problems/search-insert-position/',
             'https://leetcode.com/problems/length-of-last-word/',
             'https://leetcode.com/problems/plus-one/',
             'https://leetcode.com/problems/add-binary/',
             'https://leetcode.com/problems/sqrtx/',
             'https://leetcode.com/problems/remove-duplicates-from-sorted-list/',
             'https://leetcode.com/problems/single-number/',
             'https://leetcode.com/problems/integer-to-english-words/',
             'https://www.codewars.com/kata/5ba38ba180824a86850000f7',
             'https://www.codewars.com/kata/5a00e05cc374cb34d100000d',
             'https://www.codewars.com/kata/55225023e1be1ec8bc000390',
             'https://www.codewars.com/kata/5a2be17aee1aaefe2a000151',
             'https://www.codewars.com/kata/586f6741c66d18c22800010a',
             'https://www.codewars.com/kata/57a2013acf1fa5bfc4000921',
             'https://www.codewars.com/kata/55f9b48403f6b87a7c0000bd',
             'https://www.codewars.com/kata/52fba66badcd10859f00097e',
             'https://www.codewars.com/kata/54da5a58ea159efa38000836',
             'https://www.codewars.com/kata/5266876b8f4bf2da9b000362',
             'https://www.codewars.com/kata/5bb904724c47249b10000131',
             'https://www.codewars.com/kata/582cb0224e56e068d800003c',
             'https://www.codewars.com/kata/58649884a1659ed6cb000072',
             'https://www.codewars.com/kata/59ca8246d751df55cc00014c',
             'https://www.codewars.com/kata/541c8630095125aba6000c00',
             'https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c',
             'https://www.codewars.com/kata/5656b6906de340bd1b0000ac',
             'https://www.codewars.com/kata/55fd2d567d94ac3bc9000064',
             'https://www.codewars.com/kata/56541980fa08ab47a0000040',
             'https://www.codewars.com/kata/54ff3102c1bad923760001f3',
             'https://www.codewars.com/kata/55908aad6620c066bc00002a',
             'https://www.codewars.com/kata/5667e8f4e3f572a8f2000039',
             'https://www.codewars.com/kata/5541f58a944b85ce6d00006a',
             'https://www.codewars.com/kata/52742f58faf5485cae000b9a',
             'https://www.codewars.com/kata/55685cd7ad70877c23000102',
             'https://www.codewars.com/kata/5b853229cfde412a470000d0',
             'https://www.codewars.com/kata/5ae62fcf252e66d44d00008e',
             'https://www.codewars.com/kata/5556282156230d0e5e000089',
             'https://www.codewars.com/kata/55a70521798b14d4750000a4']
    uslovie = random.choice(tasks)

    bot.send_message(message.chat.id, f'Твоя задача: {uslovie}')
    webbrowser.open(uslovie)


# ______________________________________________________________________________________________________________________
# _______________________________________КОНЕЦ__________________________________________________________________________
# ______________________________________________________________________________________________________________________

bot.polling()
