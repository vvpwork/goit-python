import re
import os
import sys
import shutil
import zipfile
from transliterate import translit
from pathlib import Path

try:
    path = sys.argv[1]
except IndexError:
    raise Exception('You should enter a valid path')


print(f"Start in {path}")


def normalize_ext(arr):
    newArr = ['.' + i.lower() for i in arr]
    return newArr


images = normalize_ext(['JPEG', 'PNG', 'JPG', 'SVG'])
videos = normalize_ext(['AVI', 'MP4', 'MOV', 'MKV'])
documents = normalize_ext(['DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX'])
music = normalize_ext(['MP3', 'OGG', 'WAV', 'AMR'])
archives = normalize_ext(['ZIP', 'GZ', 'TAR'])

myFiles = {
    "images":  {
        'files': [],
        'extensions': set({})
    },
    "videos": {
        'files': [],
        'extensions': set({})
    },
    "documents": {
        'files': [],
        'extensions': set({})
    },
    "music": {
        'files': [],
        'extensions': set({})
    },
    "archives": {
        'files': [],
        'extensions': set({})
    },
    "others": {
        'files': [],
        'extensions': set({})
    },
}


def normalize_str(string):
    if type(string).__name__ != 'str':
        return ''
    translate_str = translit(string, 'ru', reversed=True)
    result_str = re.sub('[^0-9A-Za-z]', '_', translate_str)
    return result_str


def cope_file_in_path(file, ext, path_file,  path_name):
    path_file_from = os.path.abspath(path_file) + '/' + file + ext
    path_file_to = os.path.abspath(
        '') + '/' + path_name + '/' + normalize_str(file) + ext
    if ext in archives:
        with zipfile.ZipFile(path_file_from, 'r') as z:
            allFiles = z.extractall(f'archives/{file}')
        return

    Path(path_name).mkdir(parents=True, exist_ok=True)
    shutil.copy2(path_file_from, path_file_to)


def addFiles(file, ext, name):
    myFiles[name]['files'].append(file)
    myFiles[name]['extensions'].add(ext)


def delete_dir(path_dir):
    walkGenerator = os.walk(path_dir)
    for filesWalk in walkGenerator:
        for d in filesWalk[1]:
            d_path = filesWalk[0]+'/'+d
            if not os.listdir(d_path):
                os.rmdir(d_path)
                delete_dir(path_dir)


def rename_dir(dir_path):
    walkGenerator = os.walk(dir_path)
    for filesWalk in walkGenerator:
        new_name = normalize_str(os.path.basename(filesWalk[0]))
        path_dir = os.path.dirname(filesWalk[0])
        os.rename(filesWalk[0], path_dir + '/' + new_name)


def find_files(path):
    walkGenerator = os.walk(path)
    for filesWalk in walkGenerator:
        new_name = normalize_str(os.path.basename(filesWalk[0]))
        path_dir = os.path.dirname(filesWalk[0])

        os.rename(filesWalk[0], path_dir + '/' + new_name)
        delete_dir(filesWalk[0])

        for file in filesWalk[2]:
            ext = os.path.splitext(file)[1]
            fileName = os.path.splitext(file)[0]
            file_path = filesWalk[0]

            if ext in images:
                addFiles((fileName, ext, file_path), ext, 'images')
                continue
            if ext in videos:
                addFiles((fileName, ext, file_path), ext, 'videos')
                continue
            if ext in music:
                addFiles((fileName, ext, file_path), ext, 'music')
                continue
            if ext in documents:
                addFiles((fileName, ext, file_path), ext, 'documents')
                continue
            if ext in archives:
                addFiles((fileName, ext, file_path), ext, 'archives')
                continue
            addFiles((fileName, ext, file_path), ext, 'others')

    for key in myFiles.keys():
        files = myFiles[key]['files']
        if not len(files):
            continue
        for file in files:
            cope_file_in_path(file[0], file[1], file[2], key)


def main(path):
    rename_dir(path)
    find_files(path)


if __name__ == '__main__':
    main(path)
