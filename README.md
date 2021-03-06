# DiscordChatDownloader
A python tool for downloading the entirety of a chat log you have access to.

## UNIX Setup
Requires [Python 3.5+](https://www.python.org/downloads/release/python-350/).  

Install the [discord.py](https://github.com/Rapptz/discord.py/) library:  

    $ python3 -m pip install -U discord.py
    
Then clone the directory and make file executable:

    $ git clone https://github.com/dhdavvie/DiscordChatDownloader.git
    $ cd DiscordChatDownloader
    $ chmod +x DiscordChatDownloader.py
    
Usage:

    $ ./DiscordChatDownloader.py {bot_token} {channel_id} {output_file}
    or
    $ python3 DiscordChatDownloader.py {bot_token} {channel_id} {output_file}
    
This is intended to be used with a Bot Token! [Here](https://github.com/Chikachi/DiscordIntegration/wiki/How-to-get-a-token-and-channel-ID-for-Discord) are instructions on getting a Bot Token.
You can get the `channel_id` by following the steps [here](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID).
The `output_file` is simply the name of the file you wish to output the chat log to (ie `chatlog.txt`)
