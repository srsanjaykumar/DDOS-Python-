from telethon import TelegramClient

name ="sanjay"
api_id = 12345
api_hash = '0123456789abcdef0123456789abcdef'


client = TelegramClient(name, api_id, api_hash)

async def main():
    # Now you can use all client methods listed below, like for example...
    await client.send_message('me', 'Hello to myself!')

with client:
    client.loop.run_until_complete(main())


