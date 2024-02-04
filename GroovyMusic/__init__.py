from GroovyMusic.core.bot import Anony
from GroovyMusic.core.dir import dirr
from GroovyMusic.core.git import git
from GroovyMusic.core.userbot import Userbot
from GroovyMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
