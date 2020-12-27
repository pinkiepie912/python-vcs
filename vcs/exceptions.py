"""
vcs.exc
=======

Exception definitions.

"""


class RepoDirectoryNotFoundError(RuntimeError):
    """
    Error for no repo directory.
    """

    def __init__(self, path: str):
        super().__init__(f"{path} is not found")


class NotDirectoryError(RuntimeError):
    """
    Error for not directory.
    """

    def __init__(self, path: str):
        super().__init__(f"Not a directory {path}")


class NotFoundError(RuntimeError):
    """
    Error for not found.
    """

    def __init__(self, path: str):
        super().__init__(f"{path} is not found")
