# Web-chat

Небольшое веб‑приложение для обмена сообщениями: список сообщений, просмотр истории и отправка новых сообщений через REST API. Фронтенд на React + TypeScript, бэкенд на FastAPI. 

## Стек

React, TypeScript, Vite

FastAPI

Axios

Vercel (frontend)

Render (backend)​

## Demo

Frontend (Vercel): https://telegram-chat-app-97tg.vercel.app
Backend (Render): https://telegram-chat-app.onrender.com​

Фронтенд ходит на прод‑бэкенд, CORS настроен на домен Vercel.​

## Быстрый запуск локально
Клонировать репозиторий и перейти в корень проекта:

bash
git clone https://github.com/ph0que/telegram-chat-app.git
cd telegram-chat-app

Установить зависимости и запустить фронтенд (Vite dev server):

bash
npm install
npm run dev
По умолчанию фронтенд ожидает бэкенд на http://localhost:8000 (можно поменять через переменную окружения, см. ниже).​

## Запуск backend (FastAPI)
Перейти в папку backend и создать виртуальное окружение:

bash
cd backend
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows
Установить зависимости и запустить сервер:

bash
pip install -r requirements.txt
uvicorn main:app --reload
Бэкенд поднимется на http://localhost:8000 и будет отдавать сообщения и принимать новые.​

## Запуск frontend отдельно
Если нужно запускать фронтенд отдельно от корня:

bash
cd frontend
npm install
npm run dev
Адрес API задаётся через переменную окружения VITE_API_URL (см. следующий раздел).​

## Переменные окружения
Во фронтенде используется Vite, поэтому переменные окружения должны начинаться с префикса VITE_.​

Пример файла frontend/.env.local:

text
VITE_API_URL=http://localhost:8000

Для прод‑окружения на Vercel VITE_API_URL указывает на Render‑бэкенд:

text
VITE_API_URL=https://telegram-chat-app.onrender.com
Структура проекта
text
telegram-chat-app/
  backend/
    main.py          # FastAPI-приложение, CORS, endpoints для сообщений
    requirements.txt # зависимости backend
  frontend/
    src/
      components/    # React-компоненты интерфейса
      api/           # работа с HTTP-запросами к backend
      styles/        # стили
    index.html
    package.json
  PLAN.md            # черновой план разработки
  REVIEW.md          # заметки и ретроспектива по проекту

backend/main.py содержит конфигурацию CORS, список origins включает прод‑домен Vercel, поэтому браузерные запросы к Render проходят без ошибок.

## Деплой

### Backend (Render)

Бэкенд развёрнут на [Render](https://render.com). Текущий прод‑URL: https://telegram-chat-app.onrender.com

Основные моменты настройки:

- Тип сервиса: Web Service (Python/FastAPI).
- Start command: `uvicorn main:app --host 0.0.0.0 --port 10000` (порт зависит от настроек Render).
- Переменные окружения: стандартные для Python/uvicorn (при необходимости).

CORS в `backend/main.py` настроен так, чтобы разрешать запросы с прод‑домена фронтенда на Vercel.

### Frontend (Vercel)

Фронтенд развёрнут на [Vercel](https://vercel.com). Прод‑URL: https://telegram-chat-app-97tg.vercel.app

Основные моменты настройки:

- Framework: Vite (React + TypeScript).
- Build Command: `npm run build`.
- Output Directory: `dist`.
- Environment Variables:
  - `VITE_API_URL=https://telegram-chat-app.onrender.com`

После деплоя Vercel подставляет `VITE_API_URL` на этапе сборки, и фронтенд ходит к прод‑бэкенду на Render.





