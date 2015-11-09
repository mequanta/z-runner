import logbook
import sys

from zipline.utils import parse_args, run_pipeline

if __name__ == "__main__":
    logbook.StderrHandler().push_application()
    parsed = parse_args(sys.argv[1:])
    run_pipeline(**parsed)
    sys.exit(0)
