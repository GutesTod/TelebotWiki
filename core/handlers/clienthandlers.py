from aiogram import types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from core.scripts.wiki import get_generative_replica, getwiki, update
question = ''
class Form(StatesGroup):
    temp = State()

async def start_bot(msg : types.Message):
    await msg.answer('Здравствуйте!')

async def get_text_msgs(msg : types.Message, state : FSMContext):
    command = msg.text.lower()
    if command == 'не так':
        await msg.reply('А как?')
        await Form.temp.set()
    else:
        question = command
        reply = await get_generative_replica(question)
        if reply == 'вики':
            await msg.answer(getwiki(command))
        else:
            await msg.answer(reply)

async def wrong(msg : types.Message):
    a = f"{question}\{msg.text.lower()} \n"
    with open('./core/scripts/dialogues.txt', "a", encoding='utf-8') as f:
        f.write(a)
    await msg.reply("Готово!")
    await update()
