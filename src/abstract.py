import abc

class Apliance(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, model, price):
        self.__model = model
        self.price = price

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    price = abc.abstractproperty(get_price, set_price)

    @property
    def model(self):
        return self.__model

class Cooler(Apliance):
    def __init__(self, model, price, fuel):
        super().__init__(model, price)
        self.fuel = fuel
    price = property(lambda self: super().price,
                     lambda self, rice: super().set_price(rice))


if __name__=='__main__':
    cooler = Cooler('toshiba', 12.20, 'lux')