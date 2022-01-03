from .. import loader, utils, main
# Чел, ну ты и еблан...

def register(cb):
	cb(ZalupaMod())
class ZalupaMod(loader.Module):
	strings = {"name": "BadCrypt"}
	"""Худший модуль для шифровки за историю человечества
	Remake by @zxcminimalized
	Nedomodule by Artur Zalupov
	"""
	async def clcmd(self, message):
		"""Недонашифровать хуету"""
		text = message.message.split("cl ")[1]
		ru_keys = """ёйцукенгшщзхъфывапролджэячсмитьбю.Ё"№;%:?ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭ/ЯЧСМИТЬБЮ,"""
		en_keys = """異體字体♬♝♞♟γδεηθκλμνZXM∩SάằẫăǽẳßβЂ฿™đďÐðӘҾΣĤĦҤḦĥћҥḧŒœØỢ$śşŝšṧṩᵴﮐ§♌♍♎♏♐♑♒♓✵✶✷✸✹"""
		if text == "":
			if message.reply_to_message:
				reply_text = message.get_reply_message().message
				change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
				reply_text = str.translate(reply_text, change)
				await message.edit(reply_text)
			else:
				await message.edit("Текст отсутствует")
				await asyncio.sleep(3)
				await message.delete()
		else:
			change = str.maketrans(ru_keys + en_keys, en_keys + ru_keys)
			text = str.translate(text, change)
			await message.edit(text)