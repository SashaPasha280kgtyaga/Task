# задание 1
my_list = [4, 8, 12]
print(my_list[::-1])
# задание 2
def change(lst):
    new_start = lst.pop() 
    new_end = lst.pop(0)
    lst.append(new_end) 
    lst.insert(0, new_start) 
    return lst

print(change([6, 8, 3, 4]))
# задание 3
def to_list(*args):
    return list(args)
print(to_list('Задание', 'номер', '3'))
# задание 4
def useless(lst):
    return max(lst) / len(lst)
print(useless([52, 2007, 1337])) 
# задание 5
def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst
print(list_sort([5, 25, 52]))
# задание 6
def all_eq(lst):
    max_length = max(len(s) for s in lst) 
    new_lst = [s.ljust(max_length, "_") for s in lst]
    return new_lst
lst = ["тинкер", "тайн","ленс"]
result = all_eq(lst)
print(result) 
