# Import required methods
from requests import get
from json import loads
from shutil import copyfileobj
from mastodon import Mastodon

mastodon = Mastodon(
    access_token = 'token.secret',
    api_base_url = 'https://cfultz.com'
)


# Load the card data from Scryfall
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
special_characters=["$", "'","`","%","&","(",")",",",":","?","!","@",",",".","*","-"]
for i in special_characters:
    hTitle = mtg_title.replace(i,"")
    hSet = mtg_set.replace(i,"")
    hArtist = mtg_artist.replace(i,"")

# Set the Mastodon post information
media = mastodon.media_post("image.jpg", description="Card Name: " + mtg_title + "\n" + "Set: " + mtg_set + "\n" + "Description: "  + flavor + "\n" + "Artist: " + mtg_artist)

# Post the Toot
mastodon.status_post("#magicthegathering" + " " + "#mtg" + " " + "#" + hTitle.replace(" ", "") + " " + "#" + hArtist.replace(" ", ""),media_ids=media)
