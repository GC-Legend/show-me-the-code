#! ./venv/bin/python
# coding=utf-8

def get_activation_code(s,n):
    from random import choice

    set_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'


    result = set()
    while len(result)<s:
        while True:
            activation_code = ''
            for i in range(n):
                activation_code += choice(set_str)
            if activation_code not in result:
                result.add(activation_code)
                break
    return result


if __name__ == '__main__':
    result = get_activation_code(200,10)
    for i in result:
        print(i)
