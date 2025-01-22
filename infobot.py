import os
from flask import Flask
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Variables de entorno
BOT_TOKEN = os.getenv('8031295943:AAHUy_-K3ZCCi7bYQqLMl4z5DPeaDxXX31o')

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

async def run_bot():
    """Ejecución del bot en un loop asyncio."""
    await application.run_polling()

if __name__ == "__main__":
    # Crear un loop de eventos para ejecutar el bot y Flask en paralelo
    loop = asyncio.get_event_loop()

    # Inicia el bot en el loop de eventos
    loop.create_task(run_bot())

    # Ejecuta el servidor Flask
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


