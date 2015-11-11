def get_pricing(symbols, start_date='2013-01-03', end_date='2014-01-03', symbol_reference_date=None, frequency='daily',
                fields=None, handle_missing='raise'):
    pass


def symbols(symbols, symbol_reference_date=None, handle_missing='log'):
    pass


def local_csv(path, symbol_column=None, date_column=None, use_date_column_as_index=True, timezone='UTC',
              symbol_reference_date=None, **read_csv_kwargs):
    pass

def get_backtest(backtest_id):
    pass

def get_fundamentals(query, base_date, range_specifier=None, filter_ordered_nulls=None):
    pass


class AlgorithmResult:
    def __init__(self, result_iterator, progress_bar, algo_id):
        pass

    def create_full_tear_sheet(self, benchmark_rets=None, live_start_date=None, bayesian=False, cone_std=1.0):
        pass


class BacktestResult(AlgorithmResult):
    pass
