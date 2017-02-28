import matplotlib.pyplot as plt


class Bond (object):
    def __init__(self, term, amount, rate):
        self.term = term                    # a term we'll invest in
        self.amount = amount                # a certain amount invested in
        self.rate = rate                    # a yearly interest rate


# short term bonds have a minimum of 2 years, min amount of 1000 and yearly interest rate of 1%
# long term bonds have a minimum of 5 years, min amount of 3000 and a yearly interest of 3%
# we define the short term and long term type for bonds
# we create methods from the attributes of the class bond


class STBond(Bond):
    def __init__(self, amount, rate):
        super(STBond, self).__init__(amount, rate)
        self.amount = 1000
        self.rate = 0.01

    def bond_price(self, term):
        price = (self.amount / ((1 + self.rate) ** term))
        return price

    def build_list(self):
        list_price_bond = []
        for i in range(1, 101):
            list_price_bond.append(self.bond_price(i))
            print(self.bond_price(i))
        return list_price_bond

    def plot_graph(self):
        plt.plot(self.build_list())
        plt.ylabel('Price Bond')
        plt.xlabel('Term')
        plt.show()


class LTBond(Bond):
    def __init__(self, amount, rate):
        super(LTBond, self).__init__(amount, rate)
        self.amount = 3000
        self.rate = 0.03

    def bond_price(self, term):
        price = (self.amount/((1+self.rate)**term))
        return price

    def build_list(self):
        list_price_bond = []
        for i in range(1, 101):
            list_price_bond.append(self.bond_price(i))
            print(self.bond_price(i))
        return list_price_bond

    def plot_graph(self):
        plt.plot(self.build_list())
        plt.ylabel('Price Bond')
        plt.xlabel('Term')
        plt.show()

