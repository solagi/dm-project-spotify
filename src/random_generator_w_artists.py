import random
import requests
import string
import urllib
import pandas as pd

#  Based on a tutorial from here: https://www.youtube.com/watch?v=uXf7IRDIQS4

# Get Token here: https://developer.spotify.com/console/get-track/?id=&market=
# This token needs to be updated every time before runnning the program.
api_token = 'BQBeVBuu5Yb5Dl9SZiowPtALTbUIvbUVoI-J-YMuqZfSHDkgHACSmlHwBDvGd7fSoado5gwbHVNCt0FUn-u7iFrJmRdDFQRqZfztMrEs69nIi_5_QJjTjdhuFybcX6qrPCWcQservjZM6z0'

def get_ranom_50():
	wildcard = f'%{random.choice(string.ascii_lowercase)}%'
	query = urllib.parse.quote(wildcard)
	offset = random.randint(0, 2000)
	url = f"https://api.spotify.com/v1/search?q={query}&offset={offset}&type=track"
	response = requests.get(
		url,
		headers={
			"Content-Type": "application/json",
			"Authorization": f"Bearer {api_token}"
		}
	)
	response_json = response.json()

	random_tracks = [track for track in response_json['tracks']['items']]

	return random_tracks

def get_data():
	randoms = {'songs': [""], 'artists':[], 'featurings':[]}
	track_ids =[]
	artists = []
	featurings = []
	random_50 = []
	while(len(randoms["songs"]) < 1000):
		try:
			random_50 = get_ranom_50()
			track_ids.extend([track["id"] for track in random_50])
			artists.extend([track["artists"][0]["name"] for track in random_50])
			featurings.extend([len(track["artists"]) for track in random_50])	
			randoms = {'songs': track_ids, 'artists':artists, 'featurings':featurings}
		

		except:
			pass
		
	return randoms


def get_random_df():
	data = get_data()
	random_df = pd.DataFrame({'PlaylistID': 'None', 'PlaylistTitle': 'No Playlist', 'TrackID': data["songs"], "MainArtist": data["artists"], "NoFeaturing": data["featurings"], 'Features': ''})

	return random_df
