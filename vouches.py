import asyncio
from aiogram import Bot
import os
from keepalive import keep_alive
from random import randint

keep_alive()

services = [
    'Marcus', 'zelle', 'Email', 'CIBC', 'CashApp', 'ApplePay', 'PayPal',
    'BankofAmerica', 'Amazon', 'Gmail', 'wellsfargo', 'Venmo', 'citizens',
    'Bank', 'CapitalOne', 'Coinbase', 'Afterpay', 'Visa', 'MasterCard',
    'Facebook', 'WhatsApp', 'Instagram'
]


bot = Bot(os.environ.get('token'))
async def main_loop():
    while True:
        otp = ''.join([str(randint(0, 9)) for _ in range(6)])
        service = services[randint(0, len(services)-1)]
        msg1 = (
            f"<b>📲 AORUS OTP 📲 ┃ VOUCHES </b>\n"
            f"➖➖➖➖➖➖\n"
            f"╭  Service Name ➣ <b>{service}</b>\n"
            f"⭐ OTP ➣ <code>{otp}</code> ✅\n"
            f"╰  Capture By: -----------\n"
            f"🤖 <a href='https://t.me/AORUS_OTP_bot'>BOT</a>"
        )
        await bot.send_message(chat_id=-1002662428684, text=msg1, parse_mode='HTML')

        await asyncio.sleep(randint(600, 1300))


if __name__ == "__main__":
    asyncio.run(main_loop())
