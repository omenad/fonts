---
title: Ome Swarlipi
layout: single
permalink: /ome-swarlipi/
header:
    overlay_color: "000"
    overlay_filter: "0.5"
    overlay_image: /assets/images/ome-swarlipi-header.jpg
sidebar:
    nav: "sidebar"
---

{% include toc title="Overview" %}

# Introduction

# Glyphs

Glyphs are visual components of a font. Here we list all the glyphs supported in the font, along with the keystrokes needed to evoke them.

## Swar (Notes)

### Regular Notes

For the seven natural notes, use lower case keys corresponding to each note.

{:.keymap.swarlipi}
| Note | Key | Swarlipi |
|------|-----|----------|
| Sa   | `s` | s        |
| Re   | `r` | r        |
| Ga   | `g` | g        |
| Ma   | `m` | m        |
| Pa   | `p` | p        |
| Dha  | `d` | d        |
| Ni   | `n` | n        |

### Variant Notes

In Indian Music, Ma is the only note with a Sharp variant. Re, Ga, Dha, and Ni have Flat variants. These are typed using capital letters.

{:.keymap.swarlipi}
| Note     | Key | Swarlipi |
|----------|-----|----------|
| Flat Re  | `R` | R        |
| Flat Ga  | `G` | G        |
| Sharp Ma | `M` | M        |
| Flat Dha | `D` | D        |
| Flat Ni  | `N` | N        |

### Octaves

A dot symbol `·` above or below a note signifies upper or lower octave respectively. The absence of the dot signifies middle octave.

{:.keymap.swarlipi}
| Note           | Key  | Swarlipi |
|----------------|------|----------|
| Lower Sharp Ma | `Ml` | Ml       |
| Middle Pa      | `p`  | p        |
| Upper Flat Dha | `Du` | Du       |

## Mizrab Ke Bol (Strokes)

All Strokes take the same space as Notes, except for Dir which takes the space for two Notes.

{:.keymap.swarlipi}
| Stroke | Key | Swarlipi  |
|--------|-----|-----------|
| Da     | `;` | ;         |
| Ra     | `'` | {{ "'" }} |
| Daa    | `[` | [         |
| Raa    | `]` | ]         |
| Dir    | `\` | \         |
| Khali  | `-` | -         |

### Special Instructions for Word Processors

A number of word processors, including Microsoft Word, Apple Pages, and LibreOffice, will sometimes automatically replace a straight quotation mark `'` ([`U+0027` Apostrophe](http://graphemica.com/%27)) with a typographic quote `’` ([`U+2019` Right Single Quotation Mark](http://graphemica.com/%E2%80%99)). This facility is called "Smart Quotes".

