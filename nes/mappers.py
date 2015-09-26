'''
    TODO
'''

NES_MAPPERS = {
    2: {
        'name': 'UxROM',
        'examples': 'Mega Man, Castlevania, Contra, Duck Tales, Metal Gear',
    }
}


def find(mapper_id):
    '''
        TODO
    '''
    try:
        return NES_MAPPERS[mapper_id]
    except KeyError:
        return {
            'name': 'Unknown',
            'examples': 'None'
        }
