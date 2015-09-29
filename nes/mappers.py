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
        'examples': 'SD Gundam Knight Story, Akuma Kun, Dragon Ball 2',
    },
    17: {
        'name': 'FFE (similar to mapper 6)',
        'examples': 'Dragon Ball Z 2 (Hacked), Parodius (Hacked)',
    },
    18: {
        'name': 'Jaleco SS8806',
        'examples': 'Magic John, Plasma Ball, The Lord of King',
    },
    19: {
        'name': 'Namco 163',
        'examples': 'Megami Tensei II, Rolling Thunder (J)',
    },
    20: {
        'name': 'FDS',
        'examples': 'None',
    },
    21: {
        'name': 'VRC4a, VRC4c',
        'examples': 'Gradius 2, Ganbare Goemon Gaiden 2',
    },
    22: {
        'name': 'VRC2a',
        'examples': 'TwinBee 3, Ganbare Goemon Gaiden, Wai Wai World',
    },
    23: {
        'name': 'VRC2b, VRC4e',
        'examples': 'Contra (J), Boku Dracula Kun',
    },
    24: {
        'name': 'VRC6a',
        'examples': 'Akumajo Dracula 3',
    },
    25: {
        'name': 'VRC4b, VRC4d',
        'examples': 'Ganbare Goemon Gaiden',
    },
    26: {
        'name': 'VRC6b',
        'examples': 'Mouryou Senki Madara',
    },
    27: {
        'name': 'Pirate Variant of VRC4',
        'examples': 'Unknown',
    },
    28: {
        'name': 'Action 53 Extension Mod',
        'examples': 'STREEMERZ: Action 53 Function 16 Volume One',
    },
    34: {
        'name': 'BNROM, NINA-001',
        'examples': 'Impossible Mission 2, Deadly Towers, 3D Worldrunner',
    },
    64: {
        'name': 'RAMBO-1',
        'examples': 'Klax, Shinobi, Skull and Crossbones',
    },
    66: {
        'name': 'GxROM, MxROM',
        'examples': 'Doraemon, Dragon Power, Super Mario Bros. + Duck Hunt ',
    },
    68: {
        'name': 'After Burner',
        'examples': 'After Burner, Maharaja (J)',
    },
    69: {
        'name': 'FME-7, Sunsoft 5B',
        'examples': 'Batman (J), Batman - Return of the Joker',
    },
    71: {
        'name': 'Camerica/Codemasters',
        'examples': 'Bee 52, MiG 29 - Soviet Fighter, Fire Hawk',
    },
    73: {
        'name': 'VRC3',
        'examples': 'Salamander',
    },
    74: {
        'name': 'Pirate MMC3 derivative',
        'examples': 'Unknown, Eastern Games?',
    },
    75: {
        'name': 'VRC1',
        'examples': 'Exciting Boxing, King Kong 2: Ikari no Megaton Punch',
    },
    76: {
        'name': 'Namco 109 variant',
        'examples': 'Digital Devil Story - Megami Tensei',
    },
    79: {
        'name': 'NINA-03/NINA-06',
        'examples': 'Double Strike, Dudes with Attitudes',
    },
    85: {
        'name': 'VRC7',
        'examples': 'Lagrange Point, Tiny Toon Adventures',
    },
    86: {
        'name': 'JALECO-JF-13',
        'examples': 'Moero!! Pro Yakyuu',
    },
    94: {
        'name': 'HVC-UN1ROM, similar to the UxROM',
        'examples': 'Senjou no Ookami',
    },
    105: {
        'name': 'NES-EVENT',
        'examples': 'Nintendo World Championships 1990',
    },
    113: {
        'name': 'NINA-03/NINA-06??',
        'examples': 'Mind Blower Pak, HES 6-in-1, Total Funpak',
    },
    118: {
        'name': 'TxSROM, MMC3 Variant',
        'examples': 'Armadillo, Pro Sport Hockey',
    },
    119: {
        'name': 'TQROM, MMC3 Variant',
        'examples': 'High Speed, Pinbot',
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
        'name': 'UNROM Variant',
        'examples': 'Crazy Climber',
    },
    185: {
        'name': 'CNROM with protection diodes',
        'examples': 'Mighty Bomb Jack (J), Spy Vs. Spy (J)',
    },
    192: {
        'name': 'Pirate MMC3 derivative',
        'examples': 'Ying Lie Qun Xia Zhuan',
    },
    206: {
        'name': 'DxROM, Namco 118 / MIMIC-1',
        'examples': 'Babel no Tou',
    },
    210: {
        'name': 'Namco 175 and 340',
        'examples': 'Famista \'92, Wagyan Land 3',
    },
    228: {
        'name': 'Action 52',
        'examples': 'Action 52, Cheetah Men II',
    },
    232: {
        'name': 'Camerica/Codemasters Quattro',
        'examples': 'Quattro Adventure, Quattro Sports, Quattro Arcade',
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
