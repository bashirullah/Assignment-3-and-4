'''
def is_even_num(l):
    List = []
    for n in l:
        if n % 2 == 0:
            List.append(n)
    return List
print("Even numbers are :",is_even_num(range(1,21)))
'''

def evenfunc(num):
    if num%2 == 0:
        return True
print (list(filter(evenfunc, range(1,21))))