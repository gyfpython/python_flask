import os


def get_text(file_name):
    file_path = os.path.join('files_for_test', file_name)
    try:
        if os.path.isfile(file_path):
            file = open(file_path)
            return ''.join(file.readlines())
        else:
            return 'file not exist'
    except Exception as error:
        assert error

