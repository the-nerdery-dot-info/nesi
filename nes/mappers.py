'''
    The mappers package contains all known information about each NES mapper.
    The data here was dug up through various websites. For the sake of history,
    the following sites/docs proved useful:

        1. http://wiki.nesdev.com
        2. http://tuxnes.sourceforge.net/nesmapper.txt
'''

NES_MAPPERS = {
    2: {
        'name': 'UxROM',
        'examples': 'Mega Man, Castlevania, Contra, Duck Tales, Metal Gear',
    }
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
