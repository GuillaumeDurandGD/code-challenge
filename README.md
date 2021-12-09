# code-challenge


## Context 

We are creating more and more concerts / open stages as the first part of partner concerts to introduce talents from our platform!

However these first parts often have a limited time constraint *concert_premiere_length* in minutes and we must make sure to offer a succession of songs whose sum of the individual durations in minutes *Σtrack_length* = *concert_premiere_length*, *exactly*! 

Given a list of lengths (in minutes) of pieces of music [*track_length*] propose a function that returns a *Boolean True / False* indicating if there are 3 tracks whose sum duration is exactly the duration of *concert_premiere_length*.

We consider that  *concert_premiere_length*  and the durations  *track_length* are positive integers.

### Constraints:

- The spectators expect exactly 3 pieces in this concert first part *concert_premiere*
- We cannot offer the same song in double or triple, each song must be offered only once
- Optimize the runtime over the memory in the solution

### Technical specifications :

- Imposed technical stack:
    - Python 3
    - Third-party libraries, usage of threads/processes are not allowed
    - itertools is forbidden in this exercice, we want you to try building an approach using simple datastructures
    