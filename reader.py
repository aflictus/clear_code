from utils import ReaderMethods


class Reader(ReaderMethods):
    """
    Reader(file='file path')

    This class is basic object which used to create all subjects.
    """
    def __init__(self, file: str):
        super(Reader, self).__init__(file)


if __name__ == '__main__':
    try:
        test = Reader('test.jpg')
        test.save('new.png', file_path='C:/Users/HP/Desktop/my/')
    except Exception as ex:
        print(ex)



