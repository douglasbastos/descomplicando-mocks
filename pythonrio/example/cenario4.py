import os


def remove_files(files):
    for file in files:
        os.remove(file)
