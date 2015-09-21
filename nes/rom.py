'''
    TODO
'''

# Import standard library modules
from __future__ import print_function

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

    def __init__(self, rom):
        self.rom = rom

    def analyze(self):
        '''
            TODO
        '''

        # Analyze stuff

        return self

    def print_analysis(self):
        '''
            TODO
        '''

        print(nesi_information())
        print()

        print('Was given {rom}'.format(rom=self.rom))
