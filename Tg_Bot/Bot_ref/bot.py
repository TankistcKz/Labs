import os
import re
import json
import random

import telebot
import wikipedia
import bs4
import requests
from telebot import types
from dotenv import load_dotenv

# ──────────────────────────────────────────────
# Конфигурация
# ──────────────────────────────────────────────
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(BOT_TOKEN, parse_mode=None)
wikipedia.set_lang("ru")

with open("tanks.json", encoding="utf-8") as f:
    TANKS: dict = json.load(f)

TANK_STATS_FOOTER = "\n\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%."

USEFUL_LINKS: dict[str, str] = {
    "Официальный сайт": "https://tanki.su/?new_layout=0",
    "Ютуб-канал":       "https://www.youtube.com/@MirTankovOfficial",
    "Моды":             "https://koreanrandom.com/forum/forum/44-mods-and-software/",
}

EXCHANGE_RATES = (
    "Курс 250 золота к рублю: 55₽\n"
    "Курс 250 золота к доллару: 1$\n"
    "Курс 250 золота к тенге: 255₸\n"
    "Курс 250 золота к свободному опыту: 6250🌟"
)

HOROSCOPE_PHOTOS: dict[str, str] = {
    "♈️ОВЕН":     "https://sun9-78.userapi.com/impg/ThyFqEgB5VKINMfhVt6tQZDd_Oy-Ip00vb2qHA/6C7HBhKTBIQ.jpg?size=1280x1279&quality=95&sign=36a7a3239901c1464c1c8bfdf919abef&type=album",
    "♉️ТЕЛЕЦ":    "https://sun9-79.userapi.com/impg/fb_ZA_9bIBut2PsLIg7SQOqt9shjI4Exnj0qlw/8m9n5sbrOCI.jpg?size=1280x1279&quality=95&sign=83bad12cc4a3f87e82040cf1acc53500&type=album",
    "♊️БЛИЗНЕЦЫ": "https://sun9-43.userapi.com/impg/2ItUsx8iqg0oieqhbP7DLUoQpNbgb0efms4VKw/8dwGHlMQAaI.jpg?size=1280x1279&quality=95&sign=26df12427da65386f151e3e0164b561a&type=album",
    "♋️РАК":      "https://sun9-25.userapi.com/impg/IVcxKHd2KdXYfyswMnj758xivjaCTN582yqzpw/83LEFrhTPgQ.jpg?size=1280x1279&quality=95&sign=cd55e4284035b3143699eb691caa2129&type=album",
    "♌️ЛЕВ":      "https://sun9-48.userapi.com/impg/z0nTp4iLS-V3mOMh67wJ3KW_wBrI3uE9ZFn6YA/VEFC7H6iVV0.jpg?size=1280x1279&quality=95&sign=11459e3f6c7027958413992b78ee6d34&type=album",
    "♍️ДЕВА":     "https://sun9-66.userapi.com/impg/mFS9d-5BvuxuQsDmrOLohZOwUkZQdtQuJZFs-Q/C5FcuzMnnF8.jpg?size=1280x1279&quality=95&sign=c3abeb990ec9a4dd69651533a303dda9&type=album",
    "♎️ВЕСЫ":     "https://sun9-75.userapi.com/impg/qcyUGatP5vLUcYCxc8TR1FsXFkWo7O5GGBZrng/Ct_tVLOYric.jpg?size=1280x1279&quality=95&sign=840d387f492fe2ec19a458cbaaaa670e&type=album",
    "♏️СКОРПИОН": "https://sun9-26.userapi.com/impg/hl6bSjAKreKsst59qd59k58m0tspiKU2UPETxw/VlwbaxPlNUw.jpg?size=1280x1279&quality=95&sign=14c6fb52d380144ef310f469dba34c4b&type=album",
    "♐️СТРЕЛЕЦ":  "https://sun9-11.userapi.com/impg/5RvTx5bQAPHxyMjKB7g8bN3MQKU7Xb_vCzivLQ/9-WQRt8GhZI.jpg?size=1280x1279&quality=95&sign=ecca00a042be79164bdd74174d841faa&type=album",
    "♑️КОЗЕРОГ":  "https://sun9-16.userapi.com/impg/bLzRRvyzwZr3v87JH1c1fI1S_kKZ7alRbUn6gw/54NO16sRZSg.jpg?size=1280x1279&quality=95&sign=80bc0de18491ab8dc92d30921218ff09&type=album",
    "♒️ВОДОЛЕЙ":  "https://sun9-26.userapi.com/impg/ftrqNcYDv_zFejYo_rSY353Ml8lQg--AR7uC8w/Of-cmQ0CYj4.jpg?size=1280x1279&quality=95&sign=b65639c1a6cec7132e3439f7964b14f4&type=album",
    "♓️РЫБЫ":     "https://sun9-42.userapi.com/impg/dq1MqZKwlRzXLCxCDMi8i47e0JnK6dTlEk2InQ/XdO4qs79DlU.jpg?size=1280x1279&quality=95&sign=9e6c11f932652f44b2b8b19df4560e7d&type=album",
}

