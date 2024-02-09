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

# Set the Mastodon post information
media = mastodon.media_post("image.jpg","size:'372x520'", description="Card Name: " + mtg_title + "\n" + "Set: " + mtg_set + "\n" + "Description: "  + flavor + "\n" + "Artist: " + mtg_artist)

# Print Text
print (mtg_title)
print (mtg_set)
print (img_url)
print (flavor)


mastodon.status_post("#magicthegathering" + " " + "#mtg" + " " + "#" + mtg_title.replace(" ", "") + " " + "#" + mtg_set.replace(" ","") + " " + "#" + mtg_artist.replace(" ",""),media_ids=media)
