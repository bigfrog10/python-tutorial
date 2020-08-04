def comma(given):
    return '{:,}'.format(given)


if __name__ == '__main__':
    x = comma(1000000000000)
    print(x)
