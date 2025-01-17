# 🧹🪣 Telegram profile pic cleaner (TPPC)

**Скрипт удаляет все фотографии в профиле Telegram**

## 🚀 Как использовать

1. Установите **Pyrogram**:
   ```bash
   ## Библиотека использованная для работы с аккаунтом телеграм
   pip install pyrogram
   ```
2. Скачать репозиторий
   ```bash
   ## Клонируем репозиторий
   git clone https://github.com/MKultra6969/Telegram-Profile-Photo-Cleaner
   ```
3. Перейти в репозиторий
   ```bash
   ## Переходим в директорию 
   cd Telegram-Profile-Photo-Cleaner
   ```
4. Изменить **API_ID** и **API_HASH**
   ```python
   api_id = 11111 # Сюда вставить ваш ID
   api_hash = '5125ASOGHUIAWJn' # В ковычки вставить ваш HASH
   ```
 5. Запуск скрипта
    ```bash
    # Убедитесь в том, что вы заполнили строки API_ID и API_HASH
    python main.py
    ```
# ⚠️ Важно

1. При первом запуске запросит ввести ваш номер телефона от аккаунта который нужно отчистить.
2. После нужно ввести код подтверждения.
3. В случае если у вас стоит пароль его тоже нужно будет ввести.
4. **API_ID** и **API_HASH** брать по ссылке [my.telegram.org](https://my.telegram.org/auth). (*Это нужно для корректной работы клиента Pyrogram*)
