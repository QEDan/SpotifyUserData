import json

def print_track(track):
    title = track['name']
    artist = track['artists'][0]['name']
    album = track['album']['name']
    return artist + " - " + title + " - " + album

def printList(tracks, sortKey, reverse=True, filename=None):
    sortedList = sorted(tracks, key=lambda k:k['track'][sortKey], reverse=reverse)
    if filename:
        f = open(filename, 'w')
    for track in sortedList:
        trackString = print_track(track['track']) + ' - ' \
            + str(track['track'][sortKey])
        if filename:
            f.write(trackString + '\n')
        else:
            print(trackString)
    if filename:
        f.close()




def loadTracks(filename="myTracks.json"):
    with open(filename) as f_obj:
        tracks = json.load(f_obj)
        return tracks
    return None


def main():
    #TODO Check if tracks load, if not, fetch them from API
    tracks = loadTracks()
    printList(tracks, "popularity", reverse=True, filename="popularity.txt")
    printList(tracks, "duration_ms", filename="duration.txt")
    printList(tracks, "name", filename="name.txt")

if __name__ == "__main__":
    main()