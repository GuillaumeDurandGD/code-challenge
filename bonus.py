from version_2 import get_matching_combination_of_tracks


def compute_total_length(tracklist):
    return sum([track["length"] for track in tracklist])


def get_first_match_regardless_nb_of_track(tracklist, concert_premiere_length):
    number_of_tracks_to_play = 0
    total_length = 0

    while total_length < concert_premiere_length:
        number_of_tracks_to_play += 1
        valid, sequence = get_matching_combination_of_tracks(
            tracklist, concert_premiere_length, number_of_tracks_to_play=number_of_tracks_to_play
        )

        if valid:
            return sequence

        total_length = compute_total_length(sequence)

    return None
