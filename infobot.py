from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler, ContextTypes

BOT_TOKEN = "8031295943:AAHUy_-K3ZCCi7bYQqLMl4z5DPeaDxXX31o"
TARGET_GROUP_ID = 1638870587  # Reemplaza con el ID del grupo objetivo



async def mention_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja menciones al bot."""
    if update.message:
        # Eliminar la mención al bot
        text = update.message.text.replace(f"@{context.bot.username}", "").strip()

        # Reenviar el mensaje al grupo objetivo
        await context.bot.send_message(chat_id=TARGET_GROUP_ID, text=text)

        # Confirmar al usuario
        await update.message.reply_text("Mensaje enviado al grupo.")

if __name__ == "__main__":
    # Crear la aplicación del bot
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Comando /start
    application.add_handler(CommandHandler("start", start))

    # Manejador para mensajes que mencionen al bot
    application.add_handler(MessageHandler(filters.TEXT & filters.Entity("mention"), mention_handler))

    # Iniciar el bot
    application.run_polling()
