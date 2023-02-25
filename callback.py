from pyrogram import Client
from pyrogram.types import CallbackQuery


@Client.on_callback_query()
async def callback(app: Client, callback_query: CallbackQuery):
    if callback_query.data == 'source':
        await callback_query.answer("test")
        await app.send_message(callback_query.from_user.id, "test2")