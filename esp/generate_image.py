from argparse import ArgumentParser


def build_argument_parser():
    parser = ArgumentParser()
    parser.add_argument('-c', '--config', help='configuration file name', default='rhapsody.toml')
    parser.add_argument('-o', '--output', help='output file name', default='esp/esp.img')
    return parser


def main():
    parser = build_argument_parser()
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
