

import pandas as pd
from random import choice

from code_changer import rename_code


def generate_similar_code(df):
    result = []

    for idx, row in df.iterrows():
        code1 = str(row.get("chosen", "")).strip()
        if not code1:
            continue

        code2 = rename_code(code1)
        if code1 != code2:
            result.append({
                "anchor": code1,
                "positive": code2
            })

    return result

def read_codes(input_csv):
    df = pd.read_csv(input_csv)
    return df.dropna()

if __name__ == "__main__":
    df = read_codes("Files/dataset.csv")
    res1 = generate_similar_code(df)

    codes = df["chosen"].astype(str).tolist()
    for item in res1:
        rand = choice(codes)
        item["negative"] = rand

    df = pd.DataFrame(res1)
    df.to_csv("Files/3pairs.csv", index=False)
