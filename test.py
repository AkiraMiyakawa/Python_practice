import datetime

def test():
    print("test")
def test1(a):
    print(a)
def sum(a,b):
    result = a + b
    return result
def test2(aaa):
    result = None
    if aaa >= 5:
        result = True
    else:
        result = False
    return result

result = test2(6)
print(result)

now = datetime.datetime.now()
print(now)

# lst = [1,2,3,4,100,"egg"]

# for i in lst:
#     if i == 100:
#         print("test")
#         print(i)
#     print("AAAAAAA")

# test1("-----------")

# displayResult = sum(1,4)
# print(displayResult)

