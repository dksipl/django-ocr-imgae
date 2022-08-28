import os, shutil, pathlib, fnmatch

def move_dir(src: str, dst: str, pattern: str = '*'):

    if not os.path.isdir(dst):
        pathlib.Path(dst).mkdir(parents=True, exist_ok=True)
    for f in fnmatch.filter(os.listdir(src), pattern):
        shutil.move(os.path.join(src, f), os.path.join(dst, f))











