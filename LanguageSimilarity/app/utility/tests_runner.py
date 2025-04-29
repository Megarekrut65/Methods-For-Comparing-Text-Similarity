def run_tests(algos, texts):
    similarities = {}

    for name, pairs in texts.items():
        for idx, (text1, text2, _) in enumerate(pairs, 1):
            for algo_name, algo in algos.items():
                similarity = algo(text1, text2)
                similarities[(algo_name, text1, text2)] = similarity * 100

    return similarities