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


def fmt_str(tag, string):
    '''
        TODO
    '''
    return tag.ljust(15) + '| ' + string


class NesRom(object):
    '''
        TODO
    '''

    def __init__(self, rom_path):
        self.rom_name = os.path.basename(rom_path)

        with open(rom_path, 'rb') as fopen:
            self.rom_data = bytearray(fopen.read())

        self.rom_size = len(self.rom_data)

    def battery(self):
        '''
            TODO
        '''
        return ((self.rom_data[6] >> 1) & 0x1) == 1

    def fourscreen(self):
        '''
            TODO
        '''
        return ((self.rom_data[6] >> 3) & 0x1) == 1

    def trainer(self):
        '''
            TODO
        '''
        return ((self.rom_data[6] >> 2) & 0x1) == 1

    def mapper(self):
        '''
            TODO
        '''
        return (self.rom_data[6] >> 4) | ((self.rom_data[7] >> 4) << 4)

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

        def fmt_hex_str(string):
            '''
                TODO
            '''
            return hex(string).replace('0x', '').upper()

        return ' '.join([fmt_hex_str(n) for n in self.rom_data[0:15]])

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

        rom = fmt_str(
            'ROM',
            '{rom_name} ({rom_size} bytes, {kbytes} kilobytes)'.format(
                rom_name=self.rom_name,
                rom_size=self.rom_size,
                kbytes=self.rom_size / 1024
            )
        )

        print(rom)

        validity = fmt_str('Valid?', 'NO')

        if self.contains_magic_number():
            validity = fmt_str('Valid?', 'YES')
        else:
            # Bail out, don't parse the file if it's not valid
            return

        print(validity)

        print(fmt_str('Header', self.header()))
        print(fmt_str('PRG', str(self.prg_count())))
        print(fmt_str('CHR', str(self.chr_count())))
        print(fmt_str('Mapper', str(self.mapper())))
        print(fmt_str('FourScreen?', str(self.fourscreen())))
        print(fmt_str('Battery?', str(self.battery())))
        print(fmt_str('Mirroring?', str(self.mirroring())))
        print(fmt_str('Trainer?', str(self.trainer())))
