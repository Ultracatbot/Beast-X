#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.
# .tweet made for ultroid

# .uta ported from Dark-Cobra




from random import choice
from beastx.events import register

from telethon.errors import ChatSendInlineForbiddenError

def deEmojify(inputString: str) -> str:
    """Remove emojis and other non-safe characters from string"""
    return re.sub(EMOJI_PATTERN, "", inputString)

from . import *


@beast.on(beastx_cmd("tweet (.*)"))
async def tweet(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await e.client.inline_query("twitterstatusbot", text)
        await e.reply("New Tweet", file=results[0].document)
        await wai.delete()
    except Exception as m:
        await eor(e, str(m))


@beast.on(beastx_cmd("stick (.*)"))
async def tweet(e):
    if len(e.text) > 5 and e.text[5] != " ":
        return
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Emoji !`")
    results = await e.client.inline_query("sticker", text)
    num = choice(results)
    await e.reply("@sticker", file=num.document)
    await wai.delete()


@beast.on(beastx_cmd("stick (.*)"))
async def gglax_sticker(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give me Some Text !`")
    try:
        results = await e.client.inline_query("googlaxbot", text)
        await e.reply("Googlax", file=results[0].document)
        await wai.delete()
    except Exception as m:
        await eor(e, str(m))


@beast.on(beastx_cmd("frog (.*)"))
async def honkasays(e):
    wai = await eor(e, "`Processing...`")
    text = e.pattern_match.group(1)
    if not text:
        return await wai.edit("`Give Me Some Text !`")
    text = deEmojify(text)
    if not text.endswith("."):
        text += "."
    if len(text) <= 9:
        q = 2
    elif len(text) >= 14:
        q = 0
    else:
        q = 1
    try:
        res = await e.client.inline_query("honka_says_bot", text)
        await e.reply("Honka", file=res[q].document)
        await wai.delete()
    except Exception as er:
        await wai.edit(str(er))


@beast.on(beastx_cmd("uta (.*)"))
async def nope(doit):
    ok = doit.pattern_match.group(1)
    replied = await doit.get_reply_message()
    a = await eor(doit, "`Processing...`")
    if ok:
        pass
    elif replied and replied.message:
        ok = replied.message
    else:
        return await eor(
            doit,
            "`Sir please give some query to search and download it for you..!`",
        )
    sticcers = await doit.client.inline_query("Lybot", f"{(deEmojify(ok))}")
    await doit.reply(file=sticcers[0].document)
    await a.delete()


@beast.on(beastx_cmd("quot (.*)"))
async def quote_(event):
    IFUZI = event.pattern_match.group(1)
    if not IFUZI:
        return await eor(event, "`Give some text to make Quote..`")
    EI_IR = await eor(event, "`Processing...`")
    try:
        RE_ZK = await event.client.inline_query("@QuotAfBot", IFUZI)
        await event.reply(file=choice(RE_ZK).document)
    except Exception as U_TG:
        return await eor(EI_IR, str(U_TG))
    await EI_IR.delete()


CMD_HELP.update(
    {
        "inlinefun": """
        ✘ Commands Available -

• `.uta <search query>`
    Inline song search and downloader.

• `.gglax <query>`
    Create google search sticker with text.

• `.stic <emoji>`
    Get random stickers from emoji.

• `.frog <text>`
    make text stickers.

• `.tweet <text>`
    make twitter posts.

• `.quot <text>`
    write quote on animated sticker.
"""


    }
)
