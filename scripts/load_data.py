from zipline.data import load_from_yahoo
d = load_from_yahoo(stocks=['AAPL'], start="2015/09/01", end="2015/10/10")
print(d)