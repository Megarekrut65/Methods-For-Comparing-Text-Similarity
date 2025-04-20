import random
import time

import decouple
import google.generativeai as genai

from text_utility.base import nlp

genai.configure(api_key=decouple.config("GENAI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash-lite")

def get_synonym(word:str, feats="", upos="")->str:
    prompt = (
        f"Дай один синонім до слова '{word}' українською мовою. "
        f"Слово має залишитися тією ж частиною мови ({upos.lower()}), "
        f"і мати ті ж граматичні характеристики: {feats if feats else 'будь-які'}. "
        f"Відповідь має містити лише одне слово, у потрібній граматичній формі, без пояснень."
    )

    response = model.generate_content(prompt)
    result = response.text.strip().split()[0]
    if result.lower() != word.lower():
        return result

    return word

def synonymize(text):
    doc = nlp(text)
    new_tokens = []
    for sent in doc.sentences:
        skip_next = False
        for word in sent.words:
            lemma = word.lemma
            feats = word.feats or ""
            upos = word.upos
            if upos in {"NOUN", "VERB", "ADJ", "ADV"} and random.random() < 0.5 and not skip_next:
                skip_next = True

                synonym = get_synonym(lemma, feats, upos)
                new_tokens.append(synonym)
                time.sleep(2)
                continue
            elif upos in {"NOUN", "VERB", "ADJ", "ADV"}:
                skip_next=False
            new_tokens.append(word.text)
    return " ".join(new_tokens)

def make_synonym_pair(original):
    modified = synonymize(original)

    if random.random() < 0.5:
        return {"text1": original, "text2": modified}

    return {"text1": modified, "text2": original}