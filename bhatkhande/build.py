#!/usr/bin/python3

import argparse
import shutil
import fontforge

from pathlib import Path


def replace_glyphs(
        base_font_path,
        replacement_font_path,
        output_font_path,
        output_name,
        glyph_list):
    # Copy base font to output
    shutil.copy(base_font_path, output_font_path)
    
    # Open the output font and the font with replacement glyphs
    output_font = fontforge.open(output_font_path)
    replacement_font = fontforge.open(replacement_font_path)

    # Iterate over the glyph list
    for glyph_name in glyph_list:
        # Select the glyph in the replacement font
        replacement_font.selection.select(glyph_name)
        replacement_font.copy()  # Copy the glyph

        # Select the glyph in the output font
        output_font.selection.select(glyph_name)
        output_font.paste()  # Paste the glyph

    # Generate the output font
    output_font.fontname = output_font.fontname.replace('Base', output_name)
    output_font.familyname = output_font.familyname.replace('Base', output_name)
    output_font.fullname = output_font.fullname.replace('Base', output_name)
    output_font.save(output_font_path)
    print(output_font_path)


def main():
    parser = argparse.ArgumentParser(
        description='Build Bhatkhande font for a given language'
    )
    parser.add_argument('language', help='Name of the language to build')

    # Parse the command-line arguments
    args = parser.parse_args()
    lang = args.language.lower()
    lang_C = lang.capitalize()

    # Check if language files exist where expected
    lang_sfd = f'{lang}/{lang_C}.sfd'
    if not Path(lang_sfd).is_file():
        raise f'Could not find language file: {lang_sfd}'
    
    # Define the glyph list for replacement
    glyph_list = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        's', 'r', 'g', 'm', 'p', 'd', 'n',
             'R', 'G', 'M',      'D', 'N',
        '[', ']', ';', "'", '\\',
    ]

    # Paths to base SFD file
    base_sfd = 'base/OmeBhatkhandeBase.sfd'
    output_sfd = f'{lang}/OmeBhatkhande{lang_C}.sfd'

    # Use the base font and the language font to generate an output font
    replace_glyphs(base_sfd, lang_sfd, output_sfd, lang_C, glyph_list)


if __name__ == '__main__':
    main()
