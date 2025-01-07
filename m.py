# 04/01/2025

import pytz

from motor.motor_asyncio import AsyncIOMotorClient

from pyrogram import Client, filters, idle
from pyrogram.types import Message


IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
    "session": "BQGMcpgADgmuipxYNJlEza6kOtPAwAH2S22jUyOBOOqzsTkdFnSZnM1S9fHwsHhW7evLIpDqacLHWA9JlJ20PMEQgQJhayMLrtyoIrsRbE-RgG9p37CSMR1kguL78Y9Fi8imk9K2lctNUEffNnNrUTgOD-_ifQh4FZV6lCYr6WI_-MPNq1kQalxj5SjmUHV3nnkaIdVsTfiyroEzYP1AQhxtzoiD5XFPcQVTbK_CKeq8z2QDIMi3vv1F7cNTCZx5PuBUKvPh5xRjm6DJPrdYpelpuersLCmMr1sNv2R0sVoi4d8PKNdbP664qFAiUpRCXbbwPqRmk8Y8QaBga1oU7Pvq-R6n7AAAAAFoWYJIAA",
    "phone_number": "+919723862655"
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
