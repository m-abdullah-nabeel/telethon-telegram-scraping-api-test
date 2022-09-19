from telethon import TelegramClient

# Use your own values from my.telegram.org
api_id = 18261842
api_hash = '70c3d71ef896718195312818ac94aa89'
bot_token = '18261842:70c3d71ef896718195312818ac94aa89'

client = TelegramClient('anon', api_id, api_hash)

# bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

# # The first parameter is the .session file name (absolute paths allowed)
# with TelegramClient('anon', api_id, api_hash) as client:
#     client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))

# with bot: 
#     print("Hello, bot!")

async def main():
    # Getting information about yourself
    me = await client.get_me()

    # "me" is a user object. You can pretty-print
    # any Telegram object with the "stringify" method:
    print(me.stringify())

    # When you print something, you see a representation of it.
    # You can access all attributes of Telegram objects with
    # the dot operator. For example, to get the username:
    username = me.username
    print(username)
    print(me.phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # You can send messages to yourself...
    # await client.send_message('me', 'Hello, myself!')
    # # ...to some chat ID
    # await client.send_message(-1001485211990, 'Hello, group!')
    # # ...to your contacts
    # await client.send_message('+923063217103', 'Hello')
    # # ...or even to any username
    # await client.send_message('nooraa2005', 'Hello, friend!')
    # await client.send_message('Katt031', 'Hello, friend!')
    # await client.send_message('bella21121', 'Hello, friend!')

    # You can, of course, use markdown in your messages:
    message = await client.send_message(
        '-1001485211990',
        '**Hello**, `Group`, __See my portfolio__  '
        '[My Website](https://dr-abdullah-nabeel.web.app)!',
        link_preview=True
    )

    # Sending a message returns the sent message object, which you can use
    print(message.raw_text)

    # You can reply to messages directly if you have a message object
    await message.reply('Cool!')

    # Or send files, songs, documents, albums...
    # await client.send_file('me', '/home/me/Pictures/holidays.jpg')

    # You can print the message history of any chat:
    async for message in client.iter_messages('-1001485211990'):
        print(message.id, message.text)

        # You can download media from messages, too!
        # The method will return the path where the file was saved.
        if message.photo:
            path = await message.download_media()
            print('File saved to', path)  # printed after download is done

with client:
    client.loop.run_until_complete(main())
