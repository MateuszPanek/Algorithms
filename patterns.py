class Single(object):

    __present = False
    param = 'Jestem Singlem'

    def __init__(self):
        if Single.__present:
            raise Exception('I am groot')
        Single.__present = True


s = Single()
b = Single()