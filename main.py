from sys import argv
from map_reader import read_tsp
import numpy as np
from plotter import plotmap 




def main():
    if len(argv) != 2:
        print("Correct use: python src/main.py <filename>.tsp")
        return -1
    city_df = read_tsp(argv[1])
    print(city_df.head(5))
    plotmap(city_df)


def plot():
    pass

if __name__ == '__main__':
    main()
