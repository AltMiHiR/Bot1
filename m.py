import pytz
import logging
import asyncio
import threading

from pyrogram import Client, filters, idle
from pyrogram.types import Message

from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient



IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
      "session": "BQGMcpgAiz495Brqz0p2krN4kuGdj68KTccSsaNFfmwfqo3FacWLTWnaHSCW20K8eg6LdOB0rsagQNYVs6huDotVGBXtkZXcZOMPolSmd7tjk4eRQGqVe-YkMCnsN3GFgooQimOfkho3BttQ2cZKgKtTiWY3TjrnWzZw8jd0mr0CbAfXpiZPmV8J-XCRJoNX-AYYbXJK2ZJ9xnl3pUwH-xjYf_q94Uc9mQ3MueWKi5kYLX6hXMk86oqN_ImUcaVT3K3CzQWb_oZ4rjzslKGGj2MWv2ZogfGvoQC_eYD55FvmNV2lDLtpVXBdTFxppyo98gnaU2s2JiMK8fIXAsPjX_QU-gJe8wAAAAHaoqR0AA",
      "phone_number": "+919759234857"
}

CHATS = {
    -1001153450526: "https://t.me/joinchat/J_aD1Jjfft8xNzNk",
    -1001155030078: "https://t.me/joinchat/Kk-O3hRHsvRl-q_uuORacA",
    -1001205313235: "https://t.me/joinchat/PmGvgh0v0sJkLoxBe0d3Rg",
    -1001242480702: "https://t.me/joinchat/QcUw8BTnVbPRexXPUA1JlQ",
    -1001214829860: "@CHRISTIANSEXCLUB",
    # -1001293195336: "@MADEITOUTTHASTONE",
    # -1001232993323: "@kofecktkassin",
    # -1001147510917: "https://t.me/joinchat/McFg_URloIV0FesEJDfAAw",
    # -1001713249177: "https://t.me/joinchat/LxwyGSxGIrIzOGE1",
    # -1002148525952: "https://t.me/joinchat/Jzyphd-fWPwwZWNl"
}

class ThreadSafeList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self._lock = threading.Lock()

    def append(self, item):
        with self._lock:
            super().append(item)

    def extend(self, iterable):
        with self._lock:
            super().extend(iterable)

    def copy_with_clear(self):
        with self._lock:
            data = super().copy()
            super().clear()
            return data

    def copy(self):
        with self._lock:
            return super().copy()

    def remove(self, item):
        with self._lock:
            super().remove(item)

    def pop(self, index=-1):
        with self._lock:
            return super().pop(index)

    def clear(self):
        with self._lock:
            super().clear()

    def __contains__(self, item):
        with self._lock:
            return super().__contains__(item)

    def __iter__(self):
        with self._lock:
            return iter(super().copy())

    def __len__(self):
        with self._lock:
            return super().__len__()

    def __getitem__(self, index):
        with self._lock:
            return super().__getitem__(index)

    def __setitem__(self, index, value):
        with self._lock:
            super().__setitem__(index, value)

    def __delitem__(self, index):
        with self._lock:
            super().__delitem__(index)


DATA = ThreadSafeList()

app = Client(ACCOUNT["phone_number"], session_string=ACCOUNT["session"], max_message_cache_size=0)

@app.on_message(filters.group & filters.user([5883706596, 5917221056, 5813413216, 5860140820, 5434534346]))
async def _tracker(client: Client, message: Message):
    data = {
        "user_id": message.from_user.id,
        "chat_id": message.chat.id,
        "message_id": message.id,
        "timestamp": int(message.date.timestamp())
    }
    DATA.append(data)


async def main():
    await app.start()
    print("USERBOT STARTED!\n")

    while True:
        await asyncio.sleep(1800)

        if len(DATA) > 0:
            data = DATA.copy_with_clear()
            await TrackDataCol.insert_many(data)
            day = datetime.now(IST)
            print(f"ADDED_{len(data)}_DOCS - {day.strftime('%d-%m-%Y %H:%M:%S')}")
        else:
            day = datetime.now(IST)
            print(f"ADDED_0_DOCS - {day.strftime('%d-%m-%Y %H:%M:%S')}")

    await app.stop()
    print("USERBOT STOPPED!")


logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("asyncio").setLevel(logging.ERROR)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
