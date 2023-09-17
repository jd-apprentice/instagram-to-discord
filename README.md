# Instagram to Discord 💙

![IMAGE](https://i.ytimg.com/vi/bawUOnhbdLw/maxresdefault.jpg)


<a href="https://pypi.org/project/instagram-to-discord/"><img src="https://img.shields.io/badge/pip-install-blue"></a>
[![Supported Python versions](https://img.shields.io/pypi/pyversions/instagram-to-discord.svg?logo=python&logoColor=FFE873)](https://pypi.org/project/instagram-to-discord/)
[![PyPI downloads](https://img.shields.io/pypi/dm/instagram-to-discord.svg)](https://pypistats.org/packages/instagram-to-discord)
[![PyPI version](https://img.shields.io/pypi/v/instagram-to-discord.svg?logo=pypi&logoColor=FFE873)](https://pypi.org/project/instagram-to-discord/)
[![Licence](https://img.shields.io/github/license/jd-apprentice/pypistats.svg)](LICENSE)

## Description 📝

This is a simple abstraction layer for the Instagram API, which allows you to get the latest posts from a user and send them to a Discord channel.

## How it works? ⁉

![image](https://github.com/jd-apprentice/instagram-to-discord/assets/68082746/368fe303-f714-4572-86c5-064f08daeb19)

## Installation 📦

```bash
pip install instagram-to-discord
```

Or you can install it from the source code:

```bash
git clone https://github.com/jd-apprentice/instagram-to-discord.git
cd instagram-to-discord
pip install requirements.txt
```

## Usage 📸

#### Get data from instagram

For that we have a script called `fetch_posts.sh` localed in `utils/` folder. You can use it like this:

```bash
sh utils/fetch_posts.sh <username>
```

Or if you use Windows:

```ps1
script.bat <username>
```

This will create a folder with the name of the user and inside it will be the photos and videos that the user has uploaded.

```py
import os
from instagram-to-discord import DiscordInstagramPoster

current_folder = os.getcwd()
ask_directory = input("Enter the directory where the photos are stored (Your Instagram username): ")
folder_path = os.path.abspath(os.path.join(current_folder, ask_directory))
webhook_url = "YOUR_WEBHOOK_URL"

footer_text = "This is my title"
footer_url = "https://cdn.mos.cms.futurecdn.net/SeV6kiGf8ZsKGKNBrALzJN.jpg"
title = "!Sample Title!"

discord_instagram_poster = DiscordInstagramPoster({
    "webhook_url": webhook_url,
    "footer_text": footer_text,
    "footer_icon": footer_url,
    "title": title
})
discord_instagram_poster.get_latest_json(folder_path)
```
