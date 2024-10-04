"""Some scope examples."""


def remove_chars(msg: str, char: str) -> str:
    """Return a copy of msg with all instances of char removed."""
    copy: str = ""
    # Line 3 sets up empty str to copy values over.
    index: int = 0
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]
            # Can reword to copy += msg[index]
        index += 1
    return copy


word: str = "yoyo"  # Global variable.
print(remove_chars(word, "y"))
print(remove_chars(word, "o"))
# You are able to do (word, "y") because of positional arguments.
