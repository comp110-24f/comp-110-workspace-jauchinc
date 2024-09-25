def remove_chars(msg: str, char: str) -> str:
    """return a copy of msg with all instances of char removed."""
    copy: str = ""  # set up empty str to copy values over
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"
print(remove_chars(msg=word, char="y"))
