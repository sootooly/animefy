# bot.py
import logging
import telegram
from telegram.ext import Updater, MessageHandler, Filters

import config
import transform

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def photo_handler(bot: telegram.Bot, update: telegram.Update):
  """
  Handles incoming photos by getting the photo file, transforming it using the deepai anime style transfer model,
  and then sending the transformed image back to the user.
  """
  # Get the photo file and transform it
  photo = update.message.photo[-1].get_file()
  image_data = photo.download_as_bytearray()
  transformed_image = transform.transform_image(image_data)
  
  # Send the transformed image back to the user
  chat_id = update.message.chat_id
  bot.send_photo(chat_id=chat_id, photo=transformed_image)

def error_handler(bot, update, error):
  """
  Handles errors by logging them.
  """
  logger.warning('Update "%s" caused error "%s"', update, error)

def main():
  # Create the Updater and register the photo handler
  updater = Updater(token=config.bot_token)
  dispatcher = updater.dispatcher

  photo_handler = MessageHandler(Filters.photo, photo_handler)
  dispatcher.add_handler(photo_handler)

  # Register the error handler
  dispatcher.add_error_handler(error_handler)

  # Start the bot
  updater.start_polling()

if __name__ == '__main__':
  main()

