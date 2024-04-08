from Money import Money

class Shekel(Money):
    def __str__(self):
        return f'{self._quantity}₪'

    def __repr__(self):
        return f'Shekel({self._quantity})'

    def amount (self):
        return False

    def get_type(self):
        return 'Shekel'

    def aplly_helper(self, arg):
        return Shekel(arg)