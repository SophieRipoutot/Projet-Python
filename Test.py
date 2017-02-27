import matplotlib.pyplot as plt


def bond(amount, rate, maturity):
    price_bond = (amount/((1+rate)**maturity))
    return price_bond

for i in range(1, 101):
    list[i] = (bond(10000, 0.03, i))

    plt.plot(range, i)
    plt.ylabel('Price Bond')
    plt.xlabel('Maturity')
    plt.show()

