import pymorphy3
import re

morph = pymorphy3.MorphAnalyzer(lang='uk')

def get_lemma(word: str) -> str:
    if re.findall(r"[a-zA-Z]", word):
        return 'Некириличні символи'
    else:
        p = morph.parse(word)[0]
        lemma = p.normal_form
        return lemma