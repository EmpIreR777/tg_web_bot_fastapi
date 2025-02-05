# Парикмахерская

Добро пожаловать в проект "Парикмахерская"! Это веб-приложение с интеграцией Telegram-бота, которое позволяет пользователям записываться на услуги, просматривать свои заявки и предоставлять администраторам возможность управлять записями.

## Установка

### Требования

Убедитесь, что у вас установлены следующие компоненты:

- Python 3.8 или выше
- Aiogram 3.0


### Первоначальная настройка

1. Клонируйте репозиторий:

      ```git@github.com:EmpIreR777/tg_web_bot_fastapi.git```

   

2. Установите зависимости:

      ```pip install -r requirements.txt```
   

3. Создайте файл конфигурации .env в корне проекта. Пример содержания:


4. Настройте базу данных. Убедитесь, что вы используете контроль версий (например, с помощью Alembic), чтобы задать и настроить ваши таблицы.

## Запуск приложения

### Запуск сервера FastAPI

Для запуска сервера выполните команду:

uvicorn app.main:app --reload


Сервер будет доступен по адресу http://127.0.0.1:8000.

### Запуск Telegram-бота

Запуск Telegram-бота осуществляется через другой файл или модуль в проекте. Убедитесь, что код инициализации бота корректно реализован.

## Использование приложения

1. Запись на услуги:
   - Пользователь может оставить заявку на нужную услугу.
   - Заполните форму, выберите мастера, услугу и введите свои данные.

2. Просмотр заявок:
   - Пользователь может просмотреть свои ранее оставленные заявки в разделе "Мои заявки".

3. Административная панель:
   - Администраторы могут управлять всеми заявками и просматривать детали каждого запроса.

## Архитектура проекта

- Файлы и директории:
  - app/: Основная директория проекта.
    - api/: Обработчики API и схемы данных.
    - bot/: Код инициализации бота Telegram.
    - config/: Конфигурационные файлы.
    - dao/: Data Access Object для взаимодействия с базой данных.
    - templates/: HTML-шаблоны для рендеринга.
    - main.py: Основной файл приложения.

## Технологии

- FastAPI: Для создания веб-приложения и API.
- SQLAlchemy: Для работы с базой данных.
- Aiogram: Библиотека для создания Telegram-ботов.
- Jinja2: Шаблонизатор для HTML.



