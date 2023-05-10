import igpu
from .process_chooser import process_chooser
class processing:

    def process(self, path, file = None):
        if file == None:
            raise EmptyFileError
        try:
            gpu = igpu.get_device(0)
        except:
            gpu = "cpu"

        p = process_chooser()
        print("testttt")
        p.yolo_v7(path, file)
        return True

class EmptyFileError(Exception):
    pass