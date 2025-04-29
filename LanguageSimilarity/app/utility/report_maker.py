def save_report_md(algos, texts, similarities, filename):
    lines = [f"# Result\n\n",
             "| Algorithm | Min diff | Max diff | Avg diff |\n",
             "|-----------|----------|----------|----------|\n"]

    for algo_name, _ in algos.items():
        diffs = [abs(similarities[(algo_name, text1, text2)] - expected) for pairs in texts.values() for text1, text2, expected in pairs ]
        min_diff = min(diffs)
        max_diff = max(diffs)
        avg_diff = sum(diffs)/len(diffs)
        lines.append(f"| {algo_name} | {min_diff:.2f} | {max_diff:.2f} | {avg_diff:.2f} |\n")

    lines.append("\n# Examples\n")

    for name, pairs in texts.items():
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

def save_table_md(algos, texts, filename, content_func):
    lines = []
    algo_names = list(algos.keys())

    for name, pairs in texts.items():
        lines.append(f"\n**{name.upper()}**\n\n")
        lines.append("<table>\n")
        lines.append("  <tr>\n")
        lines.append("    <th>Text pairs</th>\n")
        for algo in algo_names:
            lines.append(f"    <th>{algo}</th>\n")
        lines.append("  </tr>\n")

        for text1, text2, expected in pairs:
            # Форматування коду HTML'ем
            pair_display = (
                f"<pre><code>{text1}</code></pre>"
                f"<pre><code>{text2}</code></pre>"
            )
            lines.append("  <tr>\n")
            lines.append(f"    <td>{pair_display}</td>\n")
            for algo in algo_names:
                content = content_func(text1, text2, expected, algo)
                lines.append(f"    <td>{content}</td>\n")
            lines.append("  </tr>\n")

        lines.append("</table>\n")

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)