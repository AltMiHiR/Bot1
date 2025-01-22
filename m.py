import pytz
import asyncio
import threading
import logging

from pyrogram import Client
from pyrogram.errors import UserAlreadyParticipant

from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient



IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
    "session": "BQGMcpgAjY5X0m8kJLmNGGTlpoVz9hoa3GBJfjPQnef6WZkn-rQ4GHPDUrdpGmXeRVop5qjacSU0jBGJd6SyLMZ-OOWJoSQIp2X0KUdIHcI2_gLSqZn8sQKUQ2EDSywYk3h-s0eLVmtakWzHi219srMZ4XWoayZufBqvb-bfCmZlkHn0jnmlYaJ2qti_oMkpx0Y7OPP2e-Z5F2qs8EcQb2TsXzgtijExd7IGEMu3oYG8Mcl2AE0E4iFzlu3wmBW7Uxq_J2Kz3WtzT-u5Ms10jAfHkhLuNZY9vlJVW9tdqKjGh6HT8Gv3HEEjUlGlJ_xbS8LvTnIlo42Ui1OZlaPkslVkluTVFQAAAAHMeMGEAA",
    "phone_number": "+919761301924"
}

CHATS = {
    -1001170860302: "@MarketStrong",
    -1001527007389: "https://t.me/joinchat/TeqEqGaau7UyZTFk",
    -1001469840857: "https://t.me/joinchat/zRL6AlXSWtkzYTFk",
    # -1001325622242: "https://t.me/joinchat/dNMbjY4oOwY4OGI0",
    # -1001595987025: "https://t.me/joinchat/ybXSq6ZDVDcwNDg8",
    # -1001493802984: "https://t.me/joinchat/SMPfqFkJn-gb_pZmMMvXJQ",
    # -1001320290633: "https://t.me/joinchat/IWC4FxHDbeOVgyLntkEeaQ",
    # -1001153450526: "https://t.me/joinchat/J_aD1Jjfft8xNzNk",
    # -1001155030078: "https://t.me/joinchat/Kk-O3hRHsvRl-q_uuORacA",
    # -1001205313235: "https://t.me/joinchat/PmGvgh0v0sJkLoxBe0d3Rg",
    # -1001242480702: "https://t.me/joinchat/QcUw8BTnVbPRexXPUA1JlQ",
    # -1001214829860: "@CHRISTIANSEXCLUB",
    # -1001192385192: "@NewGoodShiddD_Drugs",
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

        today = datetime.now(IST)
        previous_day = today - timedelta(days=1)
        today = today.astimezone(IST).replace(hour=0, minute=0, second=0, microsecond=0)
        previous_day = previous_day.astimezone(IST).replace(hour=0, minute=0, second=0, microsecond=0)

        for chat_id, chat_link in CHATS.items():
            # Joining Chat if not Joined
            try:
                chat = await app.get_chat(chat_link)
                await app.get_chat_member(chat_id=chat.id, user_id="me")
            except:
                try:
                    chat = await app.join_chat(chat_link)
                except UserAlreadyParticipant:
                    try:
                        chat = await app.get_chat(chat_link)
                    except Exception as e:
                        print(f"Failed to Access: {type(e).__name__} ( {chat_link} )")
                        continue
                except Exception as e:
                    print(f"Failed to Join: {type(e).__name__} ( {chat_link} )")
                    continue
            print(f"RUNNING {chat_id}...  {datetime.now(IST).strftime('%d-%m-%Y %H:%M:%S')}", end=" ")
            mcount = 0
            try:
                async for message in app.search_messages(chat_id=chat_id, min_date=previous_day, max_date=today):
                    mcount += 1
                    if mcount % 1000 == 0:
                        await asyncio.sleep(3)
                    if message.from_user and message.from_user.id in [5961091462, 277756078, 756558173, 126203394, 108918720]:
                        data = {
                            "user_id": message.from_user.id,
                            "chat_id": message.chat.id,
                            "message_id": message.id,
                            "timestamp": int(message.date.timestamp())
                        }
                        DATA.append(data)
            except Exception as e:
                print(f"ERROR_{type(e).__name__}", end=" ")
            if len(DATA) > 0:
                await TrackDataCol.insert_many(DATA)
                print(f"ADDED_{len(DATA)}_DOCS_OF_{previous_day.strftime('%d-%m-%Y')}")
                DATA.clear()
            else:
                print(f"ADDED_0_DOCS_OF_{previous_day.strftime('%d-%m-%Y')}")
            now = datetime.now()
            await asyncio.sleep((60 - now.second) + ((59 - now.minute) * 60))

    await app.stop()
    print("USERBOT STOPPED!")


logging.getLogger("pyrogram").setLevel(logging.ERROR)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
