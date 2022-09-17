class item:
    def __init__(self, price, quant, sale):
        self.price=price
        self.quant=quant
        self.sale=sale
    def calc(self):
        return self.price*self.quant*self.sale

apple=item(10,2,0.8)
print(apple.calc())








