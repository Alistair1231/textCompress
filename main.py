# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import binascii
import zlib
import base64
import pyperclip


def compress(text: str):
    compressed = base64.b64encode(zlib.compress(text.encode())).decode()
    return compressed


def decompress(text: str):
    decompressed = zlib.decompress(base64.b64decode(text.encode())).decode()
    return decompressed


if __name__ == '__main__':
    text = pyperclip.paste()

    compressed = compress(text)
    print("\ncompress:\n" + compressed + "\n")
    pyperclip.copy(compressed)
    try:
        decompressed = decompress(text)
        print("\ndecompress:\n" + decompressed + "\n")
        pyperclip.copy(decompressed)
    except zlib.error as e:
        print("\n"+str(e))
    except binascii.Error as e:
        print("\n"+str(e))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
