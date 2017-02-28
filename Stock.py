import pandas as pd

AAPL = pd.read_csv('F:\Data\AAPL.csv', delimiter=';')
print(AAPL)

AXP = pd.read_csv('F:\Data\AXP.csv', delimiter=';')
print(AXP)

FDX = pd.read_csv('F:\Data\FDX.csv', delimiter=';')
print(FDX)

GOOGL = pd.read_csv('F:\Data\GOOGL.csv', delimiter=';')
print(GOOGL)

IBM = pd.read_csv('F:\Data\IBM.csv', delimiter=';')
print(IBM)
KO = pd.read_csv('F:\Data\KO.csv', delimiter=';')
print(KO)

MS = pd.read_csv('F:\Data\MS.csv', delimiter=';')
print(MS)

IOK = pd.read_csv('F:\Data\IOK.csv', delimiter=';')
print(IOK)

XOM = pd.read_csv('F:\Data\XOM.csv', delimiter=';')
print(XOM)

YHOO = pd.read_csv('F:\Data\YHOO.csv', delimiter=';')
print(YHOO)


class Stock (object):
    def __init__(self, name, term, amount, number, date):
        self.name = name
        self.term = term
        self.amount = amount
        self.number = number
        self.date = date
