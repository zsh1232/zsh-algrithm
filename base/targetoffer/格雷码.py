def graycode(n):
    if n == 1:
        return ['0', '1']
    codes = graycode(n - 1)

    ret = ['0' + x for x in codes]
    codes.reverse()
    ret += ['1' + x for x in codes]
    return ret


if __name__ == '__main__':
    print(graycode(4))
