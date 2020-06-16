def encodeToBase62(decimal: int):
    if decimal <= 0:
        return 0
    else:
        BASE62: tuple = tuple('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

        quotient, reminder = divmod(decimal, len(BASE62))
        ans: str = BASE62[reminder]

        while True:
            if quotient == 0:
                break
            else:
                quotient, reminder = divmod(quotient, len(BASE62))
                ans = BASE62[reminder] + ans
        return ans


def encode(string: str):
    if string:
        return encodeToBase62(int.from_bytes(bytes(string, 'utf-8'), "big"))
    else:
        return 'Invalid String!'


if __name__ == "__main__":
    string: str = 'Hello World!'
    print(encode(string))
