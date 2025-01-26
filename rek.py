from telethon import TelegramClient, errors

# Telegram API ma'lumotlari
api_id = "22781349"  # Telegram API ID
api_hash = "be81e749f0a0579716b1af24f776399e"  # Telegram API Hash

# Sessiya nomi
session_name = "your_account_session"  # Sessiya fayli uchun nom

# Telegram sessiyasini ishga tushirish
client = TelegramClient(session_name, api_id, api_hash)

async def main():
    print("Obunachi qo'shmoqchi bo'lgan Telegram guruhingiz usernamesini kiriting (misol: @yourgroup):")
    target_group = input("Guruh usernamesi: ")

    # Reklama yuboriladigan guruhlar ro'yxati
    target_groups = ["@mamashaol", "@mamashaol", "@mamashaol"]  # O'zingiz xohlagan usernameslarni kiriting

    for group in target_groups:
        try:
            message = f"Assalomu alaykum! Ushbu guruhga obuna bo'lishni tavsiya qilamiz: {target_group}. Sizga qiziqarli bo'lishi mumkin!"
            await client.send_message(group, message)
            print(f"Reklama xabari {group} guruhiga yuborildi!")
        except errors.ChatWriteForbiddenError:
            print(f"Xatolik: {group} guruhiga yozish mumkin emas.")
        except Exception as e:
            print(f"Xatolik yuz berdi: {e}")

with client:
    client.loop.run_until_complete(main())
