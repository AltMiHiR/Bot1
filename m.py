# 08/01/2025

import pytz
import asyncio

from pyrogram import Client
from datetime import datetime, timedelta
from motor.motor_asyncio import AsyncIOMotorClient



IST = pytz.timezone('Asia/Kolkata')

_mongo_async_ = AsyncIOMotorClient("mongodb+srv://MIHIRxKHUSHI:print('MIKU1311')@thealtron.rwuawpe.mongodb.net/?retryWrites=true&w=majority")
TrackDataCol = _mongo_async_["MFBot"]['TrackData']

ACCOUNT = {
    "session": "BQGMcpgADgmuipxYNJlEza6kOtPAwAH2S22jUyOBOOqzsTkdFnSZnM1S9fHwsHhW7evLIpDqacLHWA9JlJ20PMEQgQJhayMLrtyoIrsRbE-RgG9p37CSMR1kguL78Y9Fi8imk9K2lctNUEffNnNrUTgOD-_ifQh4FZV6lCYr6WI_-MPNq1kQalxj5SjmUHV3nnkaIdVsTfiyroEzYP1AQhxtzoiD5XFPcQVTbK_CKeq8z2QDIMi3vv1F7cNTCZx5PuBUKvPh5xRjm6DJPrdYpelpuersLCmMr1sNv2R0sVoi4d8PKNdbP664qFAiUpRCXbbwPqRmk8Y8QaBga1oU7Pvq-R6n7AAAAAFoWYJIAA",
    "phone_number": "+919723862655"
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


class Userbot(Client):
    async def start(self):
        await super().start()
        try:
            async for dialog in self.get_dialogs():
                continue
        except:
            pass


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
                        await TrackDataCol.insert_one(data)
            except Exception as e:
                print(f"ERROR: {chat_id} {type(e).__name__}")
            now = datetime.now()
            await asyncio.sleep((60 - now.second) + ((59 - now.minute) * 60))

    await app.stop()
    print("USERBOT STOPPED!")


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
