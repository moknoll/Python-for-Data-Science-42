def give_bmi(height: list[int | float],
             weight: list[int | float]) -> list[int | float]:
    """The function takes 2 lists of integers
    or floats in input and returns a listof BMI values"""
    try:
        if len(height) != len(weight):
            raise ValueError("Lists dont have same length.")
        res = []

        for h, w in zip(height, weight):
            if not isinstance(h, (int, float))\
                    or not isinstance(w, (int, float)):
                raise TypeError("Value is not of type Int or Float")
            elif h <= 0 or w < 0:
                raise ValueError("Value cannot be negative")
            else:
                bmi = (w / h**2)
                res.append(bmi)
    except Exception as e:
        print(Exception.__name__ + ":", e)
    else:
        return res


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """Acepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of boolean"""
    try:
        if limit < 0:
            raise ValueError("Limit cannot be negative")
        res = []

        for i in bmi:
            if not isinstance(i, (int, float)):
                raise TypeError("Value is not of type Int or Float")
            elif i < 0:
                raise ValueError("Value cannot be negative")
            res.append(i > limit)
    except Exception as e:
        print(Exception.__name__ + ":", e)
    else:
        return res
