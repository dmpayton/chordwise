=========
Chordwise
=========

Practice your guitar chords.

Screens
=======

Menu
----

::

    |-------|
    | x | 1 |
    |---+---|
    | 2 | 3 |
    |-------|

    x Logo
    1 Settings
    2 Chord list
    3 Practice mode


Chord list
----------

::

    Major
        A B C D
        E F G

    Minor
        Am Bm Cm Dm
        Em Fm Gm

    5 (Power)
        A5 B5 C5 D5
        E5 F5 G5

Tab to view full-size chord chart, long-press to toggle chord for practice.

Settings
--------

* BPM (number)
* Time (select: 1/4, 2/4, 3/4, 4/4*, 5/4, 6/8, 7/8, 8/8)
* Sound (switch)
* Left hand mode (switch)

Practice
--------

Carousel?

Next chord preview.

Play/Pause button.

PyFretboard
===========

PyFretboard is an idea for a library that will generate svg chord charts and
scales on the fly, rather than having a bunch of static low-res png's.

https://pypi.python.org/pypi/svgwrite

::

    import fretboard
    Am = fretboard.Chord('Am')
    D = fretboard.ChordChart(frets='xx0232', fingers='---132')
    scale = fretboard.Scale(root='C', scale=fretboard.PENTATONIC_MAJOR)
