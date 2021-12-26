def f2():
    print("f2 시작")
    print("f2 끝")

def f1():
    print("f1 시작")
    f2()
    print("f1 끝")

print("main 시작")
f1()
print("main 끝")