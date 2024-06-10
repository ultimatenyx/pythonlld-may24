# def bingo(fn):
#     def whatever():
#         print("Before")
#         fn()
#         print("After")
#
#     return whatever
#
# @bingo
# def say_hello():
#     print('Hello World!')
#
#
# say_hello()

def bingo(fn):
    print("Setup")
    def whatever(*args,**kwargs):
        print("Before")
        fn(*args,**kwargs)
        print("After")

    return whatever

@bingo
def say_hello(a,b):
    print(a,b)
    print('Hello World!')


say_hello(10,20)
say_hello(10,20)
say_hello(10,20)