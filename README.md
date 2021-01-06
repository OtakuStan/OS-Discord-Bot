# OS Discord Bot
A Discord BOT for OtakuStan to help manage OtakuStan's discord servers easily and seamlessly.

## About
This Discord Bot helps you to manage various aspects on your discord server, interact with members and have fun with your server members to keep your server ever active.

This is made is Python and python discord library Discord.py

## Technologies
- Python
- Discord.py

## Invite
Invite Link for Gift Bot will be added soon.

<!-- ## How To Use Gift
- !gifth: Provides you with a list of all the bot's available commands
- !giveaway: Setup your Giveaway.
- !fifreroll: Reroll The Giveaway to select a new winner use !gifreroll #channel-name Message Id of the message
- !giftdel: Cancel the Giveaway by specifying the giveaway channel name and the message id: use !giftdel #channel_name Id of the giveaway message
## Suggestions and Bug Reports
Suggestions, requests and bug reports are always welcomed. If you have any don't forget to leave them in the issues section. -->

## Work In progress
 - Setup
    * [x] Create The Bot Class
    * [x] Connect To testing servers
    * [x] Send First Message

 - Add Commands
    * [ ] Greetings Command
    * [ ] Rules Commands
    * [ ] Member Info Commands

 - Deploy
    * [ ] Deploy To server

 More To be Added soon....

## Running The Bot on Your System
### Using Virtual Environment
- Clone it on your System
```
git clone https://github.com/OtakuStan/OS-Discord-Bot.git
```
- Go to the Working Directory
```
cd Otakustan_Bot/
```
- Creating And Activating Virtual Environment
```
py -m venv env / python3 -m venv env

env/scripts/activate
```
- Install dependencies
```
pip installl -r requirements.txt
```

- Add token
```
touch lib/bot/token
```

Add the Token to the token file

- Run the Bot
```
python os.py
```

### Using Environment Variable

You need to have Discord py installed globally in your System. Add the token to your .env file. Then in the run method of bot file simply initialize token from the environment variable


