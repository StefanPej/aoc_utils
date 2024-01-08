from numpy import prod

def read_input(year: str | int, day: str | int, strip: bool=True, filename: str='input') -> "list[str]":
    year = str(year)
    day = str(day).zfill(2)
    with open(f'{year}/day_{day}/{filename}.txt') as f:
        ret = f.readlines()
    return [line.strip() for line in ret] if strip else ret

def transpose(my_list: list) -> list:
    return list(zip(*my_list))

def order_dict(my_dict: dict, reverse: bool=False) -> dict:
    return {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=reverse)}

def order_list(my_list: list, order_val: int, reverse: bool=False) -> list:
    return [item for item in sorted(my_list, key=lambda item: item[order_val], reverse=reverse)]

def apply_function_get_total(func, func_input, method: str) -> int:
    if method not in ['sum', 'mult']:
        raise ValueError('method must be "sum" or "mult"')
    vals = [func(*inp) for inp in func_input]
    return sum(vals) if method == 'sum' else prod(vals)