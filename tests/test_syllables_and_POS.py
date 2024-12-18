from syllables_and_POS import get_syllables
from syllables_and_POS import get_POS

def test_get_syllables():
    word_list = [
    "адреса", "азбест", "андрій", "бастіон", "батальйон", "вразливий", 
    "бойкот", "бомбардувальник", "вертлявий", "верхів'я", "ніччю", 
    "сестра", "підживити", "абстрактний", "кобзар", "дубки", "казки", 
    "віднести", "земля", "звістка", "кожний", "ніздрі", "вістря", "листок", 
    "поясни", "поїзди", "майструвати", "ластівка", "каструля", "краплини", 
    "кішка", "місто", "гострий", "рідний", "ганна", "пшениця", "молочний", 
    "соняшник", "висотний", "студентство", "входити", "рибалка", "заступник", 
    "подвір'я", "хатинка", "здивування", "надривати", "незалежність", 
    "перев'язка", "узлісся", "цілеспрямованість", "вистава", "переможець", 
    "захоплення", "перекотиполе", "витривалий", "вишня", "вільний", "галузка", 
    "надходження", "нести", "хитрий", "підзвітність", "пристрасть", "віддзеркалення", 
    "агентство", "австралія", "діждатися", "торбинка", "бур'ян", "явір", 
    "єрофєєв", "клюють"
]

    expected_result = [
    "а-дре-са", "а-збест", "ан-дрій", "ба-сті-он", "ба-таль-йон", "вра-зли-вий", 
    "бой-кот", "бом-бар-ду-валь-ник", "вер-тля-вий", "вер-хів'-я", "ні-ччю", 
    "се-стра", "пі-джи-ви-ти", "аб-стра-ктний", "ко-бзар", "дуб-ки", "каз-ки", 
    "ві-дне-сти", "зем-ля", "зві-стка", "ко-жний", "ні-здрі", "ві-стря", "ли-сток", 
    "по-я-сни", "по-ї-зди", "май-стру-ва-ти", "ла-стів-ка", "ка-стру-ля", "кра-пли-ни", 
    "кі-шка", "мі-сто", "го-стрий", "рі-дний", "га-нна", "пше-ни-ця", "мо-ло-чний", 
    "со-ня-шник", "ви-со-тний", "сту-ден-тство", "вхо-ди-ти", "ри-бал-ка", "за-сту-пник", 
    "по-двір'-я", "ха-тин-ка", "зди-ву-ва-ння", "на-дри-ва-ти", "не-за-ле-жність", 
    "пе-рев'-яз-ка", "у-злі-сся", "ці-ле-спря-мо-ва-ність", "ви-ста-ва", "пе-ре-мо-жець", 
    "за-хо-пле-ння", "пе-ре-ко-ти-по-ле", "ви-три-ва-лий", "ви-шня", "віль-ний", "га-луз-ка", 
    "над-хо-дже-ння", "не-сти", "хи-трий", "пі-дзві-тність", "при-страсть", "ві-ддзер-ка-ле-ння", 
    "а-ген-тство", "ав-стра-лі-я", "ді-жда-ти-ся", "тор-бин-ка", "бур'-ян", "я-вір", 
    "є-ро-фє-єв", "клю-ють"
]

    actual_result = []

    for word in word_list:
        actual_result.append(get_syllables(word))

    assert actual_result == expected_result

def test_POS():
    word_list = [
    "адреса", "азбест", "андрій", "бастіон", "батальйон", "вразливий", 
    "бойкот", "бомбардувальник", "вертлявий", "верхів'я", "ніччю", 
    "сестра", "підживити", "абстрактний", "кобзар", "дубки", "казки", 
    "віднести", "земля", "звістка", "кожний", "ніздрі", "вістря", "листок", 
    "поясни", "поїзди", "майструвати", "ластівка", "каструля", "краплини", 
    "кішка", "місто", "гострий", "рідний", "ганна", "пшениця", "молочний", 
    "соняшник", "висотний", "студентство", "входити", "рибалка", "заступник", 
    "подвір'я", "хатинка", "здивування", "надривати", "незалежність", 
    "перев'язка", "узлісся", "цілеспрямованість", "вистава", "переможець", 
    "захоплення", "перекотиполе", "витривалий", "вишня", "вільний", "галузка", 
    "надходження", "нести", "хитрий", "підзвітність", "пристрасть", "віддзеркалення", 
    "агентство", "австралія", "діждатися", "торбинка", "бур'ян", "явір", 
    "єрофєєв", "клюють"
]

    expected_result = [
    'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Прикметник', 'Іменник',
    'Іменник', 'Прикметник', 'Іменник', 'Іменник', 'Іменник', 'Дієслово', 'Прикметник',
    'Іменник', 'Іменник', 'Іменник', 'Дієслово', 'Іменник', 'Іменник', 'Іменниковий займенник',
    'Іменник', 'Іменник', 'Іменник', 'Дієслово', 'Іменник', 'Дієслово', 'Іменник', 'Іменник',
    'Іменник', 'Іменник', 'Іменник', 'Прикметник', 'Прикметник', 'Іменник', 'Іменник', 'Прикметник',
    'Іменник', 'Прикметник', 'Іменник', 'Дієслово', 'Іменник', 'Іменник', 'Іменник', 'Іменник',
    'Іменник', 'Дієслово', 'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Іменник',
    'Іменник', 'Прикметник', 'Іменник', 'Прикметник', 'Іменник', 'Іменник', 'Дієслово', 'Прикметник',
    'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Іменник', 'Дієслово', 'Іменник', 'Іменник', 'Іменник',
    'Іменник', 'Дієслово'
]

    actual_result = []

    for word in word_list:
        actual_result.append(get_POS(word))

    assert actual_result == expected_result