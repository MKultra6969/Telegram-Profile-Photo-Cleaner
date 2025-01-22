import logging
import os
import pyfiglet
from pyrogram import Client
from pyrogram.errors import FloodWait
from colorama import Fore, Style

api_id = 1
api_hash = "1"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()

logging.getLogger("pyrogram").setLevel(logging.WARNING)

client = Client('pic_cleaner', api_id, api_hash)


def delete_all_photos():
    try:
        user = client.get_me()

        # Получаем аватарки профиля пользователя
        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("Нет аватарок для удаления.")
            return

        for photo in photos:
            try:
                client.delete_profile_photos(photo.file_id)
                logger.info(f"Аватарка {photo.file_id} удалена успешно.")
            except FloodWait as e:
                logger.warning(f"Превышен лимит запросов. Подождите {e.x} секунд.")
            except Exception as e:
                logger.error(f"Ошибка при удалении аватарки {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"Ошибка при получении аватарок профиля: {e}")


def delete_some_photos(count):
    try:
        user = client.get_me()

        # Получаем аватарки профиля пользователя
        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("Нет аватарок для удаления.")
            return

        for photo in photos[:count]:
            try:
                client.delete_profile_photos(photo.file_id)
                logger.info(f"Аватарка {photo.file_id} удалена успешно.")
            except FloodWait as e:
                logger.warning(f"Превышен лимит запросов. Подождите {e.x} секунд.")
            except Exception as e:
                logger.error(f"Ошибка при удалении аватарки {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"Ошибка при получении аватарок профиля: {e}")


def download_photos():
    try:
        user = client.get_me()

        # Создаём папку для сохранения фотографий
        if not os.path.exists("pics"):
            os.makedirs("pics")

        # Получаем аватарки профиля пользователя
        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("Нет аватарок для скачивания.")
            return

        for index, photo in enumerate(photos):
            try:
                file_path = client.download_media(photo.file_id, file_name=f"pics/avatar_{index + 1}.jpg")
                logger.info(f"Аватарка {photo.file_id} скачана: {file_path}")
            except Exception as e:
                logger.error(f"Ошибка при скачивании аватарки {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"Ошибка при скачивании аватарок профиля: {e}")


def show_info():
    info = """
    Скрипт для очистки аватарок в Telegram.

    Доступные команды:
    1. Начать очистку - удаляет все или указанное количество аватарок.
    2. Скачать аватарки - сохраняет все аватарки профиля в папку pics.
    3. Инфо - показывает это сообщение.
    4. Выход - завершает работу скрипта.

    Перед началом убедитесь, что ваш api_id и api_hash указаны правильно.

    by MKultra69
    """
    print(info)


def main_menu():
    ascii_logo = pyfiglet.figlet_format("P P C", font="cosmic")
    print(Fore.CYAN + Style.BRIGHT + ascii_logo + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "by MKultra69" + Style.RESET_ALL)

    while True:
        print(Fore.YELLOW + "\n--- Меню ---" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Начать очистку" + Style.RESET_ALL)
        print(Fore.BLUE + "2. Скачать аватарки" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Инфо" + Style.RESET_ALL)
        print(Fore.RED + "4. Выход" + Style.RESET_ALL)
        choice = input(Fore.WHITE + "Выберите действие: " + Style.RESET_ALL)

        if choice == '1':
            confirm = input(
                Fore.YELLOW + Style.BRIGHT + "Очистить все аватарки? (Y/N): " + Style.RESET_ALL).strip().lower()
            if confirm == 'y':
                delete_all_photos()
            elif confirm == 'n':
                try:
                    count = int(input(
                        Fore.YELLOW + Style.BRIGHT + "Введите количество аватарок для удаления: " + Style.RESET_ALL))
                    delete_some_photos(count)
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "Неверный ввод. Пожалуйста, введите число." + Style.RESET_ALL)
            else:
                print(Fore.RED + Style.BRIGHT + "Неверный ввод. Возврат в меню." + Style.RESET_ALL)
        elif choice == '2':
            download_photos()
        elif choice == '3':
            show_info()
        elif choice == '4':
            print(Fore.RED + Style.BRIGHT + "Выход из программы." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Неверный выбор. Попробуйте снова." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        client.start()

        main_menu()

    except Exception as e:
        logger.error(f"Ошибка: {e}")
    finally:
        client.stop()
        logger.info("Клиент остановлен.")