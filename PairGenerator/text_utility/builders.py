import random


def build_sentence_groups(sents, target_size=1000):
    target_size = min(len(sents), target_size)

    result = []
    used = set()
    i = 0

    single_count = int(target_size * 0.5)
    double_count = int(target_size * 0.3)
    triple_count = int(target_size * 0.1)
    quad_count = target_size - (single_count + double_count + triple_count)  # решта

    while i < len(sents) - 4 and len(result) < target_size:
        if single_count > 0 and i not in used:
            result.append(sents[i])
            used.add(i)
            i += 1
            single_count -= 1
        elif double_count > 0 and all(j not in used for j in range(i, i+2)):
            result.append(" ".join(sents[i:i+2]))
            used.update(range(i, i+2))
            i += 2
            double_count -= 1
        elif triple_count > 0 and all(j not in used for j in range(i, i+3)):
            result.append(" ".join(sents[i:i+3]))
            used.update(range(i, i+3))
            i += 3
            triple_count -= 1
        elif quad_count > 0 and all(j not in used for j in range(i, i+4)):
            result.append(" ".join(sents[i:i+4]))
            used.update(range(i, i+4))
            i += 4
            quad_count -= 1
        else:
            i += 1

    return result

def build_random_pairs(sentences):
    sampled = random.sample(sentences, len(sentences))
    pairs = [(sampled[i], sampled[i+1]) for i in range(0, len(sampled), 2)]
    return pairs