from random import choice

from utility import read_json, write_json


def main():
    # extract_sentences("Files/input.txt", "Files/sentences1.json", 1000)
    # extract_sentences("Files/input.txt", "Files/sentences2.json", 1000)
    sentences1 = read_json("Files/sentences1.json")
    sentences2 = read_json("Files/sentences2.json")

    pairs = []
    for sentence1 in sentences1:
        pair = {
            "text1": sentence1,
            "text2": choice(sentences2),
        }
        pairs.append(pair)

    write_json("Files/diff-pairs.json", pairs)

if __name__ == "__main__":
    main()
