import matplotlib.pyplot as plt


class Bond (object):
    def __init__(self, term, amount, rate):
        self.term = term                    # a term we'll invest in
        self.amount = amount                # a certain amount invested in
        self.rate = rate                    # a yearly interest rate

# short term bonds have a minimum of 2 years, min amount of 1000 and yearly interest rate of 1%
# long term bonds have a minimum of 5 years, min amount of 3000 and a yearly interest of 3%

    def plot_graph(self):
        plt.plot(self.build_list())
        plt.ylabel('Price Bond')
        plt.xlabel('Maturity')
        plt.show()

    def build_list(self):
        list_price_bond = []
        for i in range(1, 101):
            list_price_bond.append(self.bond_price(i, 10000, 0.03))
            print(bond_price(i, 10000, 0.03))
        return list_price_bond

    def bond_price(self, term, amount, rate):
        price_bond = (amount/((1+rate)**term))
        return price_bond
