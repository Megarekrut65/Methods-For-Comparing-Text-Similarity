import collections # https://jacobfilipp.com/DrDobbs/articles/DDJ/1988/8807/8807c/8807c.htm


def get_similarity(text1:str, text2: str) -> float:
    """
    gestalt pattern matching
    :param text1:
    :param text2:
    :return:
    """
    size = len(text1) + len(text2)

    if not size:
        return 1.0

    intersect = (collections.Counter(text1) & collections.Counter(text2))
    matches = sum(intersect.values())
    return 2.0 * matches / size