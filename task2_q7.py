
def Max_leng_str(s1, s2):
    if len(s1) == len(s2):
        print("The both strings have equal length")
        print(s1,"\n", s2)
    else:
        print("The longer string is:")
        print(s1 if len(s1) > len(s2) else s2)

 
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
Max_leng_str(s1, s2)