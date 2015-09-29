'''
    The current build information can be found within this module. Instead of
    hard coding version and author information this module can be used to fetch
    the data instead.
'''


def build():
    '''
        Returns all build settings and information.
    '''

    return {
        'author': 'Corey Prophitt',
        'author_email': 'prophitt.corey@gmail.com',
        'major_version': 1,
        'minor_version': 2,
    }
