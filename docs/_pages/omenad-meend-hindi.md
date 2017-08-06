---
title: Omenad Meend Hindi
layout: splash
permalink: /omenad-meend-hindi/
header:
    overlay_color: "000"
    overlay_filter: "0.5"
    overlay_image: /assets/images/omenad-meend-hindi-header.jpg
---

{% include toc title="Overview" %}

# Introduction

# Glyphs

## Swar (Notes)

### Regular Notes

For the seven natural notes, use lower case keys corresponding to each note.

{:.keymap.meend-hindi}
| Note | Key | Bhatkhande |
|------|-----|------------|
| Sa   | `s` | s          |
| Re   | `r` | r          |
| Ga   | `g` | g          |
| Ma   | `m` | m          |
| Pa   | `p` | p          |
| Dha  | `d` | d          |
| Ni   | `n` | n          |

### Variant Notes

In Indian Music, Ma is the only note with a Sharp variant. Re, Ga, Dha, and Ni have Flat variants. These are typed using capital letters.

{:.keymap.meend-hindi}
| Note     | Key | Bhatkhande |
|----------|-----|------------|
| Flat Re  | `R` | R          |
| Flat Ga  | `G` | G          |
| Sharp Ma | `M` | M          |
| Flat Dha | `D` | D          |
| Flat Ni  | `N` | N          |

### Octaves

A dot symbol `·` above or below a note signifies upper or lower octave respectively. The absence of the dot signifies middle octave.

{:.keymap.meend-hindi}
| Note           | Key  | Bhatkhande |
|----------------|------|------------|
| Lower Sharp Ma | `Ml` | Ml         |
| Middle Pa      | `p`  | p          |
| Upper Flat Dha | `Du` | Du         |

## Mizrab Ke Bol (Strokes)

All Strokes take the same space as Notes, except for Dir which takes the space for two Notes.

{:.keymap.meend-hindi}
| Stroke | Key | Bhatkhande  |
|--------|-----|-------------|
| Da     | `;` | ;           |
| Ra     | `'` | {{ "'" }}   |
| Daa    | `[` | [           |
| Raa    | `]` | ]           |
| Dir    | `\` | \           |
| Khali  | `-` | -           |

## Meend

The Meend characters take zero space, and must be typed immediately before a note from any octave. The Meend characters, are to be used as a set.

A valid Meend sequence is that which begins with the Meend Start character `q`, is followed by one note from any octave, followed by zero or more pairs of a Meend Continue character `w` and one note from any octave, and finished with a Meend End character `e` followed by one note from any octave. The Meend Stroke character, made with a `W`, is used to indicate a note on which a stroke is necesary to keep the meend going.

{:.keymap.meend-hindi}
| Meend Character | Key | Bhatkhande |
|-----------------|-----|------------|
| Meend Start     | `q` | q          |
| Ghaseet Start   | `Q` | Q          |
| Meend Continue  | `w` | w          |
| Meend Stroke    | `W` | W          |
| Meend End       | `e` | e          |
| Ghaseet End     | `E` | E          |

The following examples illustrate how a valid Meend sequence is visually cohesive in its representation of a continuous pull:

{:.keymap.meend-hindi}
| Key Strokes  | Bhatkhande |
|--------------|------------|
| `qgwGwRwGer` | qgwGwRwGer |
| `qger`       | qger       |
| `qgwGlwGeru` | qgwGlwGeru |
| `qgwpWMep`   | qgwpWMep   |

Please note that while the third example above is syntactically correct, such a Meend is impossible in Sitars, on which pulling even a five-note Meend is extremely difficult.

## Murki

Parentheses around a note indicate a quick movement from the note to the adjescent ones and back to the original note. For example, <span class="omenad-meend-hindi">(p)</span> translates to <span class="omenad-meend-hindi">pMdp</span>.

{:.keymap.meend-hindi}
| Key Strokes | Bhatkhande |
|-------------|------------|
| `(p)`       | (p)        |

## Kan

Kan and Krintan rely on the word processing ability to **superscript**. Since the width of these superscripted characters depends on the word processor, in certain cases it can break the monospacing of the font.

{:.keymap.meend-hindi}
| Key Strokes              | Bhatkhande          |
|--------------------------|---------------------|
| `<sup>``m``</sup>``p`    | <sup>m</sup>p       |
| `d``<sup>``g``</sup>``m` | d<sup>g</sup>m      |

The ability to add predictable superscripting is planned for the future.

## Krintan

Krintan is Kan repeated twice, thrice, four times in a single stroke of the Mizrab, represented by the numeral after the Kan note.

{:.keymap.meend-hindi}
| Key Strokes              | Bhatkhande          |
|--------------------------|---------------------|
| `<sup>``m3``</sup>``p`   | <sup>m3</sup>p      |

## Miscellaneous

{:.keymap.meend-hindi}
| Type      | Key | Bhatkhande |
|-----------|-----|------------|
| Sam       | `x` | x          |
| Long Dash | `_` | _          |
| Comma     | `,` | ,          |
| Plus      | `+` | +          |
| 0         | `0` | 0          |
| 1         | `1` | 1          |
| 2         | `2` | 2          |
| 3         | `3` | 3          |
| 4         | `4` | 4          |
| 5         | `5` | 5          |
| 6         | `6` | 6          |
| 7         | `7` | 7          |
| 8         | `8` | 8          |
| 9         | `9` | 9          |

# Layout

# Web Use
