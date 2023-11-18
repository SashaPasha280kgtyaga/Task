#задание 1
def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st
print(shortener('Падал(лишнее (лишнее) лишнее) прошлогодний снег (лишнее)'))
#задание 2
def cleaned_str(st):
    clean_lst = []
    for symbol in st:
        if symbol == '@' and clean_lst:
            clean_lst.pop()
        elif symbol != '@':
            clean_lst.append(symbol)
    return ''.join(clean_lst)
print(cleaned_str('гр@оо@лк@оц@ва'))
