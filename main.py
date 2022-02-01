from flask import Flask
import datetime

app = Flask(__name__)

# Структура одного сообщения
# Список сообщений - список словарей
messages_list = [
 {
    'text': 'Всем приветы в этом чате',
    'sender': 'Васисуалий',
    'date': '31-01-22 21:00',
 },
 {
    'text': 'Какие дела',
    'sender': 'Мишаня',
    'date': '31-01-22 22:00',
 }
]


def print_message(message):
    '''Функция которая выводит одно сообщение'''
    print(f"[{message['sender']}]: {message['text']} / {message['date']}")
    print('-' * 50)


def add_message(name, txt):
    '''Функция добавления нового сообщения в список сообщений'''
    message = {
        'text': txt,
        'sender': name,
        'date': datetime.datetime.now()
    }
    messages_list.append(message)


# Пройдем по всем элементам списка
# for m in messages_list:
#     print_message(m)

# Главная страница
@app.route('/')
def index_page():
    return 'Hello, welcome to Chat'


# Раздел со списком сообщений
@app.route('/get_messages')
def get_messages():
    return {'messages': messages_list}


# Раздел для отправки сообщений
@app.route('/send_message')
def send_message():
    # Как получить данные из браузера?
    add_message(name, text)


app.run()




