import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

token = '7622410047:AAFlO56wwFKrbe79iBMAkkq1hlUcwbcEUp4'
bot = telebot.TeleBot(token)

user_scores = {}  # Словарь для хранения баллов каждого пользователя

def update_score(user_id, correct):
    if user_id not in user_scores:
        user_scores[user_id] = 0
    if correct:
        user_scores[user_id] += 1

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот задаёт вопросы в аудио стиле. Напиши /1_question')

@bot.message_handler(commands=['1_question'])
def question_1(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Zakovat testini boshlash", callback_data='boshlash'))
    markup.add(InlineKeyboardButton("Natijalarni ko'rish", callback_data="natijalarni_korish"))
    bot.send_message(message.chat.id, 'Удачи!', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'boshlash')
def send_audio(call):
    with open('вапрос_1.mp3', 'rb') as audio:
        bot.send_audio(call.message.chat.id, audio, caption='Ответы: /1_answers')

@bot.message_handler(commands=['1_answers'])
def answer_1(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ona tili (a)", callback_data='a_1'))
    markup.add(InlineKeyboardButton("Rus tili (b)", callback_data='b_1'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_1')
def answer_1_1(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Вы ответили правильно! Следующий вопрос: /2_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_1')
def answer_1_2(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Вы ответили неправильно.')

# ======== ВОПРОС 2 ========
@bot.message_handler(commands=['2_question'])
def question_2(message):
    try:
        with open('вапрос_2.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /2_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['2_answers'])
def answer_2(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_2'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_2'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_2')
def answer_2_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /3_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_2')
def answer_2_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 3 ========
@bot.message_handler(commands=['3_question'])
def question_3(message):
    try:
        with open('вапрос_3.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /3_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['3_answers'])
def answer_3(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_3'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_3'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_3')
def answer_3_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /4_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_3')
def answer_3_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 4 ========
@bot.message_handler(commands=['4_question'])
def question_4(message):
    try:
        with open('вапрос_4.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /4_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['4_answers'])
def answer_4(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_4'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_4'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_4')
def answer_4_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /5_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_4')
def answer_4_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 5 ========
@bot.message_handler(commands=['5_question'])
def question_5(message):
    try:
        with open('вапрос_5.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /5_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['5_answers'])
def answer_5(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_5'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_5'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_5')
def answer_5_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /6_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_5')
def answer_5_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 6 ========
@bot.message_handler(commands=['6_question'])
def question_6(message):
    try:
        with open('вапрос_6.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /6_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['6_answers'])
def answer_6(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_6'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_6'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_6')
def answer_6_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /7_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_6')
def answer_6_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 7 ========
@bot.message_handler(commands=['7_question'])
def question_7(message):
    try:
        with open('вапрос_7.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /7_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['7_answers'])
def answer_7(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_7'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_7'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_7')
def answer_7_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /8_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_7')
def answer_7_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 8 ========
@bot.message_handler(commands=['8_question'])
def question_8(message):
    try:
        with open('вапрос_8.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /8_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['8_answers'])
def answer_8(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_8'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_8'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_8')
def answer_8_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /9_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_8')
def answer_8_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 9 ========
@bot.message_handler(commands=['9_question'])
def question_9(message):
    try:
        with open('вапрос_9.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /9_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['9_answers'])
def answer_9(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_9'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_9'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_9')
def answer_9_true(call):
    update_score(call.from_user.id, True)
    bot.send_message(call.message.chat.id, '✅ Верно! Следующий вопрос: /10_question')

@bot.callback_query_handler(func=lambda call: call.data == 'b_9')
def answer_9_false(call):
    update_score(call.from_user.id, False)
    bot.send_message(call.message.chat.id, '❌ Неверно.')

# ======== ВОПРОС 10 ========
@bot.message_handler(commands=['10_question'])
def question_10(message):
    try:
        with open('вапрос_10.mp3', 'rb') as audio:
            bot.send_audio(message.chat.id, audio, caption='Ответы: /10_answers')
    except FileNotFoundError:
        bot.send_message(message.chat.id, 'Аудиофайл не найден!')

@bot.message_handler(commands=['10_answers'])
def answer_10(message):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Ответ A", callback_data='a_10'))
    markup.add(InlineKeyboardButton("Ответ B", callback_data='b_10'))
    bot.send_message(message.chat.id, 'Выберите правильный ответ:', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'a_10')
def answer_10_true(call):
    update_score(call.from_user.id, True)
    show_final_buttons(call)

@bot.callback_query_handler(func=lambda call: call.data == 'b_10')
def answer_10_false(call):
    update_score(call.from_user.id, False)
    show_final_buttons(call)

# Функция для показа кнопок после завершения викторины
def show_final_buttons(call):
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton("Пройти заново", callback_data='restart'))
    markup.add(InlineKeyboardButton("Подсчитать баллы", callback_data='show_score'))
    bot.send_message(call.message.chat.id, "🏁 Викторина завершена!", reply_markup=markup)

# Обработчик кнопки "Пройти заново"
@bot.callback_query_handler(func=lambda call: call.data == 'restart')
def restart_quiz(call):
    user_scores[call.from_user.id] = 0  # Обнуляем баллы пользователя
    bot.send_message(call.message.chat.id, "🔁 Викторина начинается заново! Напиши /1_question")

# Обработчик кнопки "Подсчитать баллы"
@bot.callback_query_handler(func=lambda call: call.data == 'show_score')
def show_score(call):
    score = user_scores.get(call.from_user.id, 0)
    bot.send_message(call.message.chat.id, f"📊 Ваш результат: {score}/10")

bot.polling()
