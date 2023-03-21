# -*- coding: utf-8 -*-
import discord
import requests

# URL-адрес API для перевода
TRANSLATE_URL = "https://api-free.deepl.com/v2/translate"

# Ключ API Deepl (замените на свой собственный)
DEEPL_API_KEY = "ВАШ_КЛЮЧ_API_ЗДЕСЬ"

client = discord.Client()

@client.event
async def on_ready():
    print('Бот готов к работе!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ts'):
        # Удаляем префикс "!перевести" из сообщения
        text = message.content[len('!ts'):].strip()

        # Определяем исходный язык текста
        source_lang = detect_language(text)

        if source_lang == 'ru':
            # Переводим текст с русского на английский
            translated_text = translate(text, source_lang, 'en')
        elif source_lang == 'en':
            # Переводим текст с английского на русский
            translated_text = translate(text, source_lang, 'ru')
        else:
            await message.channel.send('Извините, я могу переводить только между русским и английским языками.')
            return

        # Отправляем переведенный текст в виде сообщения в тот же канал
        await message.channel.send(translated_text)

def detect_language(text):
    # Используем Deepl API для определения языка текста
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'target_lang': 'EN',
        'source_lang': '',
    }
    response = requests.post(TRANSLATE_URL, params=params).json()
    return response['detected_source_language']

def translate(text, source_lang, target_lang):
    # Используем Deepl API для перевода текста
    params = {
        'auth_key': DEEPL_API_KEY,
        'text': text,
        'source_lang': source_lang,
        'target_lang': target_lang,
    }
    response = requests.post(TRANSLATE_URL, params=params).json()
    return response['translations'][0]['text']

# Замените "ВАШ_ТОКЕН_ДИСКОРД_БОТА" на свой токен Discord-бота
client.run('ВАШ_ТОКЕН_ДИСКОРД_БОТА')




