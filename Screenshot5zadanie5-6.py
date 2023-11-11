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