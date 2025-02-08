from typing import Final

AUTHOR: Final[str] = 'Sourav'
VERSION: Final[int] = 1

def greet(name: str) -> None:
    print(f'Hello, {name}')