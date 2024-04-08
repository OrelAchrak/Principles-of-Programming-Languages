rates = {"Dollar": float(input("Enter the Dollar to Shekel ratio: ")),
         "Euro": float(input("Enter the Euro to Shekel ratio: ")),
         "Shekel": 1}


def get_rates():
    return rates


def add(self, other):
    return self + other


def apply(args, self, other):
    if args == "add":
        return self.aplly_helper((self + other) / rates[self.get_type()])
    elif args == "sub":
        return self.aplly_helper((self - other) / rates[self.get_type()])


def coerce_apply(args, self, other):
    from Shekel import Shekel
    if args == "add":
        return apply("add", Shekel(0), apply("add", self, other))
    if args == "sub":
        return apply("add", Shekel(0), apply("sub", self, other))


class Money(object):

    def __init__(self, quantity):
        self._quantity = quantity

    def get_quantity(self):
        return self._quantity

    def set_quantity(self, quantity):
        self._quantity = quantity
        return self

    '''def __add__(self, other):
        if self.amount() and other.amount():
            return self.amount() + other.amount()
        elif self.amount() and not other.amount():
            return self.amount() + other.get_quantity()
        elif not self.amount() and other.amount():
            return self.get_quantity() + other.amount()
        elif not self.amount() and not other.amount():
            return self.get_quantity() + other.get_quantity()
        else:
            return False'''

    def __add__(self, other):
        from Shekel import Shekel
        if not (isinstance(self, Shekel) and isinstance(other, Shekel)):
            return self.amount() + other.amount()
        elif not isinstance(self, Shekel) and isinstance(other, Shekel):
            return self.amount() + other.get_quantity()
        elif isinstance(self, Shekel) and not isinstance(other, Shekel):
            return self.get_quantity() + other.amount()
        elif isinstance(self, Shekel) and isinstance(other, Shekel):
            return self.get_quantity() + other.get_quantity()
        else:
            return False

    def __sub__(self, other):
        from Shekel import Shekel
        if not (isinstance(self, Shekel) and isinstance(other, Shekel)):
            return self.amount() - other.amount()
        elif not isinstance(self, Shekel) and isinstance(other, Shekel):
            return self.amount() - other.get_quantity()
        elif isinstance(self, Shekel) and not isinstance(other, Shekel):
            return self.get_quantity() - other.amount()
        elif isinstance(self, Shekel) and isinstance(other, Shekel):
            return self.get_quantity() - other.get_quantity()
        else:
            return False
