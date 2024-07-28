#!/usr/bin/python

import argparse
import fontforge
import os.path


def convert(input_sfd, format, output_dir):
    sfd = fontforge.open(input_sfd)
    output_file = "{}/{}.{}".format(
        output_dir,
        os.path.splitext(os.path.basename(input_sfd))[0],
        format)

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
        raise "Invalid format: {}".format(args.format)

    if not os.path.exists(args.output):
        raise "Invalid output directory: {}".format(args.output)

    if not os.path.exists(args.input_sfd) or not args.input_sfd.endswith(".sfd"):
        raise "Invalid input SFD file: {}".format(args.input_sfd)

    convert(args.input_sfd, args.format, args.output)


if __name__ == "__main__":
    main()
