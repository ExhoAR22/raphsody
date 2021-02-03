from argparse import ArgumentParser

from image_generator import generate


def build_argument_parser():
    """
    Builds the ArgumentParser object to use when parsing the arguments
    """
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', help='configuration file name', default='rhapsody.toml')
    parser.add_argument('-s', '--size', help='size of the generated image, in MiBs', type=int, default=1)
    parser.add_argument('-o', '--output', help='output file name', default='esp.img')
    return parser


def main():
    parser = build_argument_parser()
    args = parser.parse_args()
    generate(args.config, args.size, args.output)


if __name__ == '__main__':
    main()
