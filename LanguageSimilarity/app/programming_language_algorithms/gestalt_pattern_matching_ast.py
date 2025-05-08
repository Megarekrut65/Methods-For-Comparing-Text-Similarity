from app.programming_language_algorithms.ast_utility import parse_code_to_tokens, remove_comments


def longest_common_substring(seq1, seq2):
    max_len = 0
    start1 = start2 = -1

    for i in range(len(seq1)):
        for j in range(len(seq2)):
            length = 0
            while i + length < len(seq1) and j + length < len(seq2) and seq1[i + length] == seq2[j + length]:
                length += 1
            if length > max_len:
                max_len = length
                start1 = i
                start2 = j

    return start1, start2, max_len

def ratcliff_metzener(seq1, seq2):
    stack = [(seq1, seq2)]
    match_count = 0

    while stack:
        s1, s2 = stack.pop()
        if not s1 or not s2:
            continue

        i1, i2, l = longest_common_substring(s1, s2)
        if l == 0:
            continue

        match_count += l

        stack.append((s1[:i1], s2[:i2]))
        stack.append((s1[i1 + l:], s2[i2 + l:]))

    return match_count

def pattern_similarity(seq1, seq2):
    match_count = ratcliff_metzener(seq1, seq2)

    total_length = len(seq1) + len(seq2)
    return (2 * match_count) / total_length if total_length > 0 else 1.0

def get_similarity(code1: str, code2: str):
    tokens1 = parse_code_to_tokens(remove_comments(code1))
    tokens2 = parse_code_to_tokens(remove_comments(code2))

    similarity = pattern_similarity(tokens1, tokens2)

    return similarity
