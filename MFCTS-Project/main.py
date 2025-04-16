from algorithms import difflib_gestalt_pattern_matching as d_gpm
from algorithms import gestalt_pattern_matching as gpm
from algorithms import sklearn_vectorizer as s_vec
from algorithms import spacy_nlp as s_nlp
from algorithms import sentence_transformers_tensor as stt
from texts import TEXTS

algos = {
   "gestalt pattern matching": gpm.get_similarity,
    "gestalt pattern matching from difflib":d_gpm.get_similarity,
    "sklearn vectorizer":s_vec.get_similarity,
    "semantic similarity with spacy":s_nlp.get_similarity,
    "sentence transformers tensor":stt.get_similarity,
}


def main():
    output_lines = []

    for name, lst in TEXTS.items():
        output_lines.append(f"# {name}\n")

        for idx, (text1, text2) in enumerate(lst, 1):
            output_lines.append(f"### {idx}.\n")
            output_lines.append(f"**a)** {text1}\n\n")
            output_lines.append(f"**b)** {text2}\n\n")

            output_lines.append("| Algorithm | Similarity |\n")
            output_lines.append("|-----------|------------|\n")

            for algo_name, algo in algos.items():
                similarity = algo(text1, text2)

                output_lines.append(f"| {algo_name} | {similarity * 100:.2f}% |\n")

            output_lines.append("\n---\n\n")

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(output_lines)

    # for name, lst in TEXTS.items():
    #     print(LINE, name, LINE)
    #     for text1, text2 in lst:
    #         print(f"a){text1}\nb){text2}")
    #         for algo_name, algo in algos.items():
    #             similarity = algo(text1, text2)
    #             print(f"{algo_name}: {similarity*100:.2f}%")
    #         print("\n\n")
    #
    #     print(LINE, "End",name, LINE, "\n\n")


if __name__ == "__main__":
    main()