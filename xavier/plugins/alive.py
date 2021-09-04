from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

xavier_pic = Config.ALIVE_PIC or "https://telegra.ph/file/82667e54c5a2b3e86b56d.jpg"
alive_c = f"__**✘ χανιєя ιѕ σиℓιиє ✘**__\n\n"
alive_c += f"__↼ 𝐎𝐖𝐍𝐄𝐑 ⇀__ : ◤ {xavier_mention} ◢\n\n"
alive_c += f"•✘• 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧    :  `{tel_ver}` \n"
alive_c += f"•✘• 𝐗𝐚𝐯𝐢𝐞𝐫       :  __**{xavier_ver}**__\n"
alive_c += f"•✘• 𝐒𝐮𝐝𝐨            :  `{is_sudo}`\n"
alive_c += f"•✘• 𝐂𝐡𝐚𝐧𝐧𝐞𝐥      :  {xavier_channel}\n"

#-------------------------------------------------------------------------------

@bot.on(xavier_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(xavier):
    if xavier.fwd_from:
        return
    await xavier.get_chat()
    await xavier.delete()
    await bot.send_file(xavier.chat_id, xavier_pic, caption=alive_c)
    await xavier.delete()

msg = f"""
**🚀 𝙓𝙖𝙫𝙞𝙚𝙧 𝙞𝙨 𝙊𝙣𝙡𝙞𝙣𝙚 🚀**
{Config.ALIVE_MSG}
**🏓 𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐮𝐬 🏓**
**𝙏𝙚𝙡𝙚𝙩𝙝𝙤𝙣 :**  `{tel_ver}`
**𝙓𝙖𝙫𝙞𝙚𝙧  :**  **{xavier_ver}**
**𝘼𝙗𝙪𝙨𝙚    :**  **{abuse_m}**
**𝙎𝙪𝙙𝙤      :**  **{is_sudo}**
"""
botname = Config.BOT_USERNAME

@bot.on(xavier_cmd(pattern="xavier$"))
@bot.on(sudo_cmd(pattern="xavier$", allow_sudo=True))
async def xavier_a(event):
    try:
        xavier = await bot.inline_query(botname, "alive")
        await xavier[0].click(event.chat_id)
        if event.sender_id == FocusFusioN:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "xavier", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
