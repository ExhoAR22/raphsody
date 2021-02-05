from .config import build_config
from .fat import format_image, make_directory, add_file


def generate(config_file, arch, size, output):
    """
    Generates an ESP image
    :param config_file: the name of the configuration file to use
    :param arch: the architecture of the binaries included in the image
    :param size: the size of the image, in MiBs
    :param output: the name of the generated image file
    """
    if arch.lower() not in ['x86_64', 'aarch64']:
        raise ValueError(arch)
    elif size < 1:
        raise ValueError(size)

    config = build_config(config_file)
    with open(output, 'wb') as output_file:
        image = bytearray(1024 * 1024 * size)
        format_image(image)
        make_directory(image, '/EFI')
        make_directory(image, '/EFI/BOOT')
        add_file(image, '/Rhapsody.bin', config)
