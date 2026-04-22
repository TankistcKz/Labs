#Импортируем библиотеки
import telebot, wikipedia, re, bs4, requests, random
from telebot import types, apihelper
#from pyowm import OWM
#from pyowm.utils.config import get_default_config
#from pyowm.utils import timestamps
import os

bot = telebot.TeleBot("6081528871:AAHwyaMuWdD3T02wKyeRrNSTNCXvAQaCFWA", parse_mode=None)
wikipedia.set_lang("ru")

keyboard = types.ReplyKeyboardMarkup(True)
keyboard.row('/Курс', '/Время', '/Гороскоп', '/Погода', '/Новости')
keyboard.row('/Мемы', '/Танкопедия', '/Рандом', '/Полезные ссылки')

#Модуль погоды
#config_dict = get_default_config()
#config_dict['connection']['use_ssl'] = False
#config_dict['connection']['verify_ssl_serts'] = False
#config_dict['language'] = 'ru'
#owm = OWM('67190ffe259bb1f7068d5425e7aa5f99', config_dict)
#mgr = owm.weather_manager()

#Блок с функиями
def get_time():
        z=''
        s=requests.get('https://time-in.ru')
        b=bs4.BeautifulSoup(s.text, "html.parser")
        p=b.select('.time-city-time-value')
        for x in p:
            s=(x.getText().strip())
            z=z+s+'\n\n'
        if str(s)=='<Response [404]>':s='мне не известно.'
        return s

def dialogs():
    d = random.randint(1,5)
    if d == 1:
        s = '👋 \nЗдраствуй! Что будем делать?'
    elif d == 2:
        s = '😃 \nПривет! Чем займёмся?'
    elif d ==3:
        s = f'Уже {get_time()}. Какие на сегодня планы?'
    elif d ==4:
        s = f'Не забыл про Табель-календарь? Вот переходи: https://tanki.su/ru/daily-check-in/ '
    else:
        s = 'Я новенький бот, так что извени многое не умею!'
    s += '\nМои возможности => /help'
    return s

def get_weather(city):
    observation = mgr.weather_at_place(str(city))
    forecast=mgr.forecast_at_place(str(city),'3h')
    w = observation.weather
    t = w.temperature('celsius')["temp"]
    forecast_rain="не будет осадков"
    if forecast.will_have_snow() == True:
        forecast_rain="будут осадки☔️"
    s=f'Температура в городе {city}: {str(t)}°С'+'\n'+ f"На небе {w.detailed_status}"+'\n'+ f"В ближайшие 3 дня {forecast_rain}"
    return s

def getmem():
    try:
        mem = random.randint(291000, 309907)
        return f'https://vk.com/albums-43135804?z=photo-43135804_457{mem}%2Fphotos-43135804'
    
    except telebot.apihelper.ApiTelegramException:
        mem = random.randint(1000, 7171)
        print('Ошибка!!!')
        return f'https://vk.com/albums-43135804?z=photo-43135804_457{mem}%2Fphotos-43135804'

def getnew():
    new = random.randint(700, 766)
    return f'https://t.me/mirtankov_leaks/1{new}'

def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if(len((x.strip()))>3):
                   wikitext2=wikitext2+x+'.'
            else:
                break
        wikitext2 = re.sub(r'\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub(r'\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub(r'\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return '❌В энциклопедии нет информации об этом❌'

#Блок с командами
@bot.message_handler(commands=['start'])
def send_welcome(message):
 bot.reply_to(message, dialogs())

@bot.message_handler(content_types=['text', 'photo'])
def send_m(message):
    if (message.text in "/help"):   
        bot.send_message(message.chat.id, 'Вот что я могу:\n1)Показывать гороскоп🔮 \n2)Закидывать тебя танковыми мемами \n3)Показывать точное время⏱\
                        \n4)Знаю курс танковых валют💰 \n5)Предскажу погоду, чтобы ты наконец-то вышел на улицу😁 \n6)Покажу хар-ки техники в танкопедии🔧\
                        \n7)А на всё остальное постараюсь найти в Википедии', reply_markup=keyboard)
    elif (message.text in "/Мемы"):
        bot.send_photo(message.chat.id, getmem(), reply_markup=keyboard)
    elif (message.text in "/Новости"):
        bot.send_message(message.chat.id, getnew(), reply_markup=keyboard)
    elif (message.text in "/Время"):
        bot.send_message(message.chat.id,'Точное время в Екатеринбурге: '+get_time(),reply_markup=keyboard)
    elif ("/Погода" in message.text):
        #city=str(str(message.text)+' 1').split()[1]
        #if city=='1': city='Москва'
        bot.send_message(message.chat.id,'get_weather(city)' , reply_markup=keyboard)
    elif ("/Курс" in message.text):
        bot.send_message(message.chat.id, 'Курс 250 золота к рублю: 55₽\nКурс 250 золота к доллару: 1$\nКурс 250 золота к тенге: 255₸\n\
                         Курс 250 золота к свободному опыту: 6250🌟', reply_markup=keyboard)
    elif ("/Рандом" in message.text):
        bot.send_dice(message.chat.id,'🎲', reply_markup=keyboard)
#Ссылки
    elif ("/Полезные ссылки" in message.text):
        markups = types.ReplyKeyboardMarkup()
        s1 = types.KeyboardButton('/Официальный сайт Мира Танков')
        s2 = types.KeyboardButton('/Ютуб канал Мира Танков')
        s3 = types.KeyboardButton('/Моды')
        markups.row(s1)
        markups.row(s2)
        markups.row(s3)
        bot.send_message(message.chat.id,'Куды ты хочешь попасть?', reply_markup=markups)
    elif ("/Официальный сайт Мира Танков" in message.text):
        bot.send_message(message.chat.id, 'https://tanki.su/?new_layout=0', reply_markup=keyboard)
    elif ("/Ютуб канал Мира Танков" in message.text):
        bot.send_message(message.chat.id, 'https://www.youtube.com/@MirTankovOfficial', reply_markup=keyboard)
    elif ("/Моды" in message.text):
        bot.send_message(message.chat.id, 'https://koreanrandom.com/forum/forum/44-mods-and-software/', reply_markup=keyboard)
#Танкопедия
    elif ("/Танкопедия"in message.text):
        markupt = types.ReplyKeyboardMarkup()
        t1 = types.KeyboardButton('/CCCP')
        t2 = types.KeyboardButton('/Гермaния')
        t3 = types.KeyboardButton('/CША')
        markupt.row(t1, t2, t3)
        bot.send_message(message.chat.id, "Введи страну:", reply_markup=markupt)
    elif ("/CCCP"in message.text):
        markupt2 = types.ReplyKeyboardMarkup()
        t11 = types.KeyboardButton('/ИC-7')
        t12 = types.KeyboardButton('/T-62')
        t13 = types.KeyboardButton('/Oб.268')
        markupt2.row(t11, t12, t13)
        bot.send_message(message.chat.id, "Введи танк СССР:", reply_markup=markupt2)
    elif ("/ИC-7" in message.text):
        bot.send_photo(message.chat.id,'https://i.pinimg.com/originals/9f/62/b0/9f62b0009b9a7982b2ce348e905f1a79.png', reply_markup=keyboard)
        bot.send_message(message.chat.id, "ИС-7 Тяжёлый танк прорыва\
                        \nРабота над танком началась весной 1945 года. Прототипы испытывались в 1946 и 1947 гг. В 1948 г. прошёл госиспытания. Серийно не выпускался.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n490 / 490 / 640 ед.\
                        \nБронепробиваемость:\
                        \n250 / 303 / 68 мм\
                        \nВремя перезарядки орудия:\
                        \n13,70 с\
                        \nСкорострельность:\
                        \n4,38 выстр/мин\
                        \nУрон в минуту:\
                        \n2 145 ед/мин\
                        \nУВН:\
                        \n-6/18\
                        \nВремя сведения:\
                        \n2,90 с\
                        \nРазброс на 100 м:\
                        \n0,40 м\
                        \nБоезапас:\
                        \n30 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n68,19 / 70,95 т\
                        \nМощность двигателя:\
                        \n1 200 л.с.\
                        \nУдельная мощность:\
                        \n17,60 л.с./т\
                        \nМаксимальная скорость:\
                        \n59,60 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n28/25 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n2 400 ед.\
                        \nБронирование корпуса:\
                        \n150 / 150 / 100 мм\
                        \nБронирование башни:\
                        \n240 / 185 / 94 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n400 м/720 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/T-62" in message.text):
        bot.send_photo(message.chat.id,'https://glossary-na-static.gcdn.co/icons/wotb/current/uploaded/vehicles/hd/T62A.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"Т-62 Средний танк универсальный\
                        \nРазработка среднего танка первого послевоенного поколения началась в 1951 году.Однако в марте 1962 года было принято решение не начинать серийное производство Т-62А.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n360 / 360 / 440 ед.\
                        \nБронепробиваемость:\
                        \n264 / 330 / 50 мм\
                        \nВремя перезарядки орудия:\
                        \n7,01 с\
                        \nСкорострельность:\
                        \n8,56 выстр/мин\
                        \nУрон в минуту:\
                        \n3 081 ед/мин\
                        \nУВН:\
                        \n-5/17\
                        \nВремя сведения:\
                        \n2 с\
                        \nРазброс на 100 м:\
                        \n0,32 м\
                        \nБоезапас:\
                        \n50 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n37 / 39,80 т\
                        \nМощность двигателя:\
                        \n750 л.с.\
                        \nУдельная мощность:\
                        \n20,27 л.с./т\
                        \nМаксимальная скорость:\
                        \n57 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n56/48 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n1 950 ед.\
                        \nБронирование корпуса:\
                        \n100 / 80 / 45 мм\
                        \nБронирование башни:\
                        \n240 / 161 / 65 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n400 м/850 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/Oб.268" in message.text):
        bot.send_photo(message.chat.id,'https://glossary-na-static.gcdn.co/icons/wotb/current/uploaded/vehicles/hd/Object268.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"Объект 268 ПТ-САУ универсальная\
                        \nРаботы над машиной были начаты летом 1952 года. Установка разрабатывалась на шасси тяжёлого танка Т-10.Опытный образец был изготовлен в 1956 году. Машина прошла испытания, но серийно не выпускалась.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ \
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n750 / 750 / 1 100 ед\
                        \nБронепробиваемость:\
                        \n303 / 395 / 90 мм\
                        \nВремя перезарядки орудия:\
                        \n16,5 с\
                        \nСкорострельность:\
                        \n3,64 выстр/мин\
                        \nУрон в минуту:\
                        \n2 727 ед/мин\
                        \nУВН:\
                        \n-5/15\
                        \nУГН:\
                        \n-11/11\
                        \nВремя сведения:\
                        \n2,70 с\
                        \nРазброс на 100 м:\
                        \n0,33 м\
                        \nБоезапас:\
                        \n35 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n50,97 / 53,90 т\
                        \nМощность двигателя:\
                        \n800 л.с.\
                        \nУдельная мощность:\
                        \n15,69 л.с./т\
                        \nМаксимальная скорость:\
                        \n48 км/ч\
                        \nСкорость поворота корпуса/горизонт.наведения:\
                        \n28/26 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n1 950 ед.\
                        \nБронирование корпуса:\
                        \n187 / 100 / 50 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n370 м/730 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/Гермaния"in message.text):
        markupt3 = types.ReplyKeyboardMarkup()
        t21 = types.KeyboardButton('/МАUS')
        t22 = types.KeyboardButton('/Lеоpаrd 1')
        t23 = types.KeyboardButton('/Wаffеnträgеr аuf Е100')
        markupt3.row(t21, t22, t23)
        bot.send_message(message.chat.id, "Введи танк Германии:", reply_markup=markupt3)
    elif ("/МАUS" in message.text):
        bot.send_photo(message.chat.id,'https://avatars.mds.yandex.net/i?id=572b48a90b37d40951a70f94ca20a541552a55ab-10918338-images-thumbs&n=13', reply_markup=keyboard)
        bot.send_message(message.chat.id,"MAUS Тяжёлый танк штурмовой\
                        \nРазрабатывался с июня 1942 по июль 1944 года. Было изготовлено два прототипа, из которых только один получил башню с вооружением.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n490 / 490 / 630 ед.\
                        \nБронепробиваемость:\
                        \n246 / 311 / 65 мм\
                        \nВремя перезарядки орудия:\
                        \n13,30 с\
                        \nСкорострельность:\
                        \n4,51 выстр/мин\
                        \nУрон в минуту:\
                        \n2 210 ед/мин\
                        \nУВН:\
                        \n-8/24\
                        \nВремя сведения:\
                        \n2,10 с\
                        \nРазброс на 100 м:\
                        \n0,36 м\
                        \nБоезапас:\
                        \n68 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n188,98 / 192,90 т\
                        \nМощность двигателя:\
                        \n1 750 л.с.\
                        \nУдельная мощность:\
                        \n9,26 л.с./т\
                        \nМаксимальная скорость:\
                        \n20 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n15/16 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n3 000 ед.\
                        \nБронирование корпуса:\
                        \n200 / 185 / 160 мм\
                        \nБронирование башни:\
                        \n260 / 210 / 210 мм\
                        \nВремя ремонта ходовой:\
                        \n14,04 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n400 м/720 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/Lеоpаrd 1" in message.text):
        bot.send_photo(message.chat.id,'https://www.digiseller.ru/preview/284308/p1_3106922_87ce7e44.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"Leopard 1 Средний танк снайперский\
                        \nОсновной боевой танк ФРГ. Работы по созданию машины начались в 1956 году. Первые опытные образцы были построены в 1965 году на заводе Krauss-Maffei. Состоял на вооружении более чем в 10 странах мира.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n420 / 420 / 510 ед.\
                        \nБронепробиваемость:\
                        \n278 / 323 / 105 мм\
                        \nВремя перезарядки орудия:\
                        \n9,30 с\
                        \nСкорострельность:\
                        \n6,45 выстр/мин\
                        \nУрон в минуту:\
                        \n2 709 ед/мин\
                        \nУВН:\
                        \n-9/20\
                        \nВремя сведения:\
                        \n1,70 с\
                        \nРазброс на 100 м:\
                        \n0,29 м\
                        \nБоезапас:\
                        \n60 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n40 / 42 т\
                        \nМощность двигателя:\
                        \n830 л.с.\
                        \nУдельная мощность:\
                        \n20,75 л.с./т\
                        \nМаксимальная скорость:\
                        \n70 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n50/40 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n1 850 ед.\
                        \nБронирование корпуса:\
                        \n70 / 35 / 25 мм\
                        \nБронирование башни:\
                        \n52 / 60 / 60 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n410 м/750 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/Wаffеnträgеr аuf Е100" in message.text):
        bot.send_photo(message.chat.id,'https://avatars.dzeninfra.ru/get-zen_doc/3765046/pub_604e38b9af41a36641449f79_604e3cd8126a3d455accd3ea/scale_1200', reply_markup=keyboard)
        bot.send_message(message.chat.id,"Wаffеnträgеr аuf Е100 ПТ-САУ поддержки\
                        \nМашина Waffenträger auf E 100 выдуманная, хотя орудие существовало, корпус E 100 тоже был в металле.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n490 / 490 / 630 ед.\
                        \nБронепробиваемость:\
                        \n246 / 311 / 65 мм\
                        \nСнарядов в магазине:\
                        \n5 шт\
                        \nВремя перезарядки/смены снаряда в магазине:\
                        \n58/2 с\
                        \nСкорострельность:\
                        \n5,55 выстр/мин\
                        \nУрон в минуту:\
                        \n2 270 ед/мин\
                        \nУВН:\
                        \n-5/15\
                        \nВремя сведения:\
                        \n1,5 с\
                        \nРазброс на 100 м:\
                        \n0,29 м\
                        \nБоезапас:\
                        \n60 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса:\
                        \n94,7 т\
                        \nМощность двигателя:\
                        \n840 л.с.\
                        \nУдельная мощность:\
                        \n8,87 л.с./т\
                        \nМаксимальная скорость:\
                        \n40 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n26/22 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n2 000 ед.\
                        \nБронирование корпуса:\
                        \n80 / 50 / 40 мм\
                        \nБронирование башни:\
                        \n20 / 10 / 8 мм\
                        \nВремя ремонта ходовой:\
                        \n14,04 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n380 м/720 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/CША"in message.text):
        markupt4 = types.ReplyKeyboardMarkup()
        t31 = types.KeyboardButton('/Т57 HЕАVY')
        t32 = types.KeyboardButton('/М48A5 РАTTОN')
        t33 = types.KeyboardButton('/T110Е3')
        markupt4.row(t31, t32, t33)
        bot.send_message(message.chat.id, "Введи танк США:", reply_markup=markupt4)
    elif ("/Т57 HЕАVY" in message.text):
        bot.send_photo(message.chat.id,'https://glossary-na-static.gcdn.co/icons/wotb/current/uploaded/vehicles/hd/T57_58.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"T57 HEAVY TANK Тяжёлый танк поддержки\
                        \nРазрабатывался с 1951 года. К 1957 году были изготовлены опытные башни под 120-мм и 155-мм орудия, однако программа создания таких машин была признана бесперспективной, и все работы были свёрнуты.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n400 / 400 / 515 ед.\
                        \nБронепробиваемость:\
                        \n258 / 340 / 60 мм\
                        \nСнарядов в магазине:\
                        \n4 шт\
                        \nВремя перезарядки/смены снаряда в магазине:\
                        \n25/2 с\
                        \nСкорострельность:\
                        \n7,74 выстр/мин\
                        \nУрон в минуту:\
                        \n3 096 ед/мин\
                        \nУВН:\
                        \n-8/12\
                        \nВремя сведения:\
                        \n2,70 с\
                        \nРазброс на 100 м:\
                        \n0,35 м\
                        \nБоезапас:\
                        \n36 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n54,43 / 58 т\
                        \nМощность двигателя:\
                        \n810 л.с.\
                        \nУдельная мощность:\
                        \n14,88 л.с./т\
                        \nМаксимальная скорость:\
                        \n35,40 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n30/36 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n2 250 ед.\
                        \nБронирование корпуса:\
                        \n228 / 44 / 44 мм\
                        \nБронирование башни:\
                        \n152 / 127 / 50 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n400 м/745 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/М48A5 РАTTОN" in message.text):
        bot.send_photo(message.chat.id,'https://glossary-na-static.gcdn.co/icons/wotb/current/uploaded/vehicles/hd/M48A1.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"M48A5 PATTON Средний танк универсальный\
                        \nМодификация танка М48 образца 1970 года, разработанная в целях модернизации оставшейся на вооружении модели M48 до уровня танка M60. Отличается установкой нового двигателя, вооружения, СУО.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n390 / 390 / 480 ед.\
                        \nБронепробиваемость:\
                        \n268 / 330 / 53 мм\
                        \nВремя перезарядки орудия:\
                        \n8,35 с\
                        \nСкорострельность:\
                        \n7,19 выстр/мин\
                        \nУрон в минуту:\
                        \n2 802 ед/мин\
                        \nУВН:\
                        \n-9/19\
                        \nВремя сведения:\
                        \n1,90 с\
                        \nРазброс на 100 м:\
                        \n0,36 м\
                        \nБоезапас:\
                        \n57 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n47,72 / 50,35 т\
                        \nМощность двигателя:\
                        \n810 л.с.\
                        \nУдельная мощность:\
                        \n16,97 л.с./т\
                        \nМаксимальная скорость:\
                        \n45 км/ч\
                        \nСкорость поворота корпуса/башни:\
                        \n50/40 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n2 000 ед.\
                        \nБронирование корпуса:\
                        \n152 / 76 / 25 мм\
                        \nБронирование башни:\
                        \n254 / 76 / 50 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n420 м/745 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
    elif ("/T110Е3" in message.text):
        bot.send_photo(message.chat.id,'https://wxpcdn-cbprodretail.gcdn.co/dcont/tankopedia/usa/A85_T110E3.png', reply_markup=keyboard)
        bot.send_message(message.chat.id,"T110E3 ПТ-САУ Штурмовая\
                        \nВ 1954 году на базе одного из проектов TS-31 компания Chrysler Corporation предложила разработать новый тяжёлый танк. После проработки нескольких вариантов конструкции работы над танком были прекращены.\
                        \n\
                        \nТЕХНИЧЕСКИЕ ХАРАКТЕРИСТИКИ\
                        \n🗡ОГНЕВАЯ МОЩЬ\
                        \nУрон:\
                        \n750 / 750 / 1 100 ед.\
                        \nБронепробиваемость:\
                        \n295 / 375 / 90 мм\
                        \nВремя перезарядки орудия:\
                        \n18 с\
                        \nСкорострельность:\
                        \n3,33 выстр/мин\
                        \nУрон в минуту:\
                        \n2 500 ед/мин\
                        \nУВН:\
                        \n-8/16\
                        \nУГН:\
                        \n-8/8\
                        \nВремя сведения:\
                        \n2,70 с\
                        \nРазброс на 100 м:\
                        \n0,36 м\
                        \nБоезапас:\
                        \n27 шт\
                        \n\
                        \n⏱МОБИЛЬНОСТЬ\
                        \nМасса/Предельная масса:\
                        \n74,73 / 78 т\
                        \nМощность двигателя:\
                        \n875 л.с.\
                        \nУдельная мощность:\
                        \n11,71 л.с./т\
                        \nМаксимальная скорость:\
                        \n24 км/ч\
                        \nСкорость поворота корпуса/горизонт. наведения:\
                        \n24/26 град/с\
                        \n\
                        \n🛡ЖИВУЧЕСТЬ\
                        \nПрочность:\
                        \n1 950 ед.\
                        \nБронирование корпуса:\
                        \n305 / 76 / 38 мм\
                        \nВремя ремонта ходовой:\
                        \n12,03 с\
                        \n\
                        \n🔭НАБЛЮДЕНИЕ\
                        \nОбзор/Дальность связи:\
                        \n370 м/745 м\
\nТехнические характеристики указаны для техники с уровнем обучения экипажа 100%.", reply_markup=keyboard)
#Гороскоп
    elif ("/Гороскоп" in message.text):
        markup = types.ReplyKeyboardMarkup()
        g1 = types.KeyboardButton('♈️ОВЕН')
        g2 = types.KeyboardButton('♉️ТЕЛЕЦ')
        g3 = types.KeyboardButton('♊️БЛИЗНЕЦЫ')
        g4 = types.KeyboardButton('♋️РАК')
        g5 = types.KeyboardButton('♌️ЛЕВ')
        g6 = types.KeyboardButton('♍️ДЕВА')
        g7 = types.KeyboardButton('♎️ВЕСЫ')
        g8 = types.KeyboardButton('♏️СКОРПИОН')
        g9 = types.KeyboardButton('♐️СТРЕЛЕЦ')
        g10 = types.KeyboardButton('♑️КОЗЕРОГ')
        g11 = types.KeyboardButton('♒️ВОДОЛЕЙ')
        g12 = types.KeyboardButton('♓️РЫБЫ')
        markup.row(g1, g2, g3)
        markup.row(g4, g5, g6, g7)
        markup.row(g8, g9)
        markup.row(g10, g11, g12)
        bot.send_message(message.chat.id, "Введи свой знак задиака:", reply_markup=markup)
    elif ("♈️ОВЕН" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-78.userapi.com/impg/ThyFqEgB5VKINMfhVt6tQZDd_Oy-Ip00vb2qHA/6C7HBhKTBIQ.jpg?size=1280x1279&quality=95&sign=36a7a3239901c1464c1c8bfdf919abef&type=album', reply_markup=keyboard)
    elif ("♉️ТЕЛЕЦ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-79.userapi.com/impg/fb_ZA_9bIBut2PsLIg7SQOqt9shjI4Exnj0qlw/8m9n5sbrOCI.jpg?size=1280x1279&quality=95&sign=83bad12cc4a3f87e82040cf1acc53500&type=album', reply_markup=keyboard)
    elif ("♊️БЛИЗНЕЦЫ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-43.userapi.com/impg/2ItUsx8iqg0oieqhbP7DLUoQpNbgb0efms4VKw/8dwGHlMQAaI.jpg?size=1280x1279&quality=95&sign=26df12427da65386f151e3e0164b561a&type=album', reply_markup=keyboard)
    elif ("♋️РАК" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-25.userapi.com/impg/IVcxKHd2KdXYfyswMnj758xivjaCTN582yqzpw/83LEFrhTPgQ.jpg?size=1280x1279&quality=95&sign=cd55e4284035b3143699eb691caa2129&type=album', reply_markup=keyboard)
    elif ("♌️ЛЕВ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-48.userapi.com/impg/z0nTp4iLS-V3mOMh67wJ3KW_wBrI3uE9ZFn6YA/VEFC7H6iVV0.jpg?size=1280x1279&quality=95&sign=11459e3f6c7027958413992b78ee6d34&type=album', reply_markup=keyboard)
    elif ("♍️ДЕВА" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-66.userapi.com/impg/mFS9d-5BvuxuQsDmrOLohZOwUkZQdtQuJZFs-Q/C5FcuzMnnF8.jpg?size=1280x1279&quality=95&sign=c3abeb990ec9a4dd69651533a303dda9&type=album', reply_markup=keyboard)
    elif ("♎️ВЕСЫ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-75.userapi.com/impg/qcyUGatP5vLUcYCxc8TR1FsXFkWo7O5GGBZrng/Ct_tVLOYric.jpg?size=1280x1279&quality=95&sign=840d387f492fe2ec19a458cbaaaa670e&type=album', reply_markup=keyboard)
    elif ("♏️СКОРПИОН" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-26.userapi.com/impg/hl6bSjAKreKsst59qd59k58m0tspiKU2UPETxw/VlwbaxPlNUw.jpg?size=1280x1279&quality=95&sign=14c6fb52d380144ef310f469dba34c4b&type=album', reply_markup=keyboard)
    elif ("♐️СТРЕЛЕЦ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-11.userapi.com/impg/5RvTx5bQAPHxyMjKB7g8bN3MQKU7Xb_vCzivLQ/9-WQRt8GhZI.jpg?size=1280x1279&quality=95&sign=ecca00a042be79164bdd74174d841faa&type=album', reply_markup=keyboard)
    elif ("♑️КОЗЕРОГ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-16.userapi.com/impg/bLzRRvyzwZr3v87JH1c1fI1S_kKZ7alRbUn6gw/54NO16sRZSg.jpg?size=1280x1279&quality=95&sign=80bc0de18491ab8dc92d30921218ff09&type=album', reply_markup=keyboard)
    elif ("♒️ВОДОЛЕЙ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-26.userapi.com/impg/ftrqNcYDv_zFejYo_rSY353Ml8lQg--AR7uC8w/Of-cmQ0CYj4.jpg?size=1280x1279&quality=95&sign=b65639c1a6cec7132e3439f7964b14f4&type=album', reply_markup=keyboard)
    elif ("♓️РЫБЫ" in message.text):
        bot.send_photo(message.chat.id,'https://sun9-42.userapi.com/impg/dq1MqZKwlRzXLCxCDMi8i47e0JnK6dTlEk2InQ/XdO4qs79DlU.jpg?size=1280x1279&quality=95&sign=9e6c11f932652f44b2b8b19df4560e7d&type=album', reply_markup=keyboard)
#Википедия
    else:
        bot.send_message(message.chat.id,getwiki(str(message.text)))
bot.infinity_polling (none_stop = True)