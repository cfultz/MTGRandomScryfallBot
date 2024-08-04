import random
import os
from requests import get
from json import loads
from shutil import copyfileobj
from mastodon import Mastodon
from dotenv import load_dotenv

load_dotenv()

mastodon = Mastodon(
    access_token = os.getenv("token"),
    api_base_url = os.getenv("url")
)


# Use this only if you want a specific set.
# You need to set both the code and find out how many total cards are in the set
# setname = "sld"
# cardid = random.randint(0,1718)

# Load the card data from Scryfall

#This is for a specific set
card = loads(get(f"https://api.scryfall.com/cards/{setname}/{cardid}").text)

# This is the actual random card: 
 card = loads(get(f"https://api.scryfall.com/cards/random?format=image.json").text)

# Get the image URL
img_url = card['image_uris']['large']

# Get card title
mtg_title = card['name']

# Artist name
mtg_artist = card['artist']

# Get flavor text
flavor = card['oracle_text']

# Get card set
mtg_set = card['set_name']

# Save the image
with open('image.jpg', 'wb') as out_file:
    copyfileobj(get(img_url, stream = True).raw, out_file)

# Removing weird or unusable characters for hashtags
special_characters=["$","'","`","%","&","(",")",":","?","!","@","*"," "]
for i in special_characters:
    hTitle = mtg_title.replace(i,"")
    hSet = mtg_set.replace(i,"")
    hArtist = mtg_artist.replace(i,"")

    hArtist = hArtist.replace('.', '')
    hArtist = hArtist.replace(',', '')
    hArtist = hArtist.replace("'", '')
    hTitle = hTitle.replace(',',"")
    hTitle = hTitle.replace('.',"")
    hTitle = hTitle.replace(':',"")
    hTitle = hTitle.replace("'","")
    hSet = hSet.replace('.','')
    hSet = hSet.replace(',','')

# Set the Mastodon post information
media = mastodon.media_post("image.jpg", description="Card Name: " + mtg_title + "\n" + "Set: " + mtg_set + "\n" + "Description: "  + flavor + "\n" + "Artist: " + mtg_artist)
