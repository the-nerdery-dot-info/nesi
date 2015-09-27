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
    16: {
        'name': 'Bandai EPROM (24C02)',
        'examples': 'Unknown',
    },
    18: {
        'name': 'Jaleco SS8806',
        'examples': 'Unknown',
    },
    19: {
        'name': 'Namco 163',
        'examples': 'Unknown',
    },
    21: {
        'name': 'VRC4a, VRC4c',
        'examples': 'Unknown',
    },
    22: {
        'name': 'VRC2a',
        'examples': 'Unknown',
    },
    23: {
        'name': 'VRC2b, VRC4e',
        'examples': 'Unknown',
    },
    24: {
        'name': 'VRC6a',
        'examples': 'Unknown',
    },
    25: {
        'name': 'VRC4b, VRC4d',
        'examples': 'Unknown',
    },
    26: {
        'name': 'VRC6b',
        'examples': 'Unknown',
    },
    34: {
        'name': 'BNROM, NINA-001',
        'examples': 'Unknown',
    },
    64: {
        'name': 'RAMBO-1',
        'examples': 'Unknown',
    },
    66: {
        'name': 'GxROM, MxROM',
        'examples': 'Unknown',
    },
    68: {
        'name': 'After Burner',
        'examples': 'Unknown',
    },
    69: {
        'name': 'FME-7, Sunsoft 5B',
        'examples': 'Unknown',
    },
    71: {
        'name': 'Camerica/Codemasters',
        'examples': 'Unknown',
    },
    73: {
        'name': 'VRC3',
        'examples': 'Unknown',
    },
    74: {
        'name': 'Pirate MMC3 derivative',
        'examples': 'Unknown',
    },
    75: {
        'name': 'VRC1',
        'examples': 'Unknown',
    },
    76: {
        'name': 'Namco 109 variant',
        'examples': 'Unknown',
    },
    79: {
        'name': 'NINA-03/NINA-06',
        'examples': 'Unknown',
    },
    85: {
        'name': 'VRC7',
        'examples': 'Unknown',
    },
    86: {
        'name': 'JALECO-JF-13',
        'examples': 'Unknown',
    },
    94: {
        'name': 'Senjou no Ookami',
        'examples': 'Unknown',
    },
    105: {
        'name': 'NES-EVENT',
        'examples': 'Unknown',
    },
    113: {
        'name': 'NINA-03/NINA-06??',
        'examples': 'Unknown',
    },
    118: {
        'name': 'TxSROM, MMC3 Variant',
        'examples': 'Unknown',
    },
    119: {
        'name': 'TQROM, MMC3 Variant',
        'examples': 'Unknown',
    },
    159: {
        'name': 'Bandai EPROM (24C01)',
        'examples': 'Unknown',
    },
    166: {
        'name': 'SUBOR',
        'examples': 'Unknown',
    },
    167: {
        'name': 'SUBOR',
        'examples': 'Unknown',
    },
    180: {
        'name': 'Crazy Climber',
        'examples': 'Unknown',
    },
    185: {
        'name': 'CNROM with protection diodes',
        'examples': 'Unknown',
    },
    192: {
        'name': 'Pirate MMC3 derivative',
        'examples': 'Unknown',
    },
    206: {
        'name': 'DxROM, Namco 118 / MIMIC-1',
        'examples': 'Unknown',
    },
    210: {
        'name': 'Namco 175 and 340',
        'examples': 'Unknown',
    },
    228: {
        'name': 'Action 52',
        'examples': 'Unknown',
    },
    232: {
        'name': 'Camerica/Codemasters Quattro',
        'examples': 'Unknown',
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
