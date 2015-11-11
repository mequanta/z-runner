#!/usr/bin/env python

import sys

import logbook

from hosting.local.cli import run_pipeline
from zipline.utils import parse_args

if __name__ == "__main__":
    logbook.StderrHandler().push_application()
    parsed = parse_args(sys.argv[1:])
    run_pipeline(**parsed)
    sys.exit(0)
