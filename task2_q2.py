
def Upper_lower_string(String):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in String:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", String)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

Upper_lower_string('abcSdefPghijQkl')