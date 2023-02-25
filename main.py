from pyrogram import Client, enums, idle
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import logging, env
markdown = enums.ParseMode.MARKDOWN

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client('refBot', api_id=env.API_ID, api_hash=env.API_HASH, bot_token=env.BOT_TOKEN)
    
if __name__ == "__main__":
    print("𝐒𝐭𝐚𝐫𝐭𝐢𝐧𝐠 𝐓𝐡𝐞 𝐁𝐨𝐭...")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("𝐘𝐨𝐮𝐫 API_ID/API_HASH 𝐈𝐬 𝐍𝐨𝐭 𝐕𝐚𝐥𝐢𝐝.")
    except AccessTokenInvalid:
        raise Exception("𝐘𝐨𝐮𝐫 BOT_TOKEN 𝐈𝐬 𝐍𝐨𝐭 𝐕𝐚𝐥𝐢𝐝")
    uname = app.get_me().username
    print(f"@{uname} 𝐒𝐭𝐚𝐫𝐭𝐞𝐝 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲")
    idle()
    app.stop()
    print("𝐁𝐨𝐭 𝐒𝐭𝐨𝐩𝐩𝐞𝐝. 𝐁𝐲𝐞!")