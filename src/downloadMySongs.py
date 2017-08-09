import sys
import spotipy
import spotipy.util as util
import json
import operator

scope = 'user-library-read'

def print_track(track):
    title = track['name']
    artist = track['artists'][0]['name']
    album = track['album']['name']
    return artist + " - " + title + " - " + album

def printList(tracks, sortKey, reverse=True, filename=None):
    sortedList = sorted(tracks, key=lambda k:k['track']['popularity'], reverse=reverse)
    if filename:
        f = open(filename, 'w')
    for track in sortedList:
        if filename:
            f.write(print_track(track['track']) + '\n')
        else:
            print(print_track(track['track']))
    if filename:
        f.close()



def download_all_user_tracks(limit=50):
    offset = 0
    items = list()
    results = {}
    while(True):
        results = sp.current_user_saved_tracks(limit=limit, offset=offset)
        items += results['items']
        offset += limit
        if len(results['items']) < limit:
            break
    return items

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    tracks = download_all_user_tracks()
    printList(tracks, "popularity", reverse=True, filename="popularity.txt")
    with open('myTracks.json', 'w') as fp:
        json.dump(tracks, fp)


else:
    print("Can't get token for", username)


