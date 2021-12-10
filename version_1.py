"""
    Version 1 of the solution.
    Naive function with bad performance
    Complexity of O(n^3)
"""


def is_triplet_of_compatible_tracks_exists(
    list_of_tracks, concert_premiere_length, tolerance=0
):
    """
    Check if a triplet of track can matches concert_premiere_length
    :return: boolean: True if it exists a combination of track that matches the concert_premiere_length, return False otherwise
    """
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

    return bool(
        [
            duration
            for duration in all_durations
            if (duration >= (concert_premiere_length - tolerance))
            and (duration <= (concert_premiere_length + tolerance))
        ]
    )
