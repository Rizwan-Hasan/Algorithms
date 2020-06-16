def toBase62(decimal: int):
    if decimal <= 0:
        return 0
    else:
        base: int = 62
        baseDB: tuple = tuple('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

        quotient, reminder = divmod(decimal, base)
        ans: str = baseDB[reminder]

        while True:
            if quotient == 0:
                break
            else:
                quotient, reminder = divmod(quotient, base)
                ans = baseDB[reminder] + ans
        return ans


if __name__ == "__main__":
    print(toBase62(65))  # Expected 13
