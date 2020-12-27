from pathlib import PosixPath

from vcs.repository import DEFAULT_REPO_DIR_NAME, REPO_DIR_NAMES, Repository


class TestRepository:
    def test_create(self, tmp_path):
        # given
        path: PosixPath = tmp_path / "test_project"
        path.mkdir()

        # when
        repo = Repository.create(path)

        # then
        assert repo.worktree == path
        assert repo.repo_dir == path / DEFAULT_REPO_DIR_NAME
        for names in REPO_DIR_NAMES:
            assert repo.repo_dir.joinpath(*names).exists()

    def test_find(self, tmp_path):
        # given
        root_path = tmp_path / "test_project"
        root_path.mkdir()

        repo_path = root_path / DEFAULT_REPO_DIR_NAME
        repo_path.mkdir()

        # when
        repo = Repository.find(root_path)

        # then
        assert repo.worktree == root_path
        assert repo.repo_dir == repo_path
