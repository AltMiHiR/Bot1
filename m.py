# 04/01/2025

import pytz

from motor.motor_asyncio import AsyncIOMotorClient

from pyrogram import Client, filters, idle
from pyrogram.types import Message


IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
    "session": "BQGMcpgAL3HEPcinegslJIhuyyvmjlEBL3u3zjjAMe_vDAD_-yCNj4pLZnC7EPmgQ32w_74aHSIR2SUDssLV48d-Gym-s9iN3F8IeGd7AT_uO-NZEbnn_89MRUH8-R02bPxeqpXt2MZfMoVUUc3JEsJrvkZuYa0toxOHB5XcNh03Q0fd20yYVYTz_GF022Zo2qaC34YJXOx0ofjAUYsht2bxg9_RZxwxs1JjKkzUEqo0Vl77ShX2vbyjx_khwWXlSDBZ3-xUQRt6bFn586KI8RkWLDxrMG6eckdF-UWLAfN40D9ZdROn6EMw5YLN2clqz2yCYc7FW9C6zAjuyKJTuv_nXZI1wQAAAAHbJo-eAA",
    "phone_number": "+919675498001"
}

app = Client(ACCOUNT["phone_number"], session_string=ACCOUNT["session"], max_message_cache_size=0)


@app.on_message(filters.group & filters.user([5961091462, 277756078, 756558173, 126203394, 108918720]))
async def _track_post(_, message: Message):
    data = {
        "user_id": message.from_user.id,
        "chat_id": message.chat.id,
        "message_id": message.id,
        "timestamp": int(message.date.timestamp())
    }
    await TrackDataCol.insert_one(data)


app.start()
print("USERBOT STARTED!")

idle()

app.stop()
print("USERBOT STOPPED!")
