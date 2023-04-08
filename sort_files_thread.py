import os
import shutil
import threading


def sort_files_by_extension(source_folder, destination_folder, cb):
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            extension = os.path.splitext(file)[1]
            extension_folder = os.path.join(destination_folder, extension[1:])
            os.makedirs(extension_folder, exist_ok=True)
            source_file = os.path.join(root, file)
            destination_file = os.path.join(extension_folder, file)
            threading.Thread(target=shutil.copy, args=(source_file, destination_file)).start()
    return cb(f'Sorting folder {source_folder} completed successfully')


if __name__ == '__main__':
    source_folder = input('Please input path to source folder: ')
    destination_folder = input('Please input path to destination folder: ')
    sort_files_by_extension(source_folder, destination_folder, print)
