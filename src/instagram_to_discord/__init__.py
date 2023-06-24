import os
import json
import requests
import datetime
import lzma

class DiscordInstagramPoster:

    """
    options.webhook_url -- The Discord webhook URL. \n
    options.footer_text -- The footer text. \n
    options.footer_icon -- The footer icon URL. \n
    options.title -- The title of the message. \n

    This class is used to send a message to Discord.
    """

    def __init__(self, options: dict):
        self._webhook_url = options["webhook_url"]
        self.footer_text = options["footer_text"]
        self.footer_icon = options["footer_icon"]
        self.title = options["title"]

    def _send_message_to_discord(self, content: str, author_name: str, username: str, icon_url: str, photo_url: str) -> None:
        
        """
        content -- The content of the message. \n
        author_name -- The name of the author. \n
        username -- The username of the author. \n
        icon_url -- The icon URL of the author. \n
        photo_url -- The photo URL of the post. \n
        """
        
        current_datetime = datetime.datetime.now()
        serialized_datetime = current_datetime.isoformat()
        timestamp = serialized_datetime
        
        data = {
            "content": self.title,
            "embeds": [
                {
                    "description": content,
                    "color": None,
                    "author": {
                        "name": author_name,
                        "url": f'https://www.instagram.com/{username}',
                        "icon_url": icon_url
                    },
                    "footer": {
                        "text": self.footer_text,
                        "icon_url": self.footer_icon
                    },
                    "timestamp": timestamp,
                    "image": {
                        "url": photo_url
                    }
                }
            ],
            "attachments": []
        }

        try:
            response = requests.post(self._webhook_url, json=data)
        except requests.exceptions.MissingSchema:
            print("Invalid webhook URL.")
            return

        if response.status_code == 204:
            print("Message sent successfully.")
        else:
            print("Message could not be sent.")

    def get_latest_json(self, directory: str) -> None:
        """
        directory -- The directory where the files are stored.
        
        Get the latest JSON file with .json.xz extension from a directory.
        """

        files = os.listdir(directory)
        json_files = [file for file in files if file.endswith(".json.xz")]
        latest_json = max(json_files)

        json_path = os.path.join(directory, latest_json)

        with lzma.open(json_path, "rt") as file:
            json_content = file.read()

        json_data = json.loads(json_content)

        # Author information
        text_content = json_data["node"]["edge_media_to_caption"]["edges"][0]["node"]["text"]
        author_name = json_data["node"]["owner"]["full_name"]
        username = json_data["node"]["owner"]["username"]
        icon_url = json_data["node"]["owner"]["profile_pic_url"]
        photo_url = json_data["node"]["thumbnail_resources"][4]["src"]

        self._send_message_to_discord(text_content, author_name, username, icon_url, photo_url)