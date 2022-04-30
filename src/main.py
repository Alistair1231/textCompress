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
    # https://stackoverflow.com/questions/41148489/compressing-simple-text-to-text
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
