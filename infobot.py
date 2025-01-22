import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext

# Reemplaza con el token de tu bot
TOKEN = '8031295943:AAHUy_-K3ZCCi7bYQqLMl4z5DPeaDxXX31o'

# Función que maneja los mensajes y muestra el ID del grupo
def get_chat_id(update: Update, context: CallbackContext):
    # Imprime el ID del grupo en la consola
    chat_id = update.message.chat_id
    print(f"ID del grupo: {chat_id}")
    update.message.reply_text(f"El ID de este grupo es: {chat_id}")

# Función para iniciar el bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text('¡Hola! Menciona al bot para que te dé el ID del grupo.')

# Función principal
def main():
    # Usamos el token que creaste
    updater = Updater(TOKEN)

    # Obtén el dispatcher para registrar los manejadores
    dispatcher = updater.dispatcher

    # Manejador para el comando /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Manejador para obtener el ID del grupo
    dispatcher.add_handler(MessageHandler(filters.text & ~filters.command, get_chat_id))

    # Inicia el bot
    updater.start_polling()

    # Mantiene el bot funcionando hasta que se detenga
    updater.idle()
    
if __name__ == "__main__":
    # Ejecuta el bot en un hilo separado
    Thread(target=run_bot).start()
    
 # Inicia el servidor Flask
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
