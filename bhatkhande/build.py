#!/usr/bin/python

import argparse
import shutil
import fontforge
import os.path

from meta import META


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
    m = META[output_name]
    lang = 'English (US)'
    output_font.copyright = m['Copyright']
    output_font.appendSFNTName(lang, 'Copyright', m['Copyright'])
    output_font.familyname = m['Family']
    output_font.appendSFNTName(lang, 'Family', m['Family'])
    output_font.fullname = m['Family']
    output_font.appendSFNTName(lang, 'Fullname', m['Family'])
    output_font.fontname = m['PostScriptName']
    output_font.appendSFNTName(lang, 'PostScriptName', m['PostScriptName'])
    output_font.version = 'Version {} {}'.format(
        m['Version'],
        m['Date']
    )
    output_font.appendSFNTName(lang, 'Version', 'Version {} {}'.format(
        m['Version'],
        m['Date']
    ))
    output_font.appendSFNTName(lang, 'Designer', m['Designer'])
    output_font.appendSFNTName(lang, 'Designer URL', m['Designer URL'])
    output_font.appendSFNTName(lang, 'Descriptor', m['Descriptor'])
    output_font.appendSFNTName(lang, 'License', m['License'])
    output_font.appendSFNTName(lang, 'Sample Text', m['Sample Text'])
    output_font.appendSFNTName(lang, 'UniqueID', '{}:{}'.format(
        m['PostScriptName'][:16],
        m['Version']
    ))

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
    lang_sfd = '{}/{}.sfd'.format(lang, lang_C)
    if not os.path.exists(lang_sfd):
        raise 'Could not find language file: {}'.format(lang_sfd)

    # Define the glyph list for replacement
    glyph_list = [
        # Numerals
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        # Regular Notes
        's', 'r', 'g', 'm', 'p', 'd', 'n',
        # Variant Notes
             'R', 'G', 'M',      'D', 'N',
        # Strokes
        '[', ']', ';', "'", '\\',
        # Extras
        'quoteright',  # Handles smartquote fallback
    ]

    # Paths to base SFD file
    base_sfd = 'base/OmeBhatkhandeBase.sfd'
    output_sfd = '{}/OmeBhatkhande{}.sfd'.format(lang, lang_C)

    # Use the base font and the language font to generate an output font
    replace_glyphs(base_sfd, lang_sfd, output_sfd, lang_C, glyph_list)


if __name__ == '__main__':
    main()
