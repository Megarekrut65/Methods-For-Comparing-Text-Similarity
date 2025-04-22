from algorithms import difflib_gestalt_pattern_matching as d_gpm
from algorithms import gestalt_pattern_matching as gpm
from algorithms import sklearn_vectorizer as s_vec
from algorithms import spacy_nlp as s_nlp
from algorithms import sentence_transformers_tensor as stt
from algorithms import sentence_transformers_tensor_ua as stt_ua
from algorithms import stanza_jaccard as sj
from algorithms import fine_tuned_similarity_model as ft_sm

from texts import TEXTS

algos = {
   "gestalt pattern matching": gpm.get_similarity,
    "gestalt pattern matching from difflib":d_gpm.get_similarity,
    "jaccard algorithm with stanza lematization":sj.get_similarity,
    "sklearn vectorizer":s_vec.get_similarity,
    "semantic similarity with spacy":s_nlp.get_similarity,
    "sentence transformers tensor with multilanguage vectors":stt.get_similarity,
    "sentence transformers tensor with ukrainian vectors":stt_ua.get_similarity,
    "fine tuned similarity model":ft_sm.get_similarity,
}

def save_report_md(similarities, filename):
    lines = [f"# Result\n\n",
             "| Algorithm | Min diff | Max diff | Avg diff |\n",
             "|-----------|----------|----------|----------|\n"]

    for algo_name, _ in algos.items():
        diffs = [abs(similarities[(algo_name, text1, text2)] - expected) for pairs in TEXTS.values() for text1, text2, expected in pairs ]
        min_diff = min(diffs)
        max_diff = max(diffs)
        avg_diff = sum(diffs)/len(diffs)
        lines.append(f"| {algo_name} | {min_diff:.2f} | {max_diff:.2f} | {avg_diff:.2f} |\n")

    lines.append("\n# Examples\n")

    for name, pairs in TEXTS.items():
        lines.append(f"## {name}\n")

        for idx, (text1, text2, expected) in enumerate(pairs, 1):
            lines.append(f"### {idx}.\n")
            lines.append(f"**a)** {text1}\n\n")
            lines.append(f"**b)** {text2}\n\n")

            lines.append("| Algorithm | Similarity | Expected | Diff |\n")
            lines.append("|-----------|------------|----------|------|\n")

            for algo_name, _ in algos.items():
                similarity = similarities[(algo_name, text1, text2)]

                lines.append(f"| {algo_name} | {similarity:.2f}% | {expected:.2f}% | "
                             f"{abs(expected-similarity):.2f} |\n")

            lines.append("\n---\n\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)

def save_table_md(filename, content_func):
    lines = []

    algo_names = list(algos.keys())

    for name, pairs in TEXTS.items():
        lines.append(f"\n**{name.upper()}**\n\n")

        header_cols = ["Text pairs"] + algo_names
        header = "| " + " | ".join(header_cols) + " |"
        separator = "| " + " | ".join(["-" * len(col) for col in header_cols]) + " |"
        lines.extend([header + "\n", separator + "\n"])

        for text1, text2, expected in pairs:
            pair_display = f"{text1}<br><br>{text2}"
            row = [pair_display]
            for algo in algo_names:
                content = content_func(text1, text2, expected, algo)
                row.append(content)
            lines.append("| " + " | ".join(row) + " |\n")

    # Запис у файл
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)



def run_tests():
    similarities = {}

    for name, pairs in TEXTS.items():
        for idx, (text1, text2, _) in enumerate(pairs, 1):
            for algo_name, algo in algos.items():
                similarity = algo(text1, text2)
                similarities[(algo_name, text1, text2)] = similarity * 100

    return similarities

def main():
    data = run_tests()
    save_report_md(data, "README.md")
    save_table_md("SimilarityTable.md",
                  lambda text1, text2, expected, algo:f"{data[(algo, text1, text2)]:.2f}%")
    save_table_md("ExpectedTable.md",
                  lambda text1, text2, expected, algo:f"{expected:.2f}%")
    save_table_md("DiffTable.md",
                  lambda text1, text2, expected, algo:f"{abs(expected-data[(algo, text1, text2)]):.2f}")






if __name__ == "__main__":
    main()