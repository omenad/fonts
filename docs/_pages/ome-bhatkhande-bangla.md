---
title: Ome Bhatkhande Bangla
layout: single
permalink: /ome-bhatkhande-bangla/
header:
    overlay_color: "000"
    overlay_filter: "0.5"
    overlay_image: /assets/images/ome-bhatkhande-bangla-header.jpg
sidebar:
    nav: "sidebar"
---

{% include toc title="Overview" %}

# Introduction

# Glyphs

## Swar (Notes)

### Regular Notes

For the seven natural notes, use lower case keys corresponding to each note.

{:.keymap.bhatkhande-bangla}
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

{:.keymap.bhatkhande-bangla}
| Note     | Key | Bhatkhande |
|----------|-----|------------|
| Flat Re  | `R` | R          |
| Flat Ga  | `G` | G          |
| Sharp Ma | `M` | M          |
| Flat Dha | `D` | D          |
| Flat Ni  | `N` | N          |

### Octaves

A dot symbol `·` above or below a note signifies upper (Tar) or lower (Mandra) octave respectively. The two dots symbol `··` above or below a note signifies two octaves upper (Ati Tar) or lower (Ati Mandra) respectively. The absence of the dot signifies middle octave.

{:.keymap.bhatkhande-bangla}
| Note                  | Key  | Bhatkhande |
|-----------------------|------|------------|
| Lower Sharp Ma        | `Ml` | Ml         |
| Middle Pa             | `p`  | p          |
| Upper Flat Dha        | `Du` | Du         |
| Double Upper Flat Gha | `GU` | GU         |

## Mizrab Ke Bol (Strokes)

All Strokes take the same space as Notes, except for Dir which takes the space for two Notes.

{:.keymap.bhatkhande-bangla}
| Stroke | Key | Bhatkhande  |
|--------|-----|-------------|
| Da     | `;` | ;           |
| Ra     | `'` | {{ "'" }}   |
| Daa    | `[` | [           |
| Raa    | `]` | ]           |
| Dir    | `\` | \           |
| Khali  | `-` | -           |

### Special Instructions for Word Processors

A number of word processors, including Microsoft Word, Apple Pages, and LibreOffice, will sometimes automatically replace a straight quotation mark `'` ([`U+0027` Apostrophe](http://graphemica.com/%27)) with a typographic quote `’` ([`U+2019` Right Single Quotation Mark](http://graphemica.com/%E2%80%99)). This facility is called "Smart Quotes".

