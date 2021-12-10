"""
    Version 2 of the solution.
    These functions works with a window to target the best starting point then move the multiple indexes of the windows
    to select a valid list of tracks that matches concert_premiere_length
"""

import copy


def _get_starting_sequence(
    list_of_tracks, concert_premiere_length, number_of_tracks_to_play
):
    """
    Return the optimal starting point to research the list of track
    """
    previous_diff = None

    for i in range(0, len(list_of_tracks) - (number_of_tracks_to_play - 1)):
        sequence_duration = sum(list_of_tracks[i : i + number_of_tracks_to_play])

        current_diff_duration = sequence_duration - concert_premiere_length

        if (i > 0) and (abs(previous_diff) < abs(current_diff_duration)):
                start_index = i - 1
                break

        previous_diff = current_diff_duration
        start_index = i

    return [i for i in range(start_index, start_index + number_of_tracks_to_play)]


def _decrease_first_possible_index(indexes):
    """
    Decrease the index of the element on the left of the window
    If not possible, it will move the next one from the left
    For example if we have
    (01[234]5678)
    the function will do
    (0[1]2[34]5678)
    """
    indexes_copy = copy.copy(indexes)

    for index, track_index in enumerate(indexes):
        if index == 0:
            if track_index - 1 >= 0:
                indexes_copy[index] = track_index - 1
                return indexes_copy
        else:
            if track_index - 1 > indexes[index - 1]:
                indexes_copy[index] = track_index - 1
                return indexes_copy

    return indexes_copy


def _increase_last_possible_index(tracklist, indexes):
    """
    Increase the index of the element on the right of the window
    If not possible, it will move the next one from the rigth
    For example if we have
    (01[234]5678)
    the function will do
    (01[23]4[5]678)
    """
    indexes_copy = sorted(indexes, reverse=True)
    updated_indexes = copy.copy(indexes_copy)

    for index, track_index in enumerate(indexes_copy):
        if index == 0:
            if track_index + 1 < len(tracklist):
                updated_indexes[index] = track_index + 1
                break
        else:
            if track_index + 1 < indexes_copy[index - 1]:
                updated_indexes[index] = track_index + 1
                break

    updated_indexes.sort()
    return updated_indexes


def _search_valid_sequence(tracklist, indexes, concert_premiere_length, tolerance):
    """
    Recursively search a sequance that matches the concert_premiere_length by moving the indexes
    """
    sequence_duration = sum([tracklist[i] for i in indexes])

    diff = sequence_duration - concert_premiere_length

    if (tolerance and abs(diff) <= tolerance) or (not tolerance and diff == 0):
        return True, indexes
    if diff < 0:
        new_indexes = _increase_last_possible_index(tracklist, indexes)
    if diff > 0:
        new_indexes = _decrease_first_possible_index(indexes)

    if indexes == new_indexes:
        return False, indexes

    return _search_valid_sequence(tracklist, new_indexes, concert_premiere_length, tolerance)


def get_matching_combination_of_tracks(
    tracklist, concert_premiere_length, tolerance=0, number_of_tracks_to_play=3
):
    """
    Return the list of track with a sum of length equal to concert_premiere_length
    """
    ordered_tracklist = sorted(tracklist, key=lambda x: x["length"])
    tracklist_length = len(ordered_tracklist)
    list_of_durations = [track["length"] for track in ordered_tracklist]

    if number_of_tracks_to_play > tracklist_length:
        raise ValueError(
            "The asked number of tracks to play is superior to the tracklist length."
        )

    starting_sequence = _get_starting_sequence(
        list_of_durations, concert_premiere_length, number_of_tracks_to_play
    )
    valid_sequence, sequence = _search_valid_sequence(
        list_of_durations, starting_sequence, concert_premiere_length, tolerance
    )

    return valid_sequence, [ordered_tracklist[i] for i in sequence]


def is_triplet_of_compatible_tracks_exists_enhanced_version(tracklist, concert_premiere_length, tolerance=0):
    """
    Convert the result of get_matching_combination_of_tracks in boolean
    """
    valid, _ = get_matching_combination_of_tracks(
        tracklist, concert_premiere_length, tolerance, number_of_tracks_to_play=3
    )

    return valid
