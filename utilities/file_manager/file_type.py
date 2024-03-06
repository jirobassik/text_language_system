import magic


def file_type(file):
    file_object = file
    file_mime_type = magic.from_buffer(file_object.read(1024), mime=True)
    file_object.seek(0)
    print(file_mime_type)
    return file_mime_type
