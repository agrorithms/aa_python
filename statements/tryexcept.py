#Try...Except


a = '321'

try:
    print(len(a))
except:
    print("enter a string")


a=100
b=0

try:
    c = a/b
except ZeroDivisionError:
    c = None
    print(c)

d=100
#e=0

try:
    print(d/e)
except (NameError,TypeError) as er:
    print('error!',er)


def divide(x,y):
    try:
        result=x/y
    except ZeroDivisionError:
        print('Cannot divide by 0')
    else:
        print('result is',result)
    finally:
        print("finally")

#divide(1,'0')


a=321
if hasattr(a,'__len__'):
    print(len(a))

a='321'
if hasattr(a,'__len__'):
    print(len(a))
