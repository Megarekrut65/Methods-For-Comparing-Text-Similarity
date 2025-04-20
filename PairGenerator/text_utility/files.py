import json

from text_utility.base import nlp
from text_utility.builders import build_sentence_groups


def read_sentences(path):
    file = open(path, "r", errors="ignore")
    text = file.read()

    file.close()

    doc = nlp(text.lower())
    return [s.text.strip() for s in doc.sentences if len(s.text.strip().split()) > 3]

def extract_sentences(input_fil, output_file, count):
    sentences = read_sentences(input_fil)
    structured_groups = build_sentence_groups(sentences, count)
    with open(output_file, "w", errors="ignore", encoding="utf-8") as f:
        json.dump(structured_groups, f, ensure_ascii=False, indent=2)