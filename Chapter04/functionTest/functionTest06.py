def answer() :
    print(42)

answer()

def run_somthing(func) :
    func()

run_somthing(answer)

print(type(run_somthing))

def add_args(arg1, arg2) :
    print(arg1 + arg2)

print(type(add_args))

def run_something_with_args(func, arg1, arg2) :
    func(arg1, arg2)

run_something_with_args(add_args, 5, 9)

def sum_args(*args) :
    return sum(args)

def run_with_positional_args(func, *args) :
    return sum_args(*args)

print(run_with_positional_args(sum_args, 1, 2, 3, 4))
