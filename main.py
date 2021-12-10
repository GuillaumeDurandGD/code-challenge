import json
import timeit

from version_1 import is_triplet_of_compatible_tracks_exists
from version_2 import get_matching_combination_of_tracks, is_triplet_of_compatible_tracks_exists_enhanced_version
from bonus import get_first_match_regardless_nb_of_track

if __name__ == "__main__":
    with open("data/songs.json", "r") as f:
        all_tracks = json.load(f)["all_tracks"]

    concert_premiere_length = 20
    tolerance = 0

    print(
        f"Does it exist a triplet of tracks that matches the concert_premiere_length ({concert_premiere_length} minutes) ?"
    )
    print("Version 1 : ")
    print(
        is_triplet_of_compatible_tracks_exists(all_tracks, concert_premiere_length, tolerance)
    )
    print("Version 2 : ")
    print(
        is_triplet_of_compatible_tracks_exists_enhanced_version(all_tracks, concert_premiere_length, tolerance)
    )

    print()
    print("With version 2, it could be more interesting to call get_matching_combination_of_tracks to have the list of compatible tracks :")
    print(
        get_matching_combination_of_tracks(
            all_tracks, concert_premiere_length, tolerance, number_of_tracks_to_play=3
        )
    )

    print()
    print("How much time it takes to each function to do the process 1000 times (in seconds) ?")
    print("Version 1 :")
    print(
        timeit.timeit(
            lambda: is_triplet_of_compatible_tracks_exists(
                all_tracks, concert_premiere_length
            ),
            number=1000,
        )
    )
    print("Version 2 :")
    print(
        timeit.timeit(
            lambda: is_triplet_of_compatible_tracks_exists_enhanced_version(all_tracks, concert_premiere_length, tolerance),
            number=1000,
        )
    )

    print()
    print("Bonus: generalizing")
    print("Get the first compatible list of track regardless the number of track")
    print(get_first_match_regardless_nb_of_track(all_tracks, concert_premiere_length))

