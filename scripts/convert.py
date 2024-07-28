#!/usr/bin/python3

import argparse
import fontforge
from pathlib import Path


def convert(input_sfd, format, output_dir):
    sfd = fontforge.open(input_sfd)
    output_file = f"{output_dir}/{Path(input_sfd).stem}.{format}"

    sfd.generate(output_file)


def main():
    parser = argparse.ArgumentParser(
        description="Convert SFD to TTF/UFO to given output directory"
    )
    parser.add_argument(
        "--format", required=True, help="Output format. Must be ttf or ufo."
    )
    parser.add_argument("--output", required=True, help="Output directory.")
    parser.add_argument("input_sfd", help="Input SFD file.")

    args = parser.parse_args()

    if args.format not in ["ttf", "ufo"]:
        raise f"Invalid format: {args.format}"

    if not Path(args.output).is_dir:
        raise f"Invalid output directory: {args.output}"

    if not Path(args.input_sfd).is_file or not args.input_sfd.endswith(".sfd"):
        raise f"Invalid input SFD file: {args.input_sfd}"

    convert(args.input_sfd, args.format, args.output)


if __name__ == "__main__":
    main()
