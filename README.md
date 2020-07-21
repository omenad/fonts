# Omenad Fonts

[![Downloads for All Releases](https://img.shields.io/github/downloads/omenad/fonts/total.svg)](https://www.somsubhra.com/github-release-stats/?username=omenad&repository=fonts)
[![Latest Release](https://img.shields.io/github/release/omenad/fonts.svg)](https://github.com/omenad/fonts/releases/latest)

Font for writing Indian Classical Music.
[Read the full documentation.][docs]
[Download the fonts.][download]

## Fonts

### [Ome Swarlipi][swarlipi]

[![swarlipi-image][swarlipi-image]][swarlipi]

A notation system designed to be non-language specific, easy to learn, and very compact.

### Bhatkhande Notation

[![bhatkhande-hindi-image][bhatkhande-hindi-image]][bhatkhande-hindi]

The classical system for writing Indian Classical Music. These are available for [Hindi][bhatkhande-hindi], [English][bhatkhande-english], and [Punjabi][bhatkhande-punjabi].

## Development

The sources are [FontForge][fontforge] SFD files. Use it to make changes to them.

Requires Docker.

Use `scripts/build` to build the sources into `.ttf` files.
Use `scripts/server` to run the docs. They will be accessible at http://0.0.0.0:4000/fonts/, and will watch for changes.

## Releasing

Uses git-flow.
Ensure `CHANGELOG.md` is updated.
Use `scripts/publish $TAG` to make a zip file.
Make a release on GitHub. Add that zip file to it.
Add a new URL to rajada.in for the release.
Make a `docs/$TAG` branch and update all references for downloading it. Merge to `master`.

[docs]: https://omenad.github.io/fonts/
[download]: http://rajada.in/omenadfonts221
[swarlipi]: https://omenad.github.io/fonts/ome-swarlipi/
[swarlipi-image]: https://omenad.github.io/fonts/assets/images/ome-swarlipi-thumbnail.jpg
[bhatkhande-hindi]: https://omenad.github.io/fonts/ome-bhatkhande-hindi/
[bhatkhande-hindi-image]: https://omenad.github.io/fonts/assets/images/ome-bhatkhande-hindi-thumbnail.jpg
[bhatkhande-english]: https://omenad.github.io/fonts/ome-bhatkhande-english/
[bhatkhande-punjabi]: https://omenad.github.io/fonts/ome-bhatkhande-punjabi/
[fontforge]: https://fontforge.org/en-US/
