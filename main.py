from sys import argv
from map_reader import read_tsp
import numpy as np





def main():
    if len(argv) != 2:
        print("Correct use: python src/main.py <filename>.tsp")
        return -1
    problem = read_tsp(argv[1])
    print(problem.head(5))







    

main()