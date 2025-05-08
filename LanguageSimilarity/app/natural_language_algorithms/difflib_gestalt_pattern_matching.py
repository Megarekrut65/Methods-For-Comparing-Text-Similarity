import difflib


def get_similarity(text1:str, text2:str)->float:
    return difflib.SequenceMatcher(None, text1, text2).ratio()