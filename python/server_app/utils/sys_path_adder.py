import sys
import inspect
import os

curr_frame = inspect.currentframe().f_code.co_filename

# ../client_app
src_path = curr_frame.rsplit("/", maxsplit=2)[0]
# ../python
python_dir_path = curr_frame.rsplit("/", maxsplit=3)[0]
proto_path = os.path.join(python_dir_path, "proto")
sys.path.append(src_path)
sys.path.append(python_dir_path)
sys.path.append(proto_path)

def folders_to_add(folders, suffix=None):
    sys.path.append(src_path)
    if suffix:
        _src_path = src_path + "/" + suffix
    else:
        _src_path = src_path + "/"
    for folder in folders:
        sys.path.append(_src_path + folder)
