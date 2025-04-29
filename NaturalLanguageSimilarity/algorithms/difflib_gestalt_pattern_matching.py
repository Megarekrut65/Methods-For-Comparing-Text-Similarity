import difflib # https://docs.python.org/uk/3/library/difflib.html

def get_similarity(text1:str, text2:str)->float:
    """
    gestalt pattern matching
    :param text1:
    :param text2:
    :return:
    """
    return difflib.SequenceMatcher(None, text1, text2).ratio()