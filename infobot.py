
import os
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Variables de entorno
BOT_TOKEN =  '8031295943:AAHUy_-K3ZCCi7bYQqLMl4z5DPeaDxXX31o'

# Inicializa el bot
application = ApplicationBuilder().token(BOT_TOKEN).build()

# Manejador para responder con el ID del grupo
async def get_group_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        chat_id = update.message.chat_id
        await update.message.reply_text(f"El ID de este grupo es: {chat_id}")

# Configura los manejadores del bot
application.add_handler(MessageHandler(filters.TEXT & filters.ChatType.GROUPS, get_group_id))

# Flask para el Web Service
app = Flask(__name__)

@app.route("/")
def index():
    return "El bot está funcionando correctamente."

def run_bot():
    """Ejecución del bot en un hilo separado."""
    application.run_polling()

if __name__ == "__main__":
    # Ejecuta el bot en un hilo separado
    bot_thread = Thread(target=run_bot)
    bot_thread.start()

    # Inicia el servidor Flask
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
