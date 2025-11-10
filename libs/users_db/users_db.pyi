from typing import Optional


type User = tuple[str, str, str]
type UUID = str


class UsersDb:
    def append(self, password: str, email: str, name: str) -> Optional[UUID]: ...

    def discard(self, target: str) -> Optional[UUID]: ...

    def get(self, target: str) -> Optional[User]: ...

    def set(self, target: str, data: dict) -> None: ...

