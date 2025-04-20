import pandas as pd

from utility import read_json


def main():
    pairs = read_json("Files/pairs-full.json")
    df = pd.DataFrame(data=pairs)
    df.to_csv("Files/pairs-full.csv", index=False)

if __name__ == "__main__":
    main()