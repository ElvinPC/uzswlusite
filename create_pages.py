import requests

# Django API endpoint
BASE_URL = "http://127.0.0.1:8000/pages/"

# Asosiy sahifalar (parent)
pages = [
    # Uzbek
    {"title": "Bosh sahifa", "lang": 1, "sub": None, "url": "home-uz", "position": 1, "dic": "Saytning bosh sahifasi"},
    {"title": "Biz haqimizda", "lang": 1, "sub": None, "url": "about-uz", "position": 2, "dic": "Universitet haqida ma'lumot"},
    {"title": "Fakultetlar", "lang": 1, "sub": None, "url": "fakultetlar-uz", "position": 3, "dic": "Universitet fakultetlari"},
    {"title": "Yangiliklar", "lang": 1, "sub": None, "url": "yangiliklar-uz", "position": 4, "dic": "Universitet yangiliklari"},

    # Russian
    {"title": "Главная страница", "lang": 2, "sub": None, "url": "home-ru", "position": 1, "dic": "Главная страница сайта"},
    {"title": "О нас", "lang": 2, "sub": None, "url": "about-ru", "position": 2, "dic": "Информация об университете"},
    {"title": "Факультеты", "lang": 2, "sub": None, "url": "fakultety-ru", "position": 3, "dic": "Факультеты университета"},
    {"title": "Новости", "lang": 2, "sub": None, "url": "novosti-ru", "position": 4, "dic": "Новости университета"},

    # English
    {"title": "Home", "lang": 3, "sub": None, "url": "home-en", "position": 1, "dic": "Main page of the website"},
    {"title": "About us", "lang": 3, "sub": None, "url": "about-en", "position": 2, "dic": "Information about the university"},
    {"title": "Faculties", "lang": 3, "sub": None, "url": "faculties-en", "position": 3, "dic": "University faculties"},
    {"title": "News", "lang": 3, "sub": None, "url": "news-en", "position": 4, "dic": "University news"},
]

