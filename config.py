from os import path, mkdir, remove, listdir


class New_User():
    """The class is designed to create a new user folder to make it easier to accept images."""

    def __init__(self, user_id: str) -> str:
        self.user_id = str(user_id)
        self.way = path.abspath(__name__).replace(__name__, "")+'photos/'
        self.user_image = self.way+self.user_id

    def catalog(self):
        if not path.exists(self.way):
            mkdir(self.way)
        if not path.exists(self.user_image):
            mkdir(self.user_image)
            return self.user_image
        return self.user_image

    def clear_catalog(self):
        for file in listdir(self.user_image):
            remove(path.join(self.user_image, file))


class Settings_config(New_User):
    """The class is designed to read settings from config.txt file"""

    def __init__(self, user_id=None, token=True) -> str:
        super().__init__(user_id)
        self.token = token

    def check_settings(self):
        if not path.exists(self.way.replace("photos/", "config.txt")):
            with open("config.txt", "w", encoding='UTF-8') as f:
                f.write("Hi my friend! This is the bot settings!!!\n")
                f.write("Please do not change this file because I decided not to complicate the code and made the bot setup positional on the lines of this file\n")
                f.write("\nBOT TOKEN API: ")

    def TOKEN_API(self):
        with open("config.txt", "r", encoding='UTF-8') as f:
            self.token = f.readlines()[3].split()[-1]
            return self.token
