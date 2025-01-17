import logging
from pyrogram import Client
from pyrogram.errors import FloodWait


api_id = 0
api_hash = 'HASH'


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger()


client = Client('session_name', api_id, api_hash)

def delete_all_photos():
    try:
        user = client.get_me()

        photos = client.get_chat_photos(user.id)

        if not photos:
            logger.info("Нет фотографий для удаления.")
            return

        for photo in photos:
            try:
                client.delete_profile_photos(photo.file_id)
                logger.info(f"Фото {photo.file_id} удалено успешно.")
            except FloodWait as e:
                logger.warning(f"Превышен лимит запросов. Подождите {e.x} секунд.")
            except Exception as e:
                logger.error(f"Ошибка при удалении фото {photo.file_id}: {e}")

    except Exception as e:
        logger.error(f"Ошибка при получении фотографий профиля: {e}")

if __name__ == "__main__":
    try:
        client.start()

        delete_all_photos()

    except Exception as e:
        logger.error(f"Ошибка: {e}")
    finally:
        client.stop()
        logger.info("Клиент остановлен.")


# Александр это как бы твой скафандр?
