# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

####
# NEED to get better examples here, since it is important for exam!!

def func1():
    a = 1
    print(a)

def func2():
    b = 2
    print(b)

func1()
func2()
