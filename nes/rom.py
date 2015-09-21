'''
    TODO
'''

# Import standard library modules
from __future__ import print_function

import os

# Import nesi modules
import nes.settings


def nesi_information():
    '''
        Returns a string that describes the current nesi version and author
    '''

    build = nes.settings.build()

    return 'nesi {major}.{minor} by {author} ({author_email})'.format(
        major=build['major_version'],
        minor=build['minor_version'],
        author=build['author'],
        author_email=build['author_email'],
    )


class NesRom(object):
    '''
        TODO
    '''

    def __init__(self, rom_path):
        self.rom_name = os.path.basename(rom_path)

        with open(rom_path, 'rb') as fopen:
            self.rom_data = bytearray(fopen.read())

        self.rom_size = len(self.rom_data)

    def analyze(self):
        '''
            Parses the rom image and stores all information
        '''

        # Analyze stuff

        return self

    def print_file_info(self):
        '''
            Prints the rom's name and file size
        '''

        print('{rom_name} ({rom_size} bytes, {kbytes} kilobytes)'.format(
            rom_name=self.rom_name,
            rom_size=self.rom_size,
            kbytes=self.rom_size / 1024
        ))

    def print_analysis(self):
        '''
            Prints all image information
        '''

        print(nesi_information())
        print()

        self.print_file_info()
