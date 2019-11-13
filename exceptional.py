def convert(s):
    '''Convert to an integer.'''
    try: 
        x = int(s)
        print('conversion successful')
    except ValueError:
        print('conversion failed - value')
        x = -1
    except TypeError:
        print('Coversion failed - type')
        x = -1
    return x