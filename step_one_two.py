tmp_dict = {}
def step_calculator(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:<
        return 2
    if n in tmp_dict:
        return tmp_dict[n]

    ret = step_calculator(n-1) + step_calculator(n-2)
    tmp_dict[n] = ret

    return ret

def step_calculator_non_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    prepre = 2
    pre = 1
    ret = 0
    for _ in range(3, n + 1):
        ret = pre + prepre
        print('ret',ret)
        pre = prepre
        print('pre',pre)
        prepre = ret
        print('prepre',prepre)
        print('*'*10)
    return ret

step_calculator_non_recursive(6)
step_calculator(6)