# Bolalar sahifalari (child)
children = [
    # UZ
    {"title": "Universitet haqida qisqacha", "lang": 1, "sub": 1, "url": "home-intro-uz", "position": 1, "dic": "Universitet haqida qisqacha"},
    {"title": "Bizning maqsadimiz", "lang": 1, "sub": 1, "url": "home-purpose-uz", "position": 2, "dic": "Bizning maqsadimiz"},
    {"title": "Kontaktlar", "lang": 1, "sub": 1, "url": "home-contact-uz", "position": 3, "dic": "Aloqa ma'lumotlari"},

    {"title": "Rahbariyat", "lang": 1, "sub": 2, "url": "about-rahbariyat-uz", "position": 1, "dic": "Rahbariyat"},
    {"title": "Tuzilma", "lang": 1, "sub": 2, "url": "about-structure-uz", "position": 2, "dic": "Tuzilma"},
    {"title": "Tariximiz", "lang": 1, "sub": 2, "url": "about-history-uz", "position": 3, "dic": "Tariximiz"},

    {"title": "Ingliz filologiyasi", "lang": 1, "sub": 3, "url": "faculty-english-uz", "position": 1, "dic": "Ingliz filologiyasi fakulteti"},
    {"title": "Tarix fakulteti", "lang": 1, "sub": 3, "url": "faculty-history-uz", "position": 2, "dic": "Tarix fakulteti"},
    {"title": "Jurnalistika fakulteti", "lang": 1, "sub": 3, "url": "faculty-journalism-uz", "position": 3, "dic": "Jurnalistika fakulteti"},

    {"title": "So‘nggi yangiliklar", "lang": 1, "sub": 4, "url": "news-latest-uz", "position": 1, "dic": "So‘nggi yangiliklar"},
    {"title": "E’lonlar", "lang": 1, "sub": 4, "url": "news-announcements-uz", "position": 2, "dic": "E’lonlar"},
    {"title": "Matbuot xizmati", "lang": 1, "sub": 4, "url": "news-press-uz", "position": 3, "dic": "Matbuot xizmati"},

    # RU
    {"title": "Кратко об университете", "lang": 2, "sub": 5, "url": "home-intro-ru", "position": 1, "dic": "Кратко об университете"},
    {"title": "Наша цель", "lang": 2, "sub": 5, "url": "home-purpose-ru", "position": 2, "dic": "Наша цель"},
    {"title": "Контакты", "lang": 2, "sub": 5, "url": "home-contact-ru", "position": 3, "dic": "Контакты"},

    {"title": "Руководство", "lang": 2, "sub": 6, "url": "about-rahbariyat-ru", "position": 1, "dic": "Руководство"},
    {"title": "Структура", "lang": 2, "sub": 6, "url": "about-structure-ru", "position": 2, "dic": "Структура"},
    {"title": "История", "lang": 2, "sub": 6, "url": "about-history-ru", "position": 3, "dic": "История"},

    {"title": "Факультет английской филологии", "lang": 2, "sub": 7, "url": "faculty-english-ru", "position": 1, "dic": "Факультет английской филологии"},
    {"title": "Факультет истории", "lang": 2, "sub": 7, "url": "faculty-history-ru", "position": 2, "dic": "Факультет истории"},
    {"title": "Факультет журналистики", "lang": 2, "sub": 7, "url": "faculty-journalism-ru", "position": 3, "dic": "Факультет журналистики"},

    {"title": "Последние новости", "lang": 2, "sub": 8, "url": "news-latest-ru", "position": 1, "dic": "Последние новости"},
    {"title": "Объявления", "lang": 2, "sub": 8, "url": "news-announcements-ru", "position": 2, "dic": "Объявления"},
    {"title": "Пресс-служба", "lang": 2, "sub": 8, "url": "news-press-ru", "position": 3, "dic": "Пресс-служба"},

    # EN
    {"title": "About the University", "lang": 3, "sub": 9, "url": "home-intro-en", "position": 1, "dic": "About the University"},
    {"title": "Our Mission", "lang": 3, "sub": 9, "url": "home-purpose-en", "position": 2, "dic": "Our Mission"},
    {"title": "Contacts", "lang": 3, "sub": 9, "url": "home-contact-en", "position": 3, "dic": "Contacts"},

    {"title": "Administration", "lang": 3, "sub": 10, "url": "about-rahbariyat-en", "position": 1, "dic": "Administration"},
    {"title": "Structure", "lang": 3, "sub": 10, "url": "about-structure-en", "position": 2, "dic": "Structure"},
    {"title": "Our History", "lang": 3, "sub": 10, "url": "about-history-en", "position": 3, "dic": "Our History"},

    {"title": "Faculty of English Philology", "lang": 3, "sub": 11, "url": "faculty-english-en", "position": 1, "dic": "Faculty of English Philology"},
    {"title": "Faculty of History", "lang": 3, "sub": 11, "url": "faculty-history-en", "position": 2, "dic": "Faculty of History"},
    {"title": "Faculty of Journalism", "lang": 3, "sub": 11, "url": "faculty-journalism-en", "position": 3, "dic": "Faculty of Journalism"},

    {"title": "Latest News", "lang": 3, "sub": 12, "url": "news-latest-en", "position": 1, "dic": "Latest News"},
    {"title": "Announcements", "lang": 3, "sub": 12, "url": "news-announcements-en", "position": 2, "dic": "Announcements"},
    {"title": "Press Service", "lang": 3, "sub": 12, "url": "news-press-en", "position": 3, "dic": "Press Service"},
]

def create_pages(data):
    for p in data:
        res = requests.post(BASE_URL, json=p)
        if res.status_code == 201:
            print(f"✅ Yaratildi: {p['title']}")
        else:
            print(f"❌ Xato ({res.status_code}): {p['title']} - {res.text}")

print("➡️ Asosiy sahifalar yaratilmoqda...")
create_pages(pages)

print("\n➡️ Bolalar sahifalar yaratilmoqda...")
create_pages(children)
