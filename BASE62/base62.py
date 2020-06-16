import os
os.system('clear')


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
        decimal: int = int.from_bytes(bytes(string, 'utf-8'), 'big')
        return encodeToBase62(decimal)
    else:
        return 'Invalid String!'


def decode(string: str):
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    base = len(alphabet)
    strlen = len(string)
    num = 0

    idx = 0
    for char in string:
        power = (strlen - (idx + 1))
        num += alphabet.index(char) * (base**power)
        idx += 1

    return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('utf-8')


if __name__ == "__main__":
    string: str = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    print(encode(string))
    print(decode(encode(string)))