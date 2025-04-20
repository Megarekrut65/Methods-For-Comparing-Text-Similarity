from utility import read_json, write_json



def assume_similarity(pairs):
    for pair in pairs:
        print("1)", pair["text1"].lower())
        print("2)", pair["text2"].lower())
        similarity = int(input("Assume(0-100): "))/100

        pair["similarity"] = similarity

    return pairs

def main():
    pairs = read_json("Files/diff-pairs.json")

    pairs = assume_similarity(pairs)
    write_json("Files/diff-pairs-assumed.json", pairs)

if __name__ == "__main__":
    main()