In previous versions, the Bhatkhande <span class="ome-bhatkhande-bangla">&apos;</span> corresponded to the former, not the latter, and having Smart Quotes enabled made that character disappear. This was fixed in [version 2.1.0](https://github.com/omenad/fonts/releases/tag/2.1.0). Please upgrade to the latest version to remedy this issue.

## Chhand

Chhand characters take zero space, and must be typed immediately before a set of notes they will cover. They are used to show multiple notes played within the same beat.

To make a chhand of 2-8 notes, use the keys `Shift``+``2`&ndash;`8`:

{:.keymap.bhatkhande-bangla}
| Chhand Size  | Key | Bhatkhande |
|--------------|-----|------------|
| Dugun (2)    | `@` | @          |
| Tigun (3)    | `#` | #          |
| Chaugun (4)  | `$` | $          |
| Pachgun (5)  | `%` | %          |
| Chhatgun (6) | `^` | ^          |
| Satgun (7)   | `&` | &          |
| Athgun (8)   | `*` | *          |

Additionally, <code>`</code>, `!`, and `~` can be used for a lower version of Chaugun (4), Chhatgun (6), and Athgun (8) to allow for larger groupings.

{:.keymap.bhatkhande-bangla}
| Chhand Size        | Key            | Bhatkhande |
|--------------------|----------------|------------|
| Lower Chaugun (4)  | <code>`</code> | `          |
| Lower Chhatgun (6) | `!`            | !          |
| Lower Athgun (8)   | `~`            | ~          |

This is an example of a chhand showing complicated layakari:

{:.keymap.bhatkhande-bangla}
| Key Strokes                          | Bhatkhande                       |
|--------------------------------------|----------------------------------|
| ``~#srg%mpdnsu !@sr$gmpd `qswrWgem`` | ~#srg%mpdnsu !@sr$gmpd `qswrWgem |

## Meend

The Meend characters take zero space, and must be typed immediately before a note from any octave. The Meend characters, are to be used as a set.

A valid Meend sequence is that which begins with the Meend Start character `q`, is followed by one note from any octave, followed by zero or more pairs of a Meend Continue character `w` and one note from any octave, and finished with a Meend End character `e` followed by one note from any octave. The Meend Stroke character, made with a `W`, is used to indicate a note on which a stroke is necesary to keep the meend going.

{:.keymap.bhatkhande-bangla}
| Meend Character | Key | Bhatkhande |
|-----------------|-----|------------|
| Meend Start     | `q` | q          |
| Ghaseet Start   | `Q` | Q          |
| Meend Continue  | `w` | w          |
| Meend Stroke    | `W` | W          |
| Meend End       | `e` | e          |
| Ghaseet End     | `E` | E          |

The following examples illustrate how a valid Meend sequence is visually cohesive in its representation of a continuous pull:

{:.keymap.bhatkhande-bangla}
| Key Strokes  | Bhatkhande |
|--------------|------------|
| `qswrwgem`   | qswrwgem   |
| `qger`       | qger       |
| `qRwGwmep`   | qRwGwmep   |
| `qDlwNlWser` | qDlwNlWser |

## Murki

Parentheses around a note indicate a quick movement from the note to the adjescent ones and back to the original note. For example, <span class="ome-bhatkhande-bangla">(p)</span> can translate to <span class="ome-bhatkhande-bangla">Mpdp</span>, or <span class="ome-bhatkhande-bangla">dpMp</span>, or <span class="ome-bhatkhande-bangla">pMdp</span>, depending on the artist's interpretation.

{:.keymap.bhatkhande-bangla}
| Key Strokes | Bhatkhande |
|-------------|------------|
| `(p)`       | (p)        |

## Kan

Kan and Krintan rely on the word processing ability to **superscript**. Since the width of these superscripted characters depends on the word processor, in certain cases it can break the monospacing of the font.

{:.keymap.bhatkhande-bangla}
| Key Strokes              | Bhatkhande          |
|--------------------------|---------------------|
| `<sup>``m``</sup>``p`    | <sup>m</sup>p       |
| `d``<sup>``g``</sup>``m` | d<sup>g</sup>m      |

The ability to add predictable superscripting is planned for the future.

## Krintan

Krintan is Kan repeated twice, thrice, four times in a single stroke of the Mizrab, represented by the numeral after the Kan note.

{:.keymap.bhatkhande-bangla}
| Key Strokes              | Bhatkhande          |
|--------------------------|---------------------|
| `<sup>``m3``</sup>``p`   | <sup>m3</sup>p      |

## Miscellaneous

{:.keymap.bhatkhande-bangla}
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

<div class="horizontal-scroll-block" markdown="block">

{:.composition.bhatkhande-bangla}
|||`g  @pp g  p `|`-  @nn d  n `|
|||`[  \ [  ] `|`-  \ [  ] `|
|`su  -  d  n `|`su  ru  su  - `|`su  @gugu @gugu @mumu`|`ru  @rusu @-su d `|
|`[  -  [  ] `|`[  ]  [  - `|`[  \ \ \`|`[  @'[ @-' [`|
|`p  @mm @gg @mm`|`r  @rs @-s s `|||
|`[  \ \ \`|`[  @'[ @-' [ `|||
|`x`|`2`|`0`|`3`|

</div>

_Raga Bilawal: Composition 101, Antara from राग विबोध : मिश्रबानी by Dr. Ragini Trivedi_

The Bhatkhande notation system requires more ceremony and organization to write.
It is written in a tabular format, with columns subdividing the beat into smaller parts.
Each line of the composition is written in two rows: the top row being the notes (movement of the left hand on sitar), and the bottom one being strokes (movement of the right hand on sitar).
The final row represents the starting beat for each subdivision. The rest are captured from the alignment.

## Zero Character Sequencing

The zero character sets of Chhand and Meend, they can be typed in any order and have the same visual effect. For example, pay attention to the first three characters in the following:

{:.keymap.bhatkhande-bangla}
| Key Strokes              | Bhatkhande  |
|--------------------------|-------------|
| <code>`@qswr@Wgem</code> | `@qswr@Wgem |
| <code>`q@swr@Wgem</code> | `q@swr@Wgem |
| <code>@`qswr@Wgem</code> | @`qswr@Wgem |
| <code>@q`swr@Wgem</code> | @q`swr@Wgem |
| <code>q`@swr@Wgem</code> | q`@swr@Wgem |
| <code>q@`swr@Wgem</code> | q@`swr@Wgem |

Of these, the first one should be considered canonical. The characters should be ordered in ascending terms of locality, with the least local Lower Chaugun (affecting 4 notes) first, then Dugun (affecting two notes), and then the Meend Start (affecting only one). The character affecting only one note should be closest to it.

# Web Use

For usage on the web, add the following block to the `<head>` section:

```html
<link rel="stylesheet" href="https://webfonts.omenad.net/fonts.css">
```

You can then use the `.ome-bhatkhande-bangla` class on any element to use the font:

```html
<code class="ome-bhatkhande-bangla">g  @pp g  p</code>
```

It is recommended to use `<pre>` or `<code>` to preserve whitespace in the compositions.

For writing a full composition as shown above, a table is required, for example:

```html
<table class="composition bhatkhande-bangla">
  <tbody>
    <tr>
      <td></td>
      <td></td>
      <td><code>g  @pp g  p </code></td>
      <td><code>-  @nn d  n </code></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td><code>[  \ [  ] </code></td>
      <td><code>-  \ [  ] </code></td>
    </tr>
    <tr>
      <td><code>su  -  d  n </code></td>
      <td><code>su  ru  su  - </code></td>
      <td><code>su  @gugu @gugu @mumu</code></td>
      <td><code>ru  @rusu @-su d </code></td>
    </tr>
    <tr>
      <td><code>[  -  [  ] </code></td>
      <td><code>[  ]  [  - </code></td>
      <td><code>[  \ \ \</code></td>
      <td><code>[  @'[ @-' [</code></td>
    </tr>
    <tr>
      <td><code>p  @mm @gg @mm</code></td>
      <td><code>r  @rs @-s s </code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>[  \ \ \</code></td>
      <td><code>[  @'[ @-' [ </code></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td><code>x</code></td>
      <td><code>2</code></td>
      <td><code>0</code></td>
      <td><code>3</code></td>
    </tr>
  </tbody>
</table>
```

with additional styling provided by:

```css
table.composition {
  border: none;
}

table.composition td {
  width: 25%;
  border: none;
  border-right: 1px solid black;
}

table.composition td:last-child {
  border-right: none;
}

table.composition.bhatkhande-bangla td > code {
  white-space: pre;
  font-family: 'ome_bhatkhande_hindi';
}
```

Webfonts are currently not included in the download package, and they are not licensed for self-hosted web use. Usage from the above URL is free and unlimited at this time.
