from text_utility.synonym import make_synonym_pair
from utility import read_json, write_json


def main():
    #extract_sentences("Files/input.txt", "Files/sentences.json", 1000)
    sentences = read_json("Files/sentences.json")
    pairs = []
    left = []
    all_left = False

    for sentence in sentences:
        if all_left:
            left.append(sentence)
            continue

        try:
            pair = make_synonym_pair(sentence)
            pairs.append(pair)
        except:
            all_left = True
            left.append(sentence)

    write_json("Files/pairs.json", pairs)
    write_json("Files/sentences.json", left)

if __name__ == "__main__":
    main()
