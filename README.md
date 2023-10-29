# TeleAccountManager
![Static Badge](https://img.shields.io/badge/Python-red?logo=Python) ![Static Badge](https://img.shields.io/badge/telegram-tool-blue?logo=telegram)


#### TeleAccountManager is a basic tool built with [Pyrogram](https://docs.pyrogram.org) to easily control multiple telegram account using only a command through your main account in the telegram

>**Note⚠️ TeleAccountManager
is Totally Not Responsible For Account Banning
Some New Telegram Accounts get banned instantly
using MtProto server's**

## Countrys to avoid
#### USA
#### Indonesia
#### south sudan

# How To Use
* ### first we need to open the config.json file, that will look like this
```
{
    "api_id": 123,
    "api_hash": "abc"
}
```
### you will need to replace api_id/api_hash with your credentials, you can get them from [Telegram Org](https://my.telegram.org/auth)

* ## In Terminal:
1. > git clone https://github.com/PythonNoob999/TeleAccountManager.git
1. > cd TeleAccountManager
1. > pip install -r requirements.txt
1. > python main.py

### After you run ```python main.py``` you will need to authorize your MAIN account to control all of your other accounts, to add other accounts run this command ```python add_account.py```

* ## In Your Main Telegram Account
### Now you are ready to type commands to control your accounts, Example:
```/{command} {arg1} {arg2}....```

* ## Available Commands
1. ### /send_message {number_of_accounts} {target_username} {message_to_be_sent}
    #### Example:
    > /send_message 5 @ahmed How are you doing

1. ### /send_contact {number_of_accounts} {target_username} {contact-info}
    #### Custom contact example:
    > /send_contact 5 @ahmed +2042181327-Kareem

    #### Account Contact example:
    > /send_contact 5 @ahmed me

1. ### /join_chats {number_of_accounts} {chats}
    #### example:
    > /join_chats 5 @chat1|chat2|https://t.me/+XYZ

1. ### /ref {number_of_accounts} {ref_link}
    #### example:
    > /ref 12 https://t.me/TestBot?start=93223221

* ## TODO
  * [ ] Add Feature to click on a message button
  * [x] Add feature to Set amount of accounts used



