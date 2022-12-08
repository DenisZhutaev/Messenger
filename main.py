from flask import Flask, request, render_template

app = Flask(__name__)

messages_list = []


def add_message(name, text):
    new_message = {
        "name": name,
        "text": text,
        "time": "28:69",
    }
    messages_list.append(new_message)


add_message('Mike', 'Hello im finish')


@app.route('/')
def hello():
    return 'Hello on messenger'


@app.route('/get_messages')
def get_messages():
    return {'messages': messages_list}


@app.route('/send_message')
def send_message():
    name = request.args.get('name')
    text = request.args.get('text')
    add_message(name, text)
    return 'ok'


@app.route('/chat')
def display_chat():
    return render_template('chat.html')


app.run()

# This is a sample Python script.
# МЕССЕНДЖЕР

# Список всех сообщений
# messages_list = []
#
#
# # Функция для добавления новых сообщений (имя отправителя, текст сообщений) в список
# def add_message(name, text):
#     new_message = {
#         "name": name,
#         "text": text,
#         "time": "28:69",  # ДЗ: Подставить текущее время Часы:Минуты
#     }
#     messages_list.append(new_message)
#
#
# add_message("Майк", "Йо, это первое сообщение")
# add_message("Витя", "А чо так можно было чтоли?")
#
#
# # Функция для чтения сообщений
# def print_messages_list():
#     # for in
#     # Для каждого сообщения в списке сообщений, сделать следующее:
#     for message in messages_list:
#         # Здесь идет код, который может сделать какие-либо действия с сообщением message
#         name = message["name"]
#         text = message["text"]
#         time = message["time"]
#         print(f"[{name}]: {text} // {time} ")
#
#
# print_messages_list()
