#!/usr/bin/env python3

from discord import Client
import sys

chat_id = None
output = None

client = Client()

@client.event
async def on_ready():
    print('Logged in as: ' + client.user.name)
    print('------')
    channel = None
    for ch in client.private_channels:
        if ch.id == chat_id:
            channel = ch
            print('Channel found, retrieving history...')
            break
    else:
        sys.exit('Channel not found!')

    with open(output, 'w') as out:
        async for message in client.logs_from(channel, limit=9999999999999):
            out.write(message.timestamp.strftime('%d/%m/%Y %H:%M:%S%z') + ' - '
                      + message.author.name + ': ' + message.content + '\n')
    print('done')
    await client.close()


if __name__ == '__main__':

    argslen = len(sys.argv)
    if argslen == 1 or argslen < 4:
        print('Usage: python3 DiscordChatDownloader.py {user_token} {channel_id} {output_file}')
    elif argslen == 4:
        chat_id = sys.argv[2]
        output = sys.argv[3]
        client.run(sys.argv[1], bot=False)
