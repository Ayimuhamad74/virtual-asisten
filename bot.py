from telegram import Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from dotenv import load_dotenv
import os

# Muat variabel lingkungan dari file .env
load_dotenv()

# Dapatkan token bot dari variabel lingkungan
bot_token = os.getenv("BOT_TOKEN")


# Fungsi handler untuk perintah /start
def start(update: Update, context: CallbackContext) -> None
    update.message.reply_text(
        "Halo! Saya adalah bot asisten bisnis e-commerce Anda. Silakan gunakan perintah /help untuk melihat daftar perintah yang tersedia."
    )


# Fungsi handler untuk perintah /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Berikut adalah daftar perintah yang dapat Anda gunakan:\n
        "/start - Memulai bot\n"
        "/help - Menampilkan daftar perintah\n
        "Perintah khusus sesuai dengan fitur-fitur bot Anda."
    )


# Fungsi handler untuk menanggapi pesan teks
def handle_text(update: Update, context: CallbackContext) -> None
    user_input = update.message.text.lower()

    # Mencetak ke konsol
    print(f"Pengguna {update.message.from_user.username} mengatakan: {user_input}"

    # Lakukan sesuatu berdasarkan input pengguna
    if "produk" in user_input
        update.message.reply_text("Anda mencari produk. Berikut daftar produk kami..."
    elif "promo" in user_input:
        update.message.reply_text(
            "Saat ini kami memiliki promo khusus. Gunakan kode diskon XYZ untuk mendapatkan potongan harga!"
        )
    else:
        update.message.reply_text(
            "Maaf, saya tidak mengerti perintah tersebut. Gunakan /help untuk melihat daftar perintah."
        )


def main() -> None:
    # Inisialisasi updater
    updater = Updater(token=bot_token, use_context=True)

    # Inisialisasi dispatcher
    dp = updater.dispatcher

    # Menambahkan handler
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("produk", daftar_produk))
    dp.add_handler(CommandHandler("promo", daftar_promo))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == "__main__"
    main()
