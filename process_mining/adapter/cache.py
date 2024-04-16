from pathlib import Path


class CacheHandler:
    def __init__(self, path: Path | str) -> None:
        self.path = path
