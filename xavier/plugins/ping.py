import asyncio
import datetime

from . import *

@bot.on(xavier_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(xavier):
    if xavier.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(xavier, "`◤≛𝐏𝐎𝐍𝐆≛◢´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"◤≛𝐏𝐎𝐍𝐆≛◢\n\n    ✘  `{ms}`\n    ✘  __**𝐎𝐖𝐍𝐄𝐑**__ **:**  {xavier_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your χανιєя"
).add_warning(
  "✅ Harmless Module"
).add()

# xavier
