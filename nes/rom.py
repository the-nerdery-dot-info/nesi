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

        # Analysis Fields
        self.valid = False
        self.header = []
        self.prg_count = 0
        self.chr_count = 0
        self.mapper = None
        self.trainer = False
        self.fourscreen = False

    def analyze(self):
        '''
            Parses the rom image and stores all information
        '''

        self.valid = self.rom_data[0:4] == 'NES\x1a'
        self.header = ' '.join([hex(n) for n in self.rom_data[0:15]])
        self.prg_count = self.rom_data[4]
        self.chr_count = self.rom_data[5]
        self.mapper = (self.rom_data[6] >> 4) | ((self.rom_data[7] >> 4) << 4)
        self.trainer = (self.rom_data[6] & 0x4) == 1
        self.fourscreen = (self.rom_data[6] & 0x8) == 1

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

    def print_header_info(self):
        '''
            Prints the rom's header information
        '''

        print('NES\\0x1a present? {valid}'.format(valid=self.valid))
        print('Header: {header}'.format(header=self.header))
        print('PRG Count: {prg_count}'.format(prg_count=self.prg_count))
        print('CHR Count: {chr_count}'.format(chr_count=self.chr_count))
        print('Mapper: {mapper}'.format(mapper=self.mapper))
        print('Trainer: {trainer}'.format(trainer=self.trainer))
        print('4 Screen: {fourscreen}'.format(fourscreen=self.fourscreen))

    def print_analysis(self):
        '''
            Prints all image information
        '''

        print(nesi_information())
        print()

        self.print_file_info()
        print()

        self.print_header_info()
