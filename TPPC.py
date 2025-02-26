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

        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("Нет нихуя, нечего удалять.")
            return

        for photo in photos:
            try:
                client.delete_profile_photos(photo.file_id)
                logger.info(f"Авка {photo.file_id} удалена.")
            except FloodWait as e:
                logger.warning(f"Флуд. Ждем {e.x} секунд.")
            except Exception as e:
                logger.error(f"НЕ СМОГ УДАЛИТЬ ЧЗХ??? {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"ОШИБКА при получении авок профиля: {e}")


def delete_some_photos(count):
    try:
        user = client.get_me()

        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("Нет нихуя, нечего удалять.")
            return

        for photo in photos[:count]:
            try:
                client.delete_profile_photos(photo.file_id)
                logger.info(f"Авка {photo.file_id} удалена.")
            except FloodWait as e:
                logger.warning(f"Флуд. Ждем {e.x} секунд.")
            except Exception as e:
                logger.error(f"НЕ СМОГ УДАЛИТЬ ЧЗХ??? {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"ОШИБКА при получении авок профиля: {e}")


def download_photos():
    try:
        user = client.get_me()

        # Создаём папке для сохранения фоточег
        if not os.path.exists("pics"):
            os.makedirs("pics")

        # Получаем аватарке профиле пользователе
        photos = list(client.get_chat_photos(user.id))

        if not photos:
            logger.info("НЕХУЙ СКАЧИВАТЬ, НЕТ НИЧЕ.")
            return

        for index, photo in enumerate(photos):
            try:
                file_path = client.download_media(photo.file_id, file_name=f"pics/avatar_{index + 1}.jpg")
                logger.info(f"Пикча {photo.file_id} скачана: {file_path}")
            except Exception as e:
                logger.error(f"ОНО НЕ СКАЧИВАЕТСЯ {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"Ошибке при скачивании авок: {e}")


def show_info():
    info = """
    Отчистка профиля ТГ от аватарок.

    Доступные команды:
    1. Начать очистку - сносит все или указанное кол-во аватарок.
    2. Скачать аватарки - сохраняет все авки профиля в папку pics.
    3. Инфо - показывает это сообщение(АХУЕТЬ).
    4. Выход - завершает работу скрипта(НЕ МОЖЕТ БЫТЬ, АНБЕЛИВЕБЛЕ НАХУЙ).

    P.S. 
    Напиши 'q' находясь в любой вкладке для выхода в меню.
    Перед началом убедитесь, что ваш api_id и api_hash указаны правильно.

    by MKultra69 with l0ve
    """
    print(info)


def main_menu():
    ascii_logo = pyfiglet.figlet_format("T P P C", font="cosmic")
    print(Fore.CYAN + Style.BRIGHT + ascii_logo + Style.RESET_ALL)
    print(Fore.MAGENTA + Style.BRIGHT + "by MKultra69" + Style.RESET_ALL)

    while True:
        print(Fore.YELLOW + "\n--- Меню ---" + Style.RESET_ALL)
        print(Fore.GREEN + "1. Начать очистку" + Style.RESET_ALL)
        print(Fore.BLUE + "2. Скачать аватарки" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Инфо" + Style.RESET_ALL)
        print(Fore.RED + "4. Выход" + Style.RESET_ALL)
        choice = input(Fore.WHITE + "Выбирай: " + Style.RESET_ALL)

        if choice == '1':
            while True:
                confirm = input(Fore.YELLOW + Style.BRIGHT + "Снести все(Y) авки или часть(N)?: " + Style.RESET_ALL).strip().lower()
                if confirm == 'q':
                    print(Fore.CYAN + "Идем в менюшку." + Style.RESET_ALL)
                    break
                elif confirm == 'y':
                    delete_all_photos()
                    break
                elif confirm == 'n':
                    while True:
                        count_input = input(Fore.YELLOW + Style.BRIGHT + "Введи кол-во для удаления: " + Style.RESET_ALL).strip().lower()
                        if count_input == 'q':
                            print(Fore.CYAN + "Идем в менюшку." + Style.RESET_ALL)
                            break
                        try:
                            count = int(count_input)
                            delete_some_photos(count)
                            break
                        except ValueError:
                            print(Fore.RED + Style.BRIGHT + "Какую то хуйню высрал юзерок, нормально напиши" + Style.RESET_ALL)
                    if count_input == 'q':
                        break
                    break
                else:
                    print(Fore.RED + Style.BRIGHT + "Все хуйня, давай по новой." + Style.RESET_ALL)
        elif choice == '2':
            download_photos()
        elif choice == '3':
            show_info()
        elif choice == '4':
            print(Fore.RED + Style.BRIGHT + "Прощай..." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + Style.BRIGHT + "Все хуйня, давай по новой." + Style.RESET_ALL)


if __name__ == "__main__":
    try:
        client.start()

        main_menu()

    except Exception as e:
        logger.error(f"ЕГГОГ: {e}")
    finally:
        client.stop()
        logger.info("Отключился(Клиент вырубился).")
