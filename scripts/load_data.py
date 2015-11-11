from zipline.data import load_from_yahoo
import platform
import os
os.path.exists()
os.walk()
d = load_from_yahoo(stocks=['AAPL'], start="2015/09/01", end="2015/10/10")
print(d)