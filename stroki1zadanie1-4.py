#задание 1
def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
        return 'Мимо!'
print(search_substr('Кол', 'шкОла'))
#задание 2 
def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last
print(first_last('a', 'abba'))
#задание 3
from collections import Counter
def top3(st):
    counter_top3 = Counter(st.replace(' ', '')).most_common(3)
    return ', '.join([f'{letter} - {cnt}' for letter, cnt in counter_top3])
print(top3('Голова думала'))
#задание 4
def camel(st):
    new_st = ''
    letter_counter = 0
    for index, val in enumerate(st):
        if val.isalpha():
            if letter_counter % 2 == 0:
                new_st += val.upper()
            else:
                new_st += val.lower()
            letter_counter += 1
        else:
            new_st += val
    return new_st
print(camel('Утром!! было! солнечно!'))
