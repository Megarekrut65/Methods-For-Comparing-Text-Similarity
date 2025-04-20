import stanza

stanza.download("uk")
nlp = stanza.Pipeline(lang="uk", processors="tokenize,mwt,pos,lemma,depparse")