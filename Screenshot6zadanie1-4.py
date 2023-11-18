#задание 1
def to_dict(lst):
    return {element: element for element in lst}
print(to_dict([12, 21, 45, 52]))
#задание 2
my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
biggest_dict(k1=56, k2=53, k3=11, k4=91)
biggest_dict(name='Боря', age=34, weight=174, eyes_color='Черные')
print(my_dict)
#задание 3
def count_it(sequence):
    num_frequency = {int(item): sequence.count(item) for item in sequence}
    sorted_num_frequency = sorted(num_frequency.items(), key=lambda element: element[1])
    return dict(sorted_num_frequency[-3:])
print(count_it('1333333333377'))
#задание 4
from collections import OrderedDict
dct = OrderedDict({1: 1, 2: 2, 3: 3, 4: 4, 5: 5})
first = list(dct.items())[0]
last = list(dct.items())[-1]
dct.move_to_end(key=first[0])
dct.move_to_end(key=last[0], last=False)
second = list(dct.items())[1]
del dct[second[0]]
dct['new_key'] = 'new_value'
my_dict
{5: 5, 3: 3, 4: 4, 1: 1, 'new_key': 'new_value'}
id(my_dict)
17128656
print(id)