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
        self.mapper = None
        self.trainer = False
        self.fourscreen = False
        self.battery = False

    def analyze(self):
        '''
            Parses the rom image and stores all information
        '''

        self.mapper = (self.rom_data[6] >> 4) | ((self.rom_data[7] >> 4) << 4)
        self.trainer = ((self.rom_data[6] >> 2) & 0x1) == 1
        self.fourscreen = ((self.rom_data[6] >> 3) & 0x1) == 1
        self.battery = ((self.rom_data[6] >> 1) & 0x1) == 1

        return self

    def mirroring(self):
        '''
            TODO
        '''
        if (self.rom_data[6] & 0x1) == 1:
            return 'vertical'
        else:
            return 'horizontal'

    def header(self):
        '''
            TODO
        '''
        return ' '.join([hex(n) for n in self.rom_data[0:15]])

    def contains_magic_number(self):
        '''
            TODO
        '''
        return self.rom_data[0:4] == 'NES\x1a'

    def prg_count(self):
        '''
            TODO
        '''
        return self.rom_data[4]

    def chr_count(self):
        '''
            TODO
        '''
        return self.rom_data[5]

    def print_analysis(self):
        '''
            Prints all image information
        '''

        print(nesi_information())
        print()

        print('{rom_name} ({rom_size} bytes, {kbytes} kilobytes)'.format(
            rom_name=self.rom_name,
            rom_size=self.rom_size,
            kbytes=self.rom_size / 1024
        ))
        print()

        if self.contains_magic_number():
            print('NES\\0x1a present')
        else:
            print('NES\\0x1a not present!')

        print('Header: {header}'.format(header=self.header()))
        print('PRG Count: {prg_count}'.format(prg_count=self.prg_count()))
        print('CHR Count: {chr_count}'.format(chr_count=self.chr_count()))
        print('Mapper: {mapper}'.format(mapper=self.mapper))
        print('Trainer: {trainer}'.format(trainer=self.trainer))
        print('4 Screen: {fourscreen}'.format(fourscreen=self.fourscreen))
        print('Battery: {battery}'.format(battery=self.battery))
        print('Mirroring: {mirroring}'.format(mirroring=self.mirroring()))
