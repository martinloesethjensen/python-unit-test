def star_sign(month: int, day: int):
    if type(month) == int and month <= 12 and type(day) == int and day <= 32:  # todo: test case on .isnumeric()
        if month == 1:
            if day <= 20:
                return "Capricorn"
            else:
                return "Aquarius"

        elif month == 5:
            if day <= 21:
                return "Taurus"
            else:
                return "Gemini"
        else:
            if day <= 21:
                return "Sagittarius"
            else:
                return "Capricorn"
    elif type(month) is not int or type(day) is not int:  # todo: test case on typeerror
        raise TypeError("Month and day must be of type int")

    elif 0 <= month > 12 and 0 <= day > 32:  # todo: test case on valueerror
        raise ValueError("Month can't be negative and over 12.\nDay can't be negative either or over 32.")

    return None


if __name__ == '__main__':
    print(star_sign(1.0, 6))
