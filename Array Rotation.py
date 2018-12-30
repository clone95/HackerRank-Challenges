to_shift = [1, 2, 3, 4, 5, 6]
r = 4


def main(array, rotations):
    for shift in range(1, rotations+1):
        el = array.pop(-1)
        array.insert(0, el)
    return array


if __name__ == '__main__':
    print(main(to_shift, r))
