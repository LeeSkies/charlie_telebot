# charlie_telebot

Get a PaLM API key here: https://developers.generativeai.google/tutorials/setup

Get a telegram bot token here: https://t.me/BotFather

Get your telegram username from your account

Open an .env file and set the corresponding variables:

BASE_URL=https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateMessage?key=
PALM_KEY=your_palm_key
ADMIN=your_account_username
BOT_TOKEN=your_bot_token

Now you have two options:

1) Dockerize the bot using the Dockerfile -

* Note that the base image is arm based.

2) Run the bot locally -
   
* Clone the repository
* Run python3 -m venv venv
* Run source venv/bin/activate
* Run pip install -r requirements.txt
* Run python bot.py
