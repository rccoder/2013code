def f1():
    print "I am a function!"
def do_n(fun, n):
    while n > 0:
        fun()
        n -= 1
func = input("Input the function name: ")
times = eval(raw_input("Please input n: "))
do_n(func, times)
