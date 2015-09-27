'''
    The mappers package contains all known information about each NES mapper.
    The data here was dug up through various websites. For the sake of history,
    the following sites/docs proved useful:

        1. http://wiki.nesdev.com
        2. http://tuxnes.sourceforge.net/nesmapper.txt
'''

NES_MAPPERS = {
    0: {
        'name': 'NROM',
        'examples': 'Bomberman (J), Battle City, Duck Hunt, Dig Dug',
    },
    1: {
        'name': 'MMC1',
        'examples': 'Blaster Master, Bubble Bobble, Adventures of Bayou Billy',
    },
    2: {
        'name': 'UxROM',
        'examples': 'Mega Man, Castlevania, Contra, Duck Tales, Metal Gear',
    },
    3: {
        'name': 'CNROM',
        'examples': 'Arkanoid, Bump \'n\' Jump, Cybernoid, Solomon\'s Key',
    },
    4: {
        'name': 'MMC3 (TxROM)',
        'examples': 'Fester\'s Quest, Final Fantasy 3, Mega Man 3',
    },
    5: {
        'name': 'MMC5 (ExROM)',
        'examples': 'Castlevania 3, Uncharted Waters, Laser Invasion',
    },
    6: {
        'name': 'FFE (F4xxx)',
        'examples': 'Saint Seiya (Hacked), Dragon Scroll (Hacked)',
    },
    7: {
        'name': 'AxROM',
        'examples': 'Battletoads, Jeopardy',
    },
    8: {
        'name': 'FFE (F4xxx)',
        'examples': 'Saint Seiya (Hacked), Dragon Scroll (Hacked)',
    },
    9: {
        'name': 'MMC2 (PxROM)',
        'examples': 'Punch Out!',
    },
    10: {
        'name': 'MMC4 (FxROM)',
        'examples': 'Famicom Wars',
    },
    11: {
        'name': 'Color Dreams',
        'examples': 'Bible Adventures, Chiller, Crystal Mines, Metal Fighter',
    },
    12: {
        'name': 'MMC3 Variant',
        'examples': 'Dragon Ball Z 5',
    },
    13: {
        'name': 'NES-CPROM',
        'examples': 'Videomation',
    },
    14: {
        'name': 'MMC3 Variant',
        'examples': 'Samurai Spirits (Pirated)',
    },
    15: {
        'name': 'Unknown Name',
        'examples': '100-in-1 Contra Function 16 (Pirated)',
    },
}


def find(mapper_id):
    '''
        Takes a mapper ID as an integer and returns an object representing
        what we know about the mapper. The object looks like:

        {
            'name': 'Foobar,
            'examples': 'Foo, Bar, Baz'
        }

        If we don't have any information on the mapper, a special object is
        returned,

        {
            'name': 'Unknown',
            'examples': 'None'
        }
    '''

    try:
        return NES_MAPPERS[mapper_id]
    except KeyError:
        return {
            'name': 'Unknown',
            'examples': 'None'
        }
