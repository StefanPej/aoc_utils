def read_input(year: str | int, day: str | int, strip: bool=True) -> "list[str]":
    year = str(year)
    day = str(day).zfill(2)
    with open(f'{year}/day_{day}/input.txt') as f:
        ret = f.readlines()
    return [line.strip() for line in ret] if strip else ret

def transpose(my_list: list) -> list:
    return list(zip(*my_list))

def order_dict(my_dict: dict, reverse: bool=True) -> dict:
    return {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=reverse)}

def order_list(my_list: list, order_val: int, reverse: bool=True) -> list:
    return [item for item in sorted(my_list, key=lambda item: item[order_val], reverse=reverse)]

def apply_function_get_total(func, func_input, method: str) -> int:
    if method not in ['add', 'mult']:
        raise ValueError('method must be "add" or "mult"')
    
    if method == 'add':
        total = 0
    elif method == 'mult':
        total = 1
    
    for inp in func_input:
        temp_res = func(inp)
        if method == 'add':
            total += temp_res
        elif method == 'mult':
            total *= temp_res
    
    return total