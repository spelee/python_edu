
class ExceptionClass1(Exception):
    pass


class ExceptionClass2(Exception):
    pass


def high_level():
    try:
        print('- ** high_level: enter try')

        under_level()

        print('- ** high_level: exit try')
    except (ExceptionClass2, ExceptionClass1) as e:
        print('-high_level: enter except')
        print(f'-high_level: Exception caught {e}')

        print('-high_level: exit except')


def under_level():
    try:
        print('under_level: enter try')
        print('under_level: raise ExceptionClass1')
        raise ExceptionClass1()
        print('under_level: exit try *********')
    except (ExceptionClass1) as e:
        print('under_level: enter except')
        print(f'under_level: Exception caught {e}')

        print('under_level: raise ExceptionClass1')
        raise ExceptionClass1()


        print('under_level: exit except')


high_level()
