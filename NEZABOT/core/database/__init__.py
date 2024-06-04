from motor.motor_asyncio import AsyncIOMotorClient

from NEZABOT.config import MONGO_URL

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client.ilauserbot

from NEZABOT.core.database.expired import *
from NEZABOT.core.database.notes import *
from NEZABOT.core.database.premium import *
from NEZABOT.core.database.reseller import *
from NEZABOT.core.database.saved import *
from NEZABOT.core.database.NEZABOT import *
from NEZABOT.core.database.pref import *
from NEZABOT.core.database.otp import *
from NEZABOT.core.database.gbans import *
from NEZABOT.core.database.setvar import *
from NEZABOT.core.database.logger import *
from NEZABOT.core.database.bcast import *
from NEZABOT.core.database.permit import *

