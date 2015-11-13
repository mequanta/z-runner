import pandas as pd
import zipline
from zipline.errors import NoSourceError, PipelineDateError

def run_pipeline(print_algo=True, **kwargs):
    """Runs a full zipline pipeline given configuration keyword
    arguments.

    1. Load data (start and end dates can be provided a strings as
    well as the source and symobls).

    2. Instantiate algorithm (supply either algo_text or algofile
    kwargs containing initialize() and handle_data() functions). If
    algofile is supplied, will try to look for algofile_analyze.py and
    append it.

    3. Run algorithm (supply capital_base as float).

    4. Return performance dataframe.

    :Arguments:
        * print_algo : bool <default=True>
           Whether to print the algorithm to command line. Will use
           pygments syntax coloring if pygments is found.

    """
    start = kwargs['start']
    end = kwargs['end']
    # Compare against None because strings/timestamps may have been given
    if start is not None:
        start = pd.Timestamp(start, tz='UTC')
    if end is not None:
        end = pd.Timestamp(end, tz='UTC')

    # Fail out if only one bound is provided
    if ((start is None) or (end is None)) and (start != end):
        raise PipelineDateError(start=start, end=end)

    # Check if start and end are provided, and if the sim_params need to read
    # a start and end from the DataSource
    if start is None:
        overwrite_sim_params = True
    else:
        overwrite_sim_params = False

    symbols = kwargs['symbols'].split(',')
    asset_identifier = kwargs['metadata_index']

    # Pull asset metadata
    asset_metadata = kwargs.get('asset_metadata', None)
    asset_metadata_path = kwargs['metadata_path']
    # Read in a CSV file, if applicable
    if asset_metadata_path is not None:
        if os.path.isfile(asset_metadata_path):
            asset_metadata = pd.read_csv(asset_metadata_path,
                                         index_col=asset_identifier)

    source_arg = kwargs['source']
    source_time_column = kwargs['source_time_column']

    if source_arg is None:
        raise NoSourceError()

    elif source_arg == 'yahoo':
        source = zipline.data.load_bars_from_yahoo(
            stocks=symbols, start=start, end=end)

    elif os.path.isfile(source_arg):
        source = zipline.data.load_prices_from_csv(
            filepath=source_arg,
            identifier_col=source_time_column
        )

    elif os.path.isdir(source_arg):
        source = zipline.data.load_prices_from_csv_folder(
            folderpath=source_arg,
            identifier_col=source_time_column
        )

    else:
        raise NotImplementedError(
            'Source %s not implemented.' % kwargs['source'])

    algo_text = kwargs.get('algo_text', None)
    if algo_text is None:
        # Expect algofile to be set
        algo_fname = kwargs['algofile']
        with open(algo_fname, 'r') as fd:
            algo_text = fd.read()

    if print_algo:
        if PYGMENTS:
            highlight(algo_text, PythonLexer(), TerminalFormatter(),
                      outfile=sys.stdout)
        else:
            print_(algo_text)

    algo_text = '''
from zipline.api import order, record, symbol, order_target
import logbook
logbook.StderrHandler().push_application()
log = logbook.Logger()
''' + algo_text + '''



'''

    algo = zipline.TradingAlgorithm(script=algo_text,
                                    namespace=kwargs.get('namespace', {}),
                                    capital_base=float(kwargs['capital_base']),
                                    algo_filename=kwargs.get('algofile'),
                                    equities_metadata=asset_metadata,
                                    identifiers=symbols,
                                    start=start,
                                    end=end)

    perf = algo.run(source, overwrite_sim_params=overwrite_sim_params)

    output_fname = kwargs.get('output', None)
    if output_fname is not None:
        perf.to_pickle(output_fname)

    return perf