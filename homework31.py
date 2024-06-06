# Գրել Calculator class, որը․
#    - __init__ ում կստանա թիվ և կստուգի այդ թվի int կամ float լինելը, հակառակ դեպքում կվերադարձնի Error,
#    - կունենա միայն getter մեթոդ տրված թիվը ստանալու համար, իսկ այդ թիվը կլինի private,
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+, -, *, /, //, %, **),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (+=, -=, *=, /=, //=, %=, **=),
#    - կունենա համապատասխան magic մեթոդներ հետևյալ գործողությունների համար (==, >, >=, <, <=, !=),
#    - վերոնշյալ մեթոդները ռեալիզացված կլինեն այնպես, որ աշխատեն նաև Calculator կլասի երկու օբյեկտների համար,
#    - կունենա համապատասխան magic մեթոդներ, որոնք թույլ կտան օբյեկտը տպելուց․ ստանալ թիվը (__str__), ստանալ թիվը և թվի տիպը (__repr__)։


class Calculator:
    def __init__(self, num):
        if not isinstance(num, (int, float)):
            raise ValueError("Error: Input must be an integer or float.")
        self.__num = num

    @property
    def number(self):
        return self.__num

    def __str__(self):
        return str(self.__num)

    def __repr__(self):
        return f"Calculator({self.__num})"

    # +
    def __add__(self, other):
        return self.__num + other.number

    # -
    def __sub__(self, other):
        return self.__num - other.number

    # *
    def __mul__(self, other):
        return self.__num * other.number

    # /
    def __truediv__(self, other):
        return self.__num / other.number

    # //
    def __floordiv__(self, other):
        return self.__num // other.number

    # %
    def __mod__(self, other):
        return self.__num % other.number

    # **
    def __pow__(self, other):
        return self.__num ** other.number

    # +=
    def __iadd__(self, other):
        self.__num += other.number
        return self

    # -=
    def __isub__(self, other):
        self.__num -= other.number
        return self

    # *=
    def __imul__(self, other):
        self.__num *= other.number
        return self

    # /=
    def __itruediv__(self, other):
        self.__num /= other.number
        return self

    # //=
    def __ifloordiv__(self, other):
        self.__num //= other.number
        return self

    # %=
    def __imod__(self, other):
        self.__num %= other.number
        return self

    # **=
    def __ipow__(self, other):
        self.__num **= other.number
        return self

    # ==
    def __eq__(self, other):
        return self.__num == other.number

    # >
    def __gt__(self, other):
        return self.__num > other.number

    # >=
    def __ge__(self, other):
        return self.__num >= other.number

    # <
    def __lt__(self, other):
        return self.__num < other.number

    # <=
    def __le__(self, other):
        return self.__num <= other.number

    # !=
    def __ne__(self, other):
        return self.__num != other.number


calc1 = Calculator(10)
calc2 = Calculator(5)
print(calc1 + calc2) 
print(calc1 - calc2)
print(calc1 * calc2)
print(calc1 / calc2)
print(calc1 // calc2)
print(calc1 % calc2)
print(calc1 ** calc2)
print(calc1 == calc2)
print(calc1 > calc2) 
print(calc1 >= calc2)
print(calc1 < calc2)
print(calc1 <= calc2)
print(calc1 != calc2)
