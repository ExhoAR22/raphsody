import toml
from ctypes import Structure, c_uint32, c_char
from struct import pack


class ConfigEntry(Structure):
    _pack_ = 1

    _fields_ = [
        ('display_name', c_char * 16),
        ('kernel', c_char * 16),
        ('boot_protocol_version', c_uint32),
        ('kernel_arguments_length', c_uint32),
        ('kernel_arguments', c_char * 0)
    ]


def build_config(config_file):
    config = toml.load(config_file)
    result = b'RCF\0'

    for name, params in config.items():
        if type(params) is dict:
            entry = ConfigEntry()
            entry.display_name = name.encode('ascii')
            entry.kernel = params['kernel'].encode('ascii')
            entry.boot_protocol_version = params['boot_protocol_version']
            entry.kernel_arguments_length = len(params['kernel_arguments'])
            serialized = bytearray(entry)
            result += pack('I', len(serialized))
            result += serialized
            result += params['kernel_arguments'].encode('ascii')

    return result