In previous versions, the Ome Swarlipi <span class="ome-swarlipi">&apos;</span> corresponded to the former, not the latter, and having Smart Quotes enabled made that character disappear. This was fixed in [version 2.1.0](https://github.com/omenad/fonts/releases/tag/2.1.0). Please upgrade to the latest version to remedy this issue.

## Dividers

Each divider takes the space equivalent to one note. Smaller dividers typed by `a` divide beats, whereas larger dividers typed by `A` divide phases. The larger dividers when written exactly under each other in consecutive lines join together, providing a simple mechanism for making columns.

The usage of small dividers allows an arbitrary number of notes to be written in one beat. This is much harder to do in other lipi-s such as Bhātkhanḍē.

{:.keymap.swarlipi}
| Type of Divider | Key | Swarlipi |
|-----------------|-----|----------|
| Beat Divider    | `a` | a        |
| Phase Divider   | `A` | A        |

## Matra (Beats)

Numerical beats can be represented by numbers. Special beats, such as _sam_ and _khali_ are represented by `x` and `+` respectively.

{:.keymap.swarlipi}
| Matra | Key | Swarlipi |
|-------|-----|----------|
| Sam   | `x` | x        |
| Khali | `+` | +        |

## Meend

The Meend characters take zero space, and must be typed immediately before a note from any octave. The Meend characters, are to be used as a set.

A valid Meend sequence is that which begins with the Meend Start character `q`, is followed by one note from any octave, followed by zero or more pairs of a Meend Continue character `w` and one note from any octave, and finished with a Meend End character `e` followed by one note from any octave. The Meend Stroke character, made with a `W`, is used to indicate a note on which a stroke is necesary to keep the meend going.

{:.keymap.swarlipi}
| Meend Character | Key | Swarlipi |
|-----------------|-----|----------|
| Meend Start     | `q` | q        |
| Meend Continue  | `w` | w        |
| Meend Stroke    | `W` | W        |
| Meend End       | `e` | e        |

The following examples illustrate how a valid Meend sequence is visually cohesive in its representation of a continuous pull:

{:.keymap.swarlipi}
| Key Strokes  | Swarlipi   |
|--------------|------------|
| `qswrwgem`   | qswrwgem   |
| `qger`       | qger       |
| `qRwGwmep`   | qRwGwmep   |
| `qDlwNlWser` | qDlwNlWser |

## Gamak

Squiggle above a preceeding note indicates a quick vibration of sound. It can be applied to any note with `v`.

{:.keymap.swarlipi}
| Key Strokes | Swarlipi |
|-------------|----------|
| `gv`        | gv       |
| `Mlv`       | Mlv      |

## Murki

Parentheses around a note indicate a quick movement from the note to the adjescent ones and back to the original note. For example, <span class="ome-swarlipi">(p)</span> can translate to <span class="ome-swarlipi">Mpdp</span>, or <span class="ome-swarlipi">dpMp</span>, or <span class="ome-swarlipi">pMdp</span>, depending on the artist's interpretation.

{:.keymap.swarlipi}
| Key Strokes | Swarlipi |
|-------------|----------|
| `(p)`       | (p)      |


## Kan

Kan and Krintan rely on the word processing ability to **superscript**. Since the width of these superscripted characters depends on the word processor, in certain cases it can break the monospacing of the font.

{:.keymap.swarlipi}
| Key Strokes              | Swarlipi            |
|--------------------------|---------------------|
| `<sup>``m``</sup>``p`    | <sup>m</sup>p       |
| `d``<sup>``g``</sup>``m` | d<sup>g</sup>m      |

The ability to add predictable superscripting is planned for the future.

## Krintan

Krintan is Kan repeated twice, thrice, four times in a single stroke of the Mizrab, represented by two, three, or four vertical bars using `a` after the superscripted character. To save space, numerals may also be used instead of the bars.

{:.keymap.swarlipi}
| Key Strokes              | Swarlipi            |
|--------------------------|---------------------|
| `<sup>``maaa``</sup>``p` | <sup>maaa</sup>p    |
| `<sup>``m3``</sup>``p`   | <sup>m3</sup>p      |

## Miscellaneous

{:.keymap.swarlipi}
| Type      | Key | Swarlipi |
|-----------|-----|----------|
| Iteration | `#` | #        |
| Long Dash | `_` | _        |
| Comma     | `,` | ,        |
| 0         | `0` | 0        |
| 1         | `1` | 1        |
| 2         | `2` | 2        |
| 3         | `3` | 3        |
| 4         | `4` | 4        |
| 5         | `5` | 5        |
| 6         | `6` | 6        |
| 7         | `7` | 7        |
| 8         | `8` | 8        |
| 9         | `9` | 9        |

# Layout

```swarlipi
# sarraggappAddasusuaruruaguguAruruasusuaddappAggarrasas
  [a\a\a\A\a\a\a\A\a\a\a\A\a\a[a]
  x         A5          A+          A13

  dladlsa-sarAga-adladlsA-saraga-Adladlsa-sarAg
  [a'[a-'a[A[a-a[a'[A-'a[a[a-A[a'[a-'a[A[
  x        A5       A+       A13       Ax
```

_Raga Bhupali: Tora 1, from [Sitar Compositions in Ome Swarlipi](http://www.lulu.com/us/en/shop/ragini-trivedi/sitar-compositions-in-ome-swarlipi/hardcover/product-15163843.html) by [Dr. Ragini Trivedi](http://raginitrivedi.com)_

Swarlipi layout can be done in pure text form, without needing any additional formatting.

Each line of music has three parallel rows of notation to represent it.
The first row represents notes (the movement of the left hand on sitar).
The second row represents strokes (the movement of the right hand on sitar).
The third row represents beats (timing of movements).

The <span class="ome-swarlipi">#</span> in the first row represents that this is where the line starts.
Each of the sixteen beats in Teen Tal is separated by <span class="ome-swarlipi">a</span>, and every subdivision by <span class="ome-swarlipi">A</span>. These are kept in the same column in each row to make the rows align.

In the third row we use spaces for the whitespace. Each space in the font has the same width as every character, making it easy to line up.

# Web Use

For usage on the web, add the following block to the `<head>` section:

```html
<link rel="stylesheet" href="https://webfonts.omenad.net/fonts.css">
```

You can then use the `.ome-swarlipi` class on any element to use the font:

```html
<pre class="ome-swarlipi">
# sarraggappAddasusuaruruaguguAruruasusuaddappAggarrasas
  [a\a\a\A\a\a\a\A\a\a\a\A\a\a[a]
  x         A5          A+          A13
</pre>
```

It is recommended to use `<pre>` or `<code>` to preserve whitespace in the compositions.

If you'd like to do something more interesting, you can use `ome_swarlipi` as the `font-family` in a more complicated style class:

```css
.language-swarlipi {
  font-family: 'ome_swarlipi';
  font-size: 1.4em;
  line-height: 1.6em;
}
```

Webfonts are currently not included in the download package, and they are not licensed for self-hosted web use. Usage from the above URL is free and unlimited at this time.
