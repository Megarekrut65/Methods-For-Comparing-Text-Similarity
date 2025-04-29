from itertools import combinations

import pandas as pd

from code_changer import rename_code


def generate_similar_code(input_csv):
    df = pd.read_csv(input_csv)
    result = []

    for idx, row in df.iterrows():
        code1 = str(row.get("chosen", "")).strip()
        if not code1:
            continue

        code2 = rename_code(code1)
        if code1 != code2:
            result.append({
                "text1": code1,
                "text2": code2,
                "similarity": 1.0
            })

    return result

def generate_code_pairs(input_csv):
    df = pd.read_csv(input_csv)
    codes = df["chosen"].dropna().astype(str).tolist()

    results = []

    for code1, code2 in combinations(codes, 2):
        print(code1, code2)
        similarity = input("Enter similarity: ")
        results.append({
            "text1": code1.strip(),
            "text2": code2.strip(),
            "similarity": similarity
        })

    return results

if __name__ == "__main__":
    res1 = generate_similar_code("Files/dataset.csv")
    res2 = generate_code_pairs("Files/dataset.csv")

    res = res1 + res2

    df = pd.DataFrame(res)
    df.to_csv("Files/pairs.csv", index=False)
