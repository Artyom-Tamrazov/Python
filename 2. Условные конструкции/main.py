"""
    if <условие>:
        <операторы>
    elif <условие>:
        <операторы>
    else:
        <операторы>
    В условии обычно используются логические операторы:
    >  <  >=  <=  !=  ==
    Также, для объединения условных выражений
    испоьзуются логические операции:
    and  or  not
"""

# x, y = list(map(int, input().split()))
x = int(input('x: '))
y = int(input('y: '))

if x > 0 and y > 0:
    print('I')
elif x < 0 and y > 0:
    print('II')
elif x < 0 and y < 0:
    print('III')
elif x > 0 and y < 0:
    print('IV')
else:
    print("На оси")
