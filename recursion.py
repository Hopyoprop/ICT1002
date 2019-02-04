def main(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return main(n-1) + main(n-2)


if __name__ == "__main__":
    print(main(100))
