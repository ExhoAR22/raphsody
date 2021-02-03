from .config import build_config


def generate(config_file, size, output):
    """
    Generates an ESP image
    :param config_file: the name of the configuration file to use
    :param size: the size of the image, in MiBs
    :param output: the name of the generated image file
    """
    config = build_config(config_file)
    with open(output, 'wb') as output_file:
        pass
