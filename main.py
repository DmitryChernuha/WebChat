from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)


db_file = "./data/db.json"  # Путь к файлу
json_db = open(db_file, 'rb')  # Открываем файл
data = json.load(json_db)  # Загружаем данные из файла
messages_list = data["messages_list"]  # Берем сообщение из структуры и кладем в переменную


def save_message():
    '''Функция сохранения сообщений в файл'''
    data = {
        "messages_list": messages_list,
    }
    json_db = open(db_file, "w")
    json.dump(data, json_db)  # Записываем данные в файл


def print_message(message):
    '''Функция которая выводит одно сообщение'''
    print(f"[{message['sender']}]: {message['text']} / {message['date']}")
    print('-' * 50)


def add_message(name, txt):
    '''Функция добавления нового сообщения в список сообщений'''
    message = {
        'text': txt,
        'sender': name,
        'date': datetime.now().strftime('%H:%M')
    }
    messages_list.append(message)


# Пройдем по всем элементам списка
# for m in messages_list:
#     print_message(m)


@app.route('/')
def index_page():
    '''Главная страница'''
    return 'Hello, welcome to Chat'


@app.route('/get_messages')
def get_messages():
    '''Раздел со списком сообщений'''
    return {'messages': messages_list}


# Раздел для отправки сообщений
@app.route('/send_message')
def send_message():
    # Как получить данные из браузера?
    name = request.args['name']
    text = request.args['text']
    add_message(name, text)
    save_message()  # Сохраняем все сообщения в файл
    return 'Ok'

# Раздел с визуальным интерефейсом


@app.route('/form')
def form():
    return render_template('form.html')


app.run()




