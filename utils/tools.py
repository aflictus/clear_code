from formats import FILE_FORMATS, EXCEPTION_FORMATS
import os


class ReaderMethods:
    def __init__(self, file: str):
        self.file_path = self.check_file_path(file)
        self.file_name = os.path.basename(self.file_path)
        self.file_format = self.file_name.split('.')[-1].upper()
            
        if self.file_format not in FILE_FORMATS:
            if self.file_format in EXCEPTION_FORMATS:
                raise TypeError("Unsupported file type")
            
            raise TypeError("File must be a picture")
        
        self.read_image()
        

    @classmethod
    def check_file_path(cls, file_path: str):
        if not os.path.isfile(file_path):
            raise ValueError("File not found")
            
        return file_path
    

    def read_image(self):
        self.image = open(self.file_path, 'rb')
        self._header = self.image.read(2)


    def save(self, name: str, file_path: str or None=None):
        """
        save(name="YOUR_NEW_FILE_NAME", file_path="YOUR_NEW_FILE_PATH")

        This function is used to save the image.

        file_path is optional parameter.
        """
        if not name:
            raise ValueError("Name not found")

        if file_path:
            if not os.path.isdir(file_path):
                raise ValueError("Direction not found")
            file = f'{file_path}/{name}'
        else:
            file = name

        with open(file, 'wb') as output_file:
                output_file.write(self._header)
                while True:
                    marker = self.image.read(2)
                    if not marker:
                        break
                    marker_code = marker[0] * 256 + marker[1]
                    if marker_code == 0xFFD9:
                        break
                    else:
                        length = int.from_bytes(self.image.read(2), byteorder='big')
                        if marker_code == 0xFFE1:  
                            self.image.read(6)  
                            length -= 6
                        data = self.image.read(length - 2)
                        
                        output_file.write(marker)
                        output_file.write(length.to_bytes(2, byteorder='big'))
                        output_file.write(data)
    