# ──────────────────────────────────────────────
# Вспомогательные функции
# ──────────────────────────────────────────────
def get_ekb_time() -> str:
    try:
        response = requests.get("https://time-in.ru", timeout=5)
        soup = bs4.BeautifulSoup(response.text, "html.parser")
        items = soup.select(".time-city-time-value")
        return items[0].get_text(strip=True) if items else "неизвестно"
    except requests.RequestException:
        return "неизвестно"


def get_wiki_summary(query: str) -> str:
    try:
        page = wikipedia.page(query)
        raw = page.content[:1000]
        sentences = raw.split(".")
        result = ""
        for sentence in sentences[:-1]:
            if "==" in sentence:
                break
            if len(sentence.strip()) > 3:
                result += sentence + "."
        result = re.sub(r"\([^()]*\)", "", result)
        result = re.sub(r"\([^()]*\)", "", result)
        result = re.sub(r"\{[^{}]*\}", "", result)
        return result.strip() or "❌ Ничего не найдено ❌"
    except Exception:
        return "❌ В энциклопедии нет информации об этом ❌"


# ──────────────────────────────────────────────
# Диалоги (lambda позволяет вызывать функции лениво)
# ──────────────────────────────────────────────
DIALOGS: list = [
    "👋 Здравствуй! Что будем делать?",
    "😃 Привет! Чем займёмся?",
    lambda: f"Уже {get_ekb_time()}. Какие на сегодня планы?",
    "Не забыл про Табель-календарь? Вот переходи: https://tanki.su/ru/daily-check-in/",
    "Я новенький бот, так что извини — многое ещё не умею!",
]


def get_greeting() -> str:
    entry = random.choice(DIALOGS)
    text = entry() if callable(entry) else entry
    return text + "\nМои возможности => /help"


# ──────────────────────────────────────────────
# Клавиатуры
# ──────────────────────────────────────────────
MAIN_KB = types.ReplyKeyboardMarkup(resize_keyboard=True)
MAIN_KB.row("/Курс", "/Время", "/Гороскоп", "/Погода", "/Новости")
MAIN_KB.row("/Мемы", "/Танкопедия", "/Рандом", "/Полезные_ссылки")


def make_horoscope_keyboard() -> types.ReplyKeyboardMarkup:
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("♈️ОВЕН", "♉️ТЕЛЕЦ", "♊️БЛИЗНЕЦЫ")
    kb.row("♋️РАК", "♌️ЛЕВ", "♍️ДЕВА", "♎️ВЕСЫ")
    kb.row("♏️СКОРПИОН", "♐️СТРЕЛЕЦ")
    kb.row("♑️КОЗЕРОГ", "♒️ВОДОЛЕЙ", "♓️РЫБЫ")
    return kb


# ──────────────────────────────────────────────
# Обработчики команд
# ──────────────────────────────────────────────
@bot.message_handler(commands=["start"])
def cmd_start(message: types.Message) -> None:
    bot.reply_to(message, get_greeting(), reply_markup=MAIN_KB)


@bot.message_handler(commands=["help"])
def cmd_help(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        (
            "Вот что я могу:\n"
            "1) Показывать гороскоп 🔮\n"
            "2) Закидывать тебя танковыми мемами\n"
            "3) Показывать точное время ⏱\n"
            "4) Знаю курс танковых валют 💰\n"
            "5) Предскажу погоду 😁\n"
            "6) Покажу характеристики техники в Танкопедии 🔧\n"
            "7) На всё остальное найду в Википедии"
        ),
        reply_markup=MAIN_KB,
    )


@bot.message_handler(commands=["Мемы"])
def cmd_memes(message: types.Message) -> None:
    mem_id = random.randint(291000, 309907)
    url = f"https://vk.com/albums-43135804?z=photo-43135804_457{mem_id}%2Fphotos-43135804"
    bot.send_photo(message.chat.id, url, reply_markup=MAIN_KB)


@bot.message_handler(commands=["Новости"])
def cmd_news(message: types.Message) -> None:
    post_id = random.randint(700, 766)
    url = f"https://t.me/mirtankov_leaks/1{post_id}"
    bot.send_message(message.chat.id, url, reply_markup=MAIN_KB)


