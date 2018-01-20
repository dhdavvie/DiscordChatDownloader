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

    $ ./DiscordChatDownloader.py {user_token} {channel_id} {output_file}
    or
    $ python3 DiscordChatDownloader.py {user_token} {channel_id} {output_file}
    
You can get the `user_token` by following the steps [here](https://github.com/TheRacingLion/Discord-SelfBot/wiki/Discord-Token-Tutorial). 
You can get the `channel_id` by following the steps [here](https://support.discordapp.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID).
The `output_file` is simply the name of the file you wish to output the chat log to (ie `chatlog.txt`)
