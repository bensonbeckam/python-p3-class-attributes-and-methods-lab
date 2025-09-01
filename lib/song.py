class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Update song count
        Song.count += 1

        # Add genre to list (no duplicates)
        if genre not in Song.genres:
            Song.genres.append(genre)

        # Add artist to list (no duplicates)
        if artist not in Song.artists:
            Song.artists.append(artist)

        # Update genre count
        if genre in Song.genre_count:
            Song.genre_count[genre] += 1
        else:
            Song.genre_count[genre] = 1

        # Update artist count
        if artist in Song.artist_count:
            Song.artist_count[artist] += 1
        else:
            Song.artist_count[artist] = 1
