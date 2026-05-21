import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "8558971167:AAE9GFlX26_HVWS36BdcMIsF6dVnXEyCLM4"

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def handler(message: types.Message):
    await message.answer(f"🔍 Ты написал: {message.text}")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
