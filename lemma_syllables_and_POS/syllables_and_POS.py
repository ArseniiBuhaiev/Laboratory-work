import pymorphy3
import re

morph = pymorphy3.MorphAnalyzer(lang='uk')

POS_map = {
    'NOUN': ', Іменник',
    'ADJF': ', Прикметник',
    'ADJS': ', Прикметник',
    'COMP': ', Компаратив',
    'VERB': ', Дієслово',
    'INFN': ', Дієслово',
    'PRTF': ', Дієприкметник',
    'PRTS': ', Дієприкметник',
    'GRND': ', Дієприслівник',
    'NUMR': ', Числівник',
    'ADVB': ', Прислівник',
    'NPRO': ', Іменниковий займенник',
    'PRED': ', Предикатив',
    'PREP': ', Прийменник',
    'CONJ': ', Сполучник',
    'PRCL': ', Частка',
    'INTJ': ', Вигук',
    None: ''
}

def get_POS(word: str) -> str:
    p = morph.parse(word)[0]
    POS = p.tag.POS

    return POS_map[POS]

def get_syllables(word: str) -> str:

    word = (word.casefold()).strip()

    vowels = {
        "у", "е", "ї", "і", "а",
        "о", "є", "я", "и", "ю"
    }
    consonants = {
        "й", "ц", "к", "н", "г",
        "ґ", "ш", "щ", "з", "х",
        "ф", "в", "п", "р", "л",
        "д", "ж", "ч", "с", "м",
        "т", "б", "ь"
    }
    voiced = {
        "г", "ґ", "з", "д", "ж", "б"
    }
    unvoiced = {
        "ц", "к", "ш", "щ", "ф",
        "п", "ч", "с", "т", "х",
    }
    sonorant = {
        "й", "н", "в", "р", "л", "м",
    }

    current_syllable = ""
    syllables_list = []
     

    if len(word) < 3:
        return word
    else:
        for i, ch in enumerate(word):

            is_apstrph = ch == "'"

            cnsnnt_btwn_vwls = ch in vowels \
                and i != len(word) - 1 \
                and i != len(word) - 2 \
                and word[i+1] in consonants \
                and word[i+2] in vowels 
                
            two_nsd_cnsnnt = i != len(word) - 1 \
                and i != len(word) - 2 \
                and word[i+1] in voiced \
                and word[i+2] in voiced \
                or i != len(word) - 1 \
                and i != len(word) - 2 \
                and word[i+1] in unvoiced \
                and word[i+2] in unvoiced

            two_vcd_or_two_unvcd_and_snrnt = i != len(word) - 1 \
                and i != len(word) - 2 \
                and i != len(word) - 3 \
                and word[i+1] in voiced \
                and word[i+2] in voiced \
                and word [i+3] in sonorant \
                or i != len(word) - 1 \
                and i != len(word) - 2 \
                and i != len(word) - 3 \
                and word[i+1] in unvoiced \
                and word[i+2] in unvoiced \
                and word [i+3] in sonorant \

            is_snrnt_before_vcd_or_unvcd = i != len(word) - 1 \
                and ch in sonorant \
                and word[i+1] in voiced \
                or i != len(word) - 1 \
                and ch in sonorant \
                and word[i+1] in unvoiced

            is_vcd_next_is_unvcd = i != len(word) - 1 \
                and ch in voiced \
                and word[i+1] in unvoiced

            is_snrnt_before_not_snrnt = ch in sonorant \
                and i != len(word) - 1 \
                and word[i+1] in consonants \
                and word[i+1] not in sonorant

            two_cnsnnt_second_is_snrnt_between_vwls = ch in vowels \
                and i != len(word) - 1 \
                and i != len(word) - 2 \
                and word[i+1] in consonants \
                and word[i+1] not in sonorant \
                and word[i+2] in sonorant

            is_snrnt_before_snrnt = ch in sonorant \
                and i != len(word) - 1 \
                and word[i+1] in sonorant

            is_doubled = i != len(word) - 1 \
                and i != len(word) - 2 \
                and word[i+1] == word [i+2]
            
            two_vwls = i != len(word) - 1 \
                and ch in vowels \
                and word[i+1] in vowels
            
            last_vwl = i + 1 == len(word) - 1 \
            and word[i+1] in vowels
    
            if is_apstrph \
            or cnsnnt_btwn_vwls \
            or two_nsd_cnsnnt \
            or two_vcd_or_two_unvcd_and_snrnt \
            or is_vcd_next_is_unvcd \
            or is_snrnt_before_vcd_or_unvcd \
            or is_snrnt_before_not_snrnt \
            or two_cnsnnt_second_is_snrnt_between_vwls\
            or is_snrnt_before_snrnt\
            or is_doubled \
            or two_vwls \
            or last_vwl:
                current_syllable += ch
                if any(char in vowels for char in current_syllable):
                    syllables_list.append(current_syllable)
                    current_syllable = ""
            else:
                current_syllable += ch
    
    if current_syllable != "":
        syllables_list.append(current_syllable)

    for syl in syllables_list:
        if not any(char in vowels for char in syl):
            syllables_list[syllables_list.index(syl) - 1] += syl
            syllables_list.pop(syllables_list.index(syl))
        elif syl.startswith('ь'):
            syllables_list[syllables_list.index(syl) - 1] += "ь"
            syllables_list[syllables_list.index(syl)] = syl.replace("ь", "")

    return "-".join(syllables_list)

def get_slbls_and_POS(word: str) -> str:
    if re.findall(r"[a-zA-Z]", word):
        return "Не кириличні символи"
    elif word.isnumeric():
        POS = "Числівник"
        return f"{POS}"
    else:
        syllables = get_syllables(word)
        POS = get_POS(word)
        return f"{syllables}{POS}"