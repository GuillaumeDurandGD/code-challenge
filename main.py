import json


def get_triplet_of_compatible_tracks(list_of_tracks, concert_premiere_length, tolerance=0):
    list_of_tracks.sort(key=lambda x: x["length"])
    list_of_durations = [track["length"] for track in list_of_tracks]

    all_durations = []
    for idx1, duration_1 in enumerate(list_of_durations):
        for idx2, duration_2 in enumerate(list_of_durations):
            for idx3, duration_3 in enumerate(list_of_durations):
                if len({idx1, idx2, idx3}) == 3:
                    all_durations.append(sum([duration_1, duration_2, duration_3]))

    if not tolerance:
        return concert_premiere_length in all_durations

    return bool([duration for duration in all_durations if
                 (duration >= (concert_premiere_length - tolerance)) and (duration <= (concert_premiere_length + tolerance))])


if __name__ == "__main__":
    with open("data/songs.json", "r") as f:
        all_tracks = json.load(f)["all_tracks"]

    concert_premiere_length = 20
    tolerance = 0

    print(f"Does it exist a triplet of tracks that matches the concert_premiere_length ({concert_premiere_length} minutes) ?")
    print(get_triplet_of_compatible_tracks(all_tracks, concert_premiere_length, tolerance))
