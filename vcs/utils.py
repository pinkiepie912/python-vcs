"""
vcs.utils
==============

"""

import os
from pathlib import PosixPath
from typing import Optional

from .exceptions import NotDirectoryError


def create_dir(root_path: PosixPath, *path: str) -> Optional[str]:
    path = os.path.join(root_path, *path)
    if os.path.exists(path):
        if os.path.isdir(path):
            return path
        else:
            raise NotDirectoryError(path)

    os.makedirs(path)
    return path
