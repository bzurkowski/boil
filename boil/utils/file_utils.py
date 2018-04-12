import contextlib
import os
import shutil
import tempfile


def ensure_dir(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)


@contextlib.contextmanager
def temp_dir():
    tmp_dir = tempfile.mkdtemp()
    try:
        yield tmp_dir
    finally:
        shutil.rmtree(tmp_dir)


def copy_tree(src, dst):
    for name in os.listdir(src):
        src_name = os.path.join(src, name)
        dst_name = os.path.join(dst, name)
        if os.path.isdir(src_name):
            shutil.copytree(src_name, dst_name)
        else:
            shutil.copy2(src_name, dst_name)
