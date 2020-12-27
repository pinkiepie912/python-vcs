import os
from typing import List

import attr


@attr.s
class Configuration:
    ignore_files: List[str] = attr.ib()
    root_path: str = attr.ib()
    repo_dir_name: str = attr.ib(default=".py_vcm")

    @property
    def repo_dir(self) -> str:
        return os.path.join(self.root_path, self.repo_dir_name)
