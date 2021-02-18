import os
import sys

# path содержит первый аргумент, считаем, что это валидный адрес в файловой системе
path = sys.argv[1]
print(f"Start in {path}")

images = ('JPEG', 'PNG', 'JPG', 'SVG')
videos = ('AVI', 'MP4', 'MOV', 'MKV')
documents = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
music = ('MP3', 'OGG', 'WAV', 'AMR')
archives = ('ZIP', 'GZ', 'TAR')

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


def addFiles(file, ext, name):
    myFiles[name]['files'].append(file)
    myFiles[name]['extensions'].add(ext)


def find_files(path):
    walkGenerator = os.walk(path)
    for filesWalk in walkGenerator:
        for file in filesWalk[2]:
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
            if ext in archives:
                addFiles(file, ext, 'archives')
                continue
            addFiles(file, ext, 'others')

    for key in myFiles.keys():
        files = myFiles[key]['files']
        extensions = myFiles[key]["extensions"]
        if not len(files):
            continue
        print(
            f'{key.capitalize()} files: { files } extensions: { extensions if len(extensions) else "" }')


if __name__ == "__main__":
    find_files(path)
