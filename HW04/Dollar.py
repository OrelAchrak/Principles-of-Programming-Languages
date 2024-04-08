from Money import Money , get_rates

class Dollar(Money):

    def __str__(self):
        return f'{self._quantity}$'

    def __repr__(self):
        return f'Dollar({self._quantity})'

    def amount(self):
        rates = get_rates()
        return self.get_quantity() * rates['Dollar']

    def get_type(self):
        return 'Dollar'

    def aplly_helper(self, arg):
        return Dollar(arg)



