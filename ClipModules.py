from .. import loader, utils, main
import asyncio
import random
import datetime

def register(cb):
	cb(ClipModulesMod())
class ClipModulesMod(loader.Module):
	"""All Clip Userbot Modules in one FTG Module
	by @zxcminimalized sheesh"""
	strings = {'name': 'ClipModules'}
	async def helpclipcmd(self, message):
		"""Help?"""
		await message.edit("<code>Зачем тебе использовать help из другого юзербота в фтг? Лучше забудь.</code>")
	async def restartclipcmd(self, message):
		await message.edit("<code>Перезагрузка...</code>")
		await self.allmodules.commands["restart"](await message.respond("_"))
	async def chanceclipcmd(self, message):
		"""Random chance"""
		await message.edit("Вероятность составляет " + str(random.randint(1, 100)) + "%") 
	async def linkclipcmd(self, message):
		""".linkclip <reply>
		Ищет ссылку в тексте
		"""
		msg = await message.get_reply_message()
		msg = msg.message
		if('\n' in str(msg).split("https://")[1]):
			try:
				link = str(msg).split("https://")[1].split("\n")[0]
			except Exception as ex:
				await message.edit("Упс... Ссылка не найдена в тексте :(\nВозможная ошибка: <code>" + str(ex) + "</code>")
			else:
				await message.edit("Ссылка найдена! " + link)
		else:
			try:
				link = str(msg).split("https://")[1].split(" ")[0]
			except:
				await message.edit("Ошибка!")
			else:
				await message.edit("Ссылка найдена! " + link)
	async def sendclipcmd(self, message):
		"""Send message to user by reply
		.sendclip <reply>
		"""
		reply = await message.get_reply_message()
		msg = message.message
		msg = msg.split("sendclip ")[1]
		await message.client.send_message(int(reply.sender.id), msg)
		await message.edit("Отправлено!")
	async def timeclipcmd(self, message):
		delta = datetime.timedelta(hours=3, minutes=0)
		currentTime = (datetime.datetime.now() + delta).strftime('%Y-%m-%d %H:%M:%S')
		await message.edit(str(currentTime))
	async def delclipcmd(self, message):
		"""Delete message by reply"""
		reply = await message.get_reply_message()
		mid = reply.id
		cid = reply.sender.id
		await message.client.delete_messages(cid, mid)
		await message.delete()
	async def spambanclipcmd(self, message):
		await message.client.send_message('spambot', '/start')
		await asyncio.sleep(2)
		msgs = await message.client.get_messages('spambot')
		await message.edit(str(msgs[0].message))
	