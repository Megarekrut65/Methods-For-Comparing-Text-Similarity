from app.nl_algos import ALGOS as NL_ALGOS
from app.nl_texts import TEXTS as NL_TEXTS

from app.pl_algos import ALGOS as PL_ALGOS
from app.pl_texts import TEXTS as PL_TEXTS

from app.utility.report_maker import save_report_md, save_table_md
from app.utility.tests_runner import run_tests

def save_all(data, algos, texts, prefix, folder):
    save_report_md(algos, texts, data, f"{folder}/{prefix}-Report.md")
    save_table_md(algos, texts,f"{folder}/{prefix}-SimilarityTable.md",
                  lambda text1, text2, expected, algo:f"{data[(algo, text1, text2)]:.2f}%")
    save_table_md(algos, texts,f"{folder}/{prefix}-ExpectedTable.md",
                  lambda text1, text2, expected, algo:f"{expected:.2f}%")
    save_table_md(algos, texts,f"{folder}/{prefix}-DiffTable.md",
                  lambda text1, text2, expected, algo:f"{abs(expected-data[(algo, text1, text2)]):.2f}")

def main():
    nl_data = run_tests(NL_ALGOS, NL_TEXTS)
    save_all(nl_data, NL_ALGOS, NL_TEXTS, "NL", "Reports")

    pl_data = run_tests(PL_ALGOS, PL_TEXTS)
    save_all(pl_data, PL_ALGOS, PL_TEXTS, "PL", "Reports")


if __name__ == "__main__":
    main()