from zipline import TradingAlgorithm as _TradingAlgorithm

from zipline.protocol import Order, Portfolio, Position, Account
from zipline.assets import Equity


class ExecutionTimeout(StandardError):
    pass

class QuantopianTradingAlgorithm(_TradingAlgorithm):
    pass


def symbol():
    pass


def symbols():
    pass


def set_symbol_lookup_date():
    pass


def sid(security_id):
    pass


def update_universe(sids):
    pass


def fetch_csv(url, pre_func=None, post_func=None, universe_func=None, date_column='date',
              date_format='%m/%d/%y', timezone='UTC', symbol=None, mask=True, **kwargs):
    pass
