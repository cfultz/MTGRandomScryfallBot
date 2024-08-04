# MTG Random Scryfall Bot 

The is a Mastodon bot that pulls a random Magic: The Gathering card from Scryfall and toots it correctly to a Mastodon instance with full description and hashtags.

![Screenshot](screenshot.jpg)

## Requirments
- Mastodon.py (pip install Mastodon)
- python-dotenv (pip install python-dotenv)


## How to Use
 
- Clone repository
- Create file called ``.env`` and place Mastodon Access Token and API URL inside
   ```
   token = RANDOMTOKENHERE
   url = MASTODONURLHERE
   ```


- Save and run the bot. eg: ``python MTGMastodonBot.py``

## TODO

- Add ability to have the bot respond to specific card search queries from users and reply
- ???