@bot.message_handler(commands=["Время"])
def cmd_time(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        f"Точное время в Екатеринбурге: {get_ekb_time()}",
        reply_markup=MAIN_KB,
    )


@bot.message_handler(commands=["Погода"])
def cmd_weather(message: types.Message) -> None:
    bot.send_message(message.chat.id, "⚙️ Модуль погоды временно недоступен.", reply_markup=MAIN_KB)


@bot.message_handler(commands=["Курс"])
def cmd_kurs(message: types.Message) -> None:
    bot.send_message(message.chat.id, EXCHANGE_RATES, reply_markup=MAIN_KB)


@bot.message_handler(commands=["Рандом"])
def cmd_random(message: types.Message) -> None:
    bot.send_dice(message.chat.id, "🎲", reply_markup=MAIN_KB)


# ── Полезные ссылки ──
@bot.message_handler(commands=["Полезные_ссылки"])
def cmd_useful_links(message: types.Message) -> None:
    kb = types.InlineKeyboardMarkup()
    for label, url in USEFUL_LINKS.items():
        kb.add(types.InlineKeyboardButton(label, url=url))
    bot.send_message(message.chat.id, "Куда ты хочешь попасть?", reply_markup=kb)


# ── Гороскоп ──
@bot.message_handler(commands=["Гороскоп"])
def cmd_horoscope(message: types.Message) -> None:
    bot.send_message(
        message.chat.id,
        "Выбери свой знак зодиака:",
        reply_markup=make_horoscope_keyboard(),
    )


# ── Танкопедия: выбор страны ──
@bot.message_handler(commands=["Танкопедия"])
def cmd_tankopedia(message: types.Message) -> None:
    kb = types.InlineKeyboardMarkup()
    for country in TANKS:
        kb.add(types.InlineKeyboardButton(country, callback_data=f"tank_country_{country}"))
    bot.send_message(message.chat.id, "Выбери страну:", reply_markup=kb)


# ── Танкопедия: callback — страна выбрана, показать танки ──
@bot.callback_query_handler(func=lambda call: call.data.startswith("tank_country_"))
def cb_tank_country(call: types.CallbackQuery) -> None:
    country = call.data.split("tank_country_", 1)[1]
    tanks_in_country = TANKS.get(country, {})

    kb = types.InlineKeyboardMarkup()
    for tank_name in tanks_in_country:
        safe_name = tank_name.lstrip("/")
        kb.add(types.InlineKeyboardButton(tank_name, callback_data=f"tank_{safe_name}"))

    bot.answer_callback_query(call.id)
    bot.send_message(call.message.chat.id, f"Танки {country}:", reply_markup=kb)


# ── Танкопедия: callback — конкретный танк ──
@bot.callback_query_handler(func=lambda call: call.data.startswith("tank_") and not call.data.startswith("tank_country_"))
def cb_tank_info(call: types.CallbackQuery) -> None:
    safe_name = call.data.split("tank_", 1)[1]
    tank_name = "/" + safe_name

    # Ищем танк по всем странам
    tank = None
    for country_tanks in TANKS.values():
        if tank_name in country_tanks:
            tank = country_tanks[tank_name]
            break

    bot.answer_callback_query(call.id)
    if not tank:
        bot.send_message(call.message.chat.id, "Танк не найден.", reply_markup=MAIN_KB)
        return

    bot.send_photo(call.message.chat.id, tank["photo"], reply_markup=MAIN_KB)
    bot.send_message(call.message.chat.id, tank["info"] + TANK_STATS_FOOTER, reply_markup=MAIN_KB)


# ──────────────────────────────────────────────
# Fallback: гороскоп по тексту кнопки или Википедия
# ──────────────────────────────────────────────
@bot.message_handler(func=lambda m: True)
def handle_text(message: types.Message) -> None:
    text = message.text or ""

    # Гороскоп — текстовые кнопки (не команды)
    for sign, photo_url in HOROSCOPE_PHOTOS.items():
        if text == sign:
            bot.send_photo(message.chat.id, photo_url, reply_markup=MAIN_KB)
            return

    # Неизвестная команда
    if text.startswith("/"):
        bot.send_message(message.chat.id, "Неизвестная команда. Смотри /help", reply_markup=MAIN_KB)
        return

    # Всё остальное — в Википедию
    bot.send_message(message.chat.id, get_wiki_summary(text), reply_markup=MAIN_KB)


# ──────────────────────────────────────────────
# Запуск
# ──────────────────────────────────────────────
if __name__ == "__main__":
    bot.infinity_polling(none_stop=True)
