# F = 10110000

# return F
def func_f():
    if x == 0 and y == 0 and z == 0:
        return 1
    if x == 0 and y == 0 and z == 1:
        return 0
    if x == 0 and y == 1 and z == 0:
        return 1
    if x == 0 and y == 1 and z == 1:
        return 1
    if x == 1 and y == 0 and z == 0:
        return 0
    if x == 1 and y == 0 and z == 1:
        return 0
    if x == 1 and y == 1 and z == 0:
        return 0
    if x == 1 and y == 1 and z == 1:
        return 0


# Zhegalkin polynomial
def linear():
    global a0, a2, a3, a1, a12, a23, a13, a123
    af = func_f()
    if x == 0 and y == 0 and z == 0:
        a0 = af
        return a0
    if x == 0 and y == 0 and z == 1:
        a3 = a0 ^ af
        return a3
    if x == 0 and y == 1 and z == 0:
        a2 = af ^ a0
        return a2
    if x == 0 and y == 1 and z == 1:
        a23 = af ^ a2 ^ a3 ^ a0
        return a23
    if x == 1 and y == 0 and z == 0:
        a1 = af ^ a0
        return a1
    if x == 1 and y == 0 and z == 1:
        a13 = af ^ a1 ^ a3 ^ a0
        return a13
    if x == 1 and y == 1 and z == 0:
        a12 = af ^ a1 ^ a2 ^ a0
        return a12
    if x == 1 and y == 1 and z == 1:
        a123 = af ^ a12 ^ a13 ^ a23 ^ a1 ^ a2 ^ a3 ^ a0
        return a123


# check for linear by Zhegalkin polynomial
def is_linear():
    if a12 == 0 and a13 == 0 and a23 == 0 and a123 == 0:
        return "Функція лінійна"
    else:
        return "Функція нелінійна"


def saves_0_const():
    af = func_f()
    if x == 0 and y == 0 and z == 0 and (af == 0):
        return 1
    if x == 0 and y == 0 and z == 0 and (af == 1):
        return 0


def saves_1_const():
    af = func_f()
    if x == 1 and y == 1 and z == 1 and (af == 1):
        return 1
    if x == 1 and y == 1 and z == 1 and (af == 0):
        return 0


def ddnf():
    if func_f() == 1:
        if x == 0:
            p_x = "x'"
        elif x == 1:
            p_x = "x"
        if y == 0:
            p_y = "y'"
        elif y == 1:
            p_y = "y"
        if z == 0:
            p_z = "z'"
        elif z == 1:
            p_z = "z"
        logic = (p_x + p_y + p_z)
        return logic


def dknf():
    if func_f() == 0:
        if x == 0:
            p_x = "x"
        elif x == 1:
            p_x = "x'"
        if y == 0:
            p_y = "y"
        elif y == 1:
            p_y = "y'"
        if z == 0:
            p_z = "z"
        elif z == 1:
            p_z = "z'"
        logic = ("(" + p_x + "\/" + p_y + "\/" + p_z + ")")
        return logic


ddnf_array_e = []
dknf_array_e = []
linear_array = []
f_arr = []
print("x y z  F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            # print truth table
            print(x, y, z, "", func_f())
            if saves_0_const() == 1:
                saves_0 = "Функція зберігає константу 0"
            if saves_0_const() == 0:
                saves_0 = "Функція не зберігає константу 0"
            if saves_1_const() == 1:
                saves_1 = "Функція зберігає константу 1"
            if saves_1_const() == 0:
                saves_1 = "Функція не зберігає константу 1"
            if ddnf() != None:
                ddnf_array_e.append(ddnf())
                ddnf_array_e.append("\/")
            if dknf() != None:
                dknf_array_e.append(dknf())
                dknf_array_e.append("/\\")
            f_arr.append(str(func_f()))
            linear_array.append(linear())


def inverse():
    f = ''.join(f_arr)
    f = list(f)
    for i in range(len(f)):
        f[i] = '1' if f[i] == '0' else '0'
    return ''.join(f)


def is_self_dual():
    f = ''.join(f_arr)
    if f == ''.join(reversed(inverse())):
        return "Функція самодвоїста"
    else:
        return "Функція не самодвоїста"


# optional check for linear
# print("Поліном Жегалкіна: ", "a0:", a0, "a1:", a1, "a2:", a2, "a3:", a3, "a12:", a12, "a13:", a13,"a23:", a23, "a123:", a123)

# Function characteristics output
def output():
    print("1.", saves_0)
    print("2.", saves_1)
    print("3.", is_self_dual())
    print("4.", is_linear())
    if len(ddnf_array_e) != 0:
        ddnf_array_e.pop()
    if len(dknf_array_e) != 0:
        dknf_array_e.pop()
    print("5.", "ДДНФ:", *ddnf_array_e)
    print("6.", "ДКНФ:", *dknf_array_e)


output()
