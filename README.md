# Instagram to Discord 💙

![IMAGE](https://i.ytimg.com/vi/bawUOnhbdLw/maxresdefault.jpg)

## Description 📝

This is a simple abstraction layer for the Instagram API, which allows you to get the latest posts from a user and send them to a Discord channel.

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
discord_instagram_poster.get_latest_photo(folder_path)
```