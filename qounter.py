import argparse as ap
from src import categorised_force as cf
from src import csv_handler


parser = ap.ArgumentParser(description="A tool for calculating known partial sums of an unknown subset of a list")

parser.add_argument("-f", "--file", nargs=1, metavar="path", type=str, 
                    help="path to CSV input data")
parser.add_argument("-s", "--sum", nargs=1, metavar="num", type=int, 
                    help="partial sum that needs to be calculated using the elements from the input data")

args = parser.parse_args()

sums = csv_handler.csv_to_lst(args.file[0])

cf.rec_sum_search(sums, key=args.sum[0])
