# from environs import Env
#
# # environs kutubxonasidan foydalanish
# env = Env()
# env.read_env()
#
# # .env fayl ichidan quyidagilarni o'qiymiz
# BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
# ADMINS = env.list("ADMINS")  # adminlar ro'yxati
# IP = env.str("ip")  # Xosting ip manzili
#
# DB_USER = env.str("DB_USER")
# DB_PASS = env.str("DB_PASS")
# DB_NAME = env.str("DB_NAME")
# DB_HOST = env.str("DB_HOST")

import os

BOT_TOKEN = str(os.environ.get("BOT_TOKEN"))
ADMINS = os.environ.get("ADMINS").split(",")  # Splitting the admins into a list
IP = str(os.environ.get("ip"))
PROVIDER_TOKEN = str(os.environ.get("PROVIDER_TOKEN"))
