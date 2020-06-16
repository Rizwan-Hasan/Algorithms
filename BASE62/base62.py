# def bytes_to_int(barray, byteorder="big", signed=False):
#     """Converts a byte array to an integer value.
#     Python 3 comes with a built-in function to do this, but we would like to
#     keep our code Python 2 compatible.
#     """

#     try:
#         return int.from_bytes(barray, byteorder, signed=signed)
#     except AttributeError:
#         # For Python 2.x
#         if byteorder != "big" or signed:
#             raise NotImplementedError()

#         # NOTE: This won't work if a generator is given
#         n = len(barray)
#         ds = (x << (8 * (n - 1 - i)) for i, x in enumerate(bytearray(barray)))

#         return sum(ds)


def toBase62(decimal: int):
    if decimal <= 0:
        return 0
    else:
        base: int = 62
        baseDB: tuple = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

        quotient, reminder = divmod(decimal, base)
        ans: str = baseDB[reminder]

        while True:
            if quotient == 0:
                break
            else:
                quotient, reminder = divmod(quotient, base)
                ans = baseDB[reminder] + ans
        return ans


def stringToBase62(string: str):
    if string:
        # return toBase62(bytes_to_int(bytes(string, 'utf-8')))
        return toBase62(int.from_bytes(bytes(string, 'utf-8'), "big"))
    else:
        return 'Invalid String!'


if __name__ == "__main__":
    string: str = 'Hello World!'
    print(stringToBase62(string))
