from math import pi


def area(r):
    if type(r) not in [int, float]:
        raise TypeError('Input should be of numeric value')

    if r < 0:
        raise ValueError('Radius can\' be a negative number')

    return pi * r ** 2


def main():
    radius = [1, 0, -3, True, 'Hello', [1, 2]]

    for r in radius:
        try:
            print(f'Area of circle with {r} is {area(r)}')
        except (ValueError, TypeError) as e:
            print(e)


if __name__ == '__main__':
    main()
