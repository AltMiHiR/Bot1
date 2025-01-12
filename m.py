# 08/01/2025

import pytz
import asyncio
import threading

from pyrogram import Client
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient



IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
    "session": "BAGMcpgASd4WLRgrZ64zoyXzB35aQ2sojHn7qOIWSzwFcJakUx5woxJXA3t9wYjYyo4EElmpQcEc5riVWcqTdzZcFHzJ-aNBI3Sv-_F2sZUX5yVwrIWAZ9Kb571zxTpLIyV45xwpU-mhixcz95hgcdMcDJmixLxDh4APITOslwIB_UDaqrGJ1Yv2i9WRfJIfG3euE6vnweaYijFn-7ARRFS0Rg2BRhzNE_SdfSPwZ_CZ59OfTt4ETQUD5zBN94CzEgNojuQZkgzZk5l5BmAgOmZMLAdRVp0OcqZsEco0TjUdW5R-UIIDMdHeGAilkhKY26YWcrgbd9tbw5RmZgM1EDLGrMw4QgAAAABpsOo_AA",
    "phone_number": "+923551044130"
}

CHATS = {
    -1001303959083: "@httpstmejoinchatOltDQhO6Cw",
    -1001170860302: "@MarketStrong",
    -1001437916508: "@afengiogtobak",
    -1001527007389: "https://t.me/joinchat/TeqEqGaau7UyZTFk",
    -1001469840857: "https://t.me/joinchat/zRL6AlXSWtkzYTFk",
    -1001325622242: "https://t.me/joinchat/dNMbjY4oOwY4OGI0",
    -1001595987025: "https://t.me/joinchat/ybXSq6ZDVDcwNDg8",
    -1001493802984: "https://t.me/joinchat/SMPfqFkJn-gb_pZmMMvXJQ",
    -1001320290633: "https://t.me/joinchat/IWC4FxHDbeOVgyLntkEeaQ",
    -1001153450526: "https://t.me/joinchat/J_aD1Jjfft8xNzNk",
    -1001155030078: "https://t.me/joinchat/Kk-O3hRHsvRl-q_uuORacA",
    -1001424853896: "https://t.me/joinchat/M40bxxNMyvCFkYKTa-LPuA",
    -1001205313235: "https://t.me/joinchat/PmGvgh0v0sJkLoxBe0d3Rg",
    -1001242480702: "https://t.me/joinchat/QcUw8BTnVbPRexXPUA1JlQ",
    -1001214829860: "@CHRISTIANSEXCLUB",
    -1001192385192: "@NewGoodShiddD_Drugs",
    -1001293195336: "@MADEITOUTTHASTONE",
    -1001232993323: "@kofecktkassin",
    -1001147510917: "https://t.me/joinchat/McFg_URloIV0FesEJDfAAw",
    -1001713249177: "https://t.me/joinchat/LxwyGSxGIrIzOGE1",
    -1002148525952: "https://t.me/joinchat/Jzyphd-fWPwwZWNl"
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


class Userbot(Client):
    async def start(self):
        await super().start()
        try:
            async for dialog in self.get_dialogs():
                continue
        except:
            pass


DATA = ThreadSafeList()


async def main():
    app = Userbot(ACCOUNT["phone_number"], session_string=ACCOUNT["session"], no_updates=True, max_message_cache_size=0)

    await app.start()
    print("USERBOT STARTED!")

    is_not_first = False

    while True:
        if is_not_first:
            current_date = datetime.now(IST)
            next_day = current_date + timedelta(days=1)
            next_day = next_day.replace(hour=0, minute=0, second=0, microsecond=0)
            sleep_seconds = (next_day - current_date).total_seconds()
            if sleep_seconds:
                await asyncio.sleep(sleep_seconds)
        else:
            is_not_first = True

        for chat_id, chat_link in CHATS.items():
            previous_day = datetime.now() - timedelta(days=1)
            mcount = 0
            try:
                async for message in app.search_messages(chat_id=chat_id, min_date=previous_day, max_date=datetime.now()):
                    mcount += 1
                    if mcount % 1000 == 0:
                        await asyncio.sleep(4)
                    if message.from_user.id in [5961091462, 277756078, 756558173, 126203394, 108918720]:
                        data = {
                            "user_id": message.from_user.id,
                            "chat_id": message.chat.id,
                            "message_id": message.id,
                            "timestamp": int(message.date.timestamp())
                        }
                        DATA.append(data)
            except Exception as e:
                print(f"ERROR: {chat_id} {type(e).__name__}")
            await TrackDataCol.insert_many(DATA)
            DATA.clear()
            now = datetime.now()
            await asyncio.sleep((60 - now.second) + ((59 - now.minute) * 60))

    await app.stop()
    print("USERBOT STOPPED!")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
