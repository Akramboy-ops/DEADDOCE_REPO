from .. import loader, utils, main
import asyncio

@loader.tds
class GlazBogaMod(loader.Module):
  strings = {"name": "GlazBoga"}
  """Eye of God by Nikita Xyrix
  https://t.me/zxcminimalized"""
  async def dnncmd(self, message):
    """Send uid to Eye of God
    .dnn <reply>"""
    reply = await message.get_reply_message()
    await message.edit("<code>You have 5 seconds to click Inline buttons in</code> @Anal_glaz_bot")
    try:
      await message.client.send_message(1713095454, str(reply.sender.id))
      await asyncio.sleep(2) 
      await asyncio.sleep(3)
      await asyncio.sleep(4)
      messages = await message.client.get_messages('Telegram')
      messages[0].click()
      await asyncio.sleep(5)
      messages2 = await message.client.get_messages(1713095454)
      await message.edit(str(messages2[0].message))
    except Exception as ex:
      await message.edit(str(ex))