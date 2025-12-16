# Telegram Chat App

Telegram‑подобное веб‑приложение: список сообщений, просмотр истории и отправка новых сообщений через REST API. Фронтенд на React + TypeScript, бэкенд на FastAPI.​​

## Стек технологий
Backend: Python 3.12, FastAPI, Uvicorn.​

Frontend: React, TypeScript, Vite.​

Протокол: REST API, формат данных — JSON.

## Быстрый запуск (backend + frontend)
В корне проекта:

bash
npm install
npm run dev
Скрипт npm run dev одновременно поднимает:

backend (FastAPI) на http://127.0.0.1:8000

frontend (Vite) на http://localhost:5173

Фронтенд по умолчанию обращается к API по адресу http://localhost:8000 (можно переопределить через переменную окружения VITE_API_URL в .env).​

## Запуск backend отдельно
bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows (PowerShell/cmd)

# или
source venv/bin/activate     # Linux/macOS

pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
Бэкенд будет доступен по адресу http://127.0.0.1:8000, документация OpenAPI — http://127.0.0.1:8000/docs.​

## Запуск frontend отдельно
bash
cd frontend
npm install
npm run dev
По умолчанию приложение доступно по адресу http://localhost:5173.​

## Основной функционал
Отображение списка сообщений, полученных с бэкенда (GET /messages).​

Отправка нового сообщения через форму (POST /messages).​

Разделение сообщений «от меня» и «от собеседника» по флагу fromMe.​

Обновление списка сообщений после успешной отправки.​

## Структура проекта
backend/ — код FastAPI, файл main.py, модели и ручки API.​

frontend/ — React‑приложение (Vite, TypeScript), компоненты интерфейса.​

PLAN.md / REVIEW.md — план и заметки по реализации тестового задания.

## Demo

Frontend: https://telegram-chat-app-97tg.vercel.app/  
Backend: не задеплоен, работает только локально по адресу http://localhost:8000 (для проверки API нужно поднять backend у себя, см. раздел «Запуск backend отдельно» выше).