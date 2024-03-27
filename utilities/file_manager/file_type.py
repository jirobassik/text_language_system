import copy
import magic


def file_type(file):
    file_object = copy.copy(file)
    file_mime_type = magic.from_buffer(file_object.read(1024), mime=True)
    file_object.seek(0)
    return file_mime_type
