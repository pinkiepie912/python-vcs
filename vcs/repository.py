"""
vcs.repository
==============

Repository definitions.

"""
from __future__ import annotations

import os
from pathlib import Path, PosixPath
from typing import Optional

from .exceptions import (
    NotDirectoryError,
    NotFoundError,
    RepoDirectoryNotFoundError,
)
from .utils import create_dir

__all__ = ("Repository", "REPO_DIR_NAMES", "DEFAULT_REPO_DIR_NAME")


REPO_DIR_NAMES = [
    ("branches",),
    ("objects",),
    ("refs", "tags"),
    ("refs", "heads"),
]
DEFAULT_REPO_DIR_NAME = ".py_vcs"


class Repository:
    def __init__(
        self, path: PosixPath, repo_dir_name: str = DEFAULT_REPO_DIR_NAME
    ):
        self.worktree: PosixPath = path
        if not repo_dir_name:
            raise ValueError(
                f"repo_dir_name is not specified: {repo_dir_name}"
            )
        self.repo_dir: PosixPath = path / repo_dir_name
        if not os.path.isdir(self.repo_dir):
            raise RepoDirectoryNotFoundError(str(self.repo_dir))

    @classmethod
    def create(
        cls, path: PosixPath, repo_dir_name: str = DEFAULT_REPO_DIR_NAME
    ) -> Repository:
        if not path.exists():
            raise NotFoundError(str(path))

        if not path.is_dir():
            raise NotDirectoryError(str(path))

        repo_dir = path / repo_dir_name
        for names in REPO_DIR_NAMES:
            create_dir(repo_dir, *names)

        with open(repo_dir / "HEAD", "w") as f:
            f.write("ref: refs/heads/main")

        return cls(path, repo_dir_name)

    @classmethod
    def find(
        cls,
        path: Optional[PosixPath] = None,
        repo_dir_name: str = DEFAULT_REPO_DIR_NAME,
    ) -> Repository:
        if not path:
            path = Path(".")
        if not path.exists():
            raise NotFoundError(str(path))

        repo_dir = path / repo_dir_name
        if not repo_dir.exists():
            raise NotFoundError(repo_dir)

        if not repo_dir.is_dir():
            raise NotDirectoryError(repo_dir)

        return Repository(path, repo_dir_name)
