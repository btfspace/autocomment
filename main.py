from telethon import TelegramClient, events
from datetime import datetime
import configparser
import sys

config = configparser.ConfigParser()
config.read('config.ini', encoding = 'utf-8')
config = config['posthandler']
channels = config['channels'].split(',')

with TelegramClient('tgph', config['api_id'], config['api_hash']) as client:
	print('Checking the availability of the specified Telegram channels...')
	available = []
	for dialog in client.iter_dialogs():
		if not dialog.is_group and dialog.is_channel \
			and dialog.name in channels:
			available.append(dialog.name)

	if not available:
		print('None of the specified channels were found')
		sys.exit()

	if len(channels) != len(available):
		print(f'Finded {len(channels) - len(available)} from {len(channels)} channels')
	else:
		print('Finded all channels')
	print()

	@client.on(events.NewMessage(chats = tuple(available)))
	async def messageHandler(event):
		chat = await client.get_entity(event.message.chat_id)
		chat = chat.title
		time = datetime.now()
		strtime = f'{time.hour}:{time.minute}:{time.second}'

		if not event.replies or not event.replies.comments:
			return print(f'Received message from {chat} at {strtime} without comments, skipping')

		print(f'Received message from {chat} at {strtime}, writing comment...')
		await client.send_message(
			entity = chat, 
			message = config['messages'].split(':')[channels.index(chat)],
			comment_to = event
		)
		print('Success!\n')

	client.run_until_disconnected()