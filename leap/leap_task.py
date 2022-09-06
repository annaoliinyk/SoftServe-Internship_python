# Task from https://exercism.org/tracks/python/exercises/leap

def leap_year(year):
    return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)


def main():
    print(leap_year(1996))
    print(leap_year(2000))
    print(leap_year(1997))


if __name__ == "__main__":
    main()
