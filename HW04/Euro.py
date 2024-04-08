from Money import Money, get_rates

class Euro(Money):
    def __str__(self):
        return f'{self._quantity}€'

    def __repr__(self):
        return f"Euro({self._quantity})"

    def amount(self):
        rates = get_rates()
        return self.get_quantity() * rates['Euro']

    def get_type(self):
        return 'Euro'

    def aplly_helper(self, arg):
        return Euro(arg)