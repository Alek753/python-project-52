### Hexlet tests and linter status:
[![Actions Status](https://github.com/Alek753/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Alek753/python-project-52/actions)


# Проект 4: Менеджер задач (Task manager)
## Описание
Менеджер задач (Task manager) – это приложение на базе фреймворка Django, которое позволяет назначать задачи исполнителям и менять их статус. Для работы в приложении необходима регистрация.

### [Приложение на Render.com](https://python-project-52-oyvr.onrender.com)

## Системные требования
* Python 3.13
* Django 5.1.7
* PostgreSQL

## Установка

1. Клонировать репозиторий с GitHub:
   ```sh
   git clone https://github.com/Alek753/python-project-52
   ```

2. Перейти в директорию проекта.

3. Установить зависимости:
   ```sh
   make install
   ```

4. Создать базу данных для работы приложения:
   ```sh
    make migrate
   ```  

5. Создать в корне директории проекта файл '.env' и заполнить его следующим образом:
   ```sh
   SECRET_KEY=ваш_секретный_ключ
   ```

6. Чтобы запустить приложение в режиме разработки:
   ```sh
   make dev
   ```

5. Чтобы запустить приложение в продакшене (на gunicorn):
   ```sh
   make render-start
   ```
