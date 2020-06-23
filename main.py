import pandas as pd
import os
from argparse import ArgumentParser
from bs4 import BeautifulSoup
import numpy as np
import requests
import sys
from Market_functios import *

def parse():
    parser = ArgumentParser(description="Este programa se realiza para analizar 10 randoms stocks del Nasdaq")
    parser.add_argument ("t","--ticker", help="La cantidad de tickers del dataframe", default=10)
    parser.add_argument(("52","--52weekhigk",type=int, help="la performance de las stocks en las ultimas 52 semanas")
    return parser.parse_args()


def main():
    args = parse()
    ticker=args.ticker
    52weekhigk=args.52weekhigh
    