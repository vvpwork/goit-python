import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

# files - это список имен файлов и папок в path.
files = os.listdir(path)

images = ('JPEG', 'PNG', 'JPG')
videos = ('AVI', 'MP4', 'MOV')
documents = ('DOC', 'DOCX', 'TXT')
music = ('MP3', 'OGG', 'WAV', 'AMR')

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
    "others": {
        'files': [],
        'extensions': set({})
    },
}


def addFiles(file, ext, name):
    myFiles[name]['files'].append(file)
    myFiles[name]['extensions'].add(ext)


for file in files:

    ext = os.path.splitext(file)[1].replace('.', '').upper()

    if ext in images:
        addFiles(file, ext, 'images')
        continue
    if ext in videos:
        addFiles(file, ext, 'videos')
        continue
    if ext in music:
        addFiles(file, ext, 'music')
        continue
    if ext in documents:
        addFiles(file, ext, 'documents')
        continue

    addFiles(file, ext, 'others')

for key in myFiles.keys():
    print(
        f'{key.capitalize()} files: { myFiles[key]["files"]  } extensions: {myFiles[key]["extensions"]}')
