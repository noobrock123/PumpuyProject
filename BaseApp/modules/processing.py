import igpu

class processing:

    def process(file = None):
        if file == None:
            raise EmptyFileError
        try:
            gpu = igpu.get_device(0)
        except:
            print("Not supported")
        print(gpu.name)
        return True
    
class EmptyFileError(Exception):
    pass