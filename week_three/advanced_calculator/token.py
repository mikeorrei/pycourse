def get_int(inp: str, ind: int):
    ret_str = ""
    for i in range(ind, len(inp)):
        if inp[i].isdigit():
            ret_str = ret_str + inp[i]
            ret_i = i
        else:
            break

    return int(ret_str), ret_i


def token_type(tok):
    if type(tok) is int:
        return "int"
    elif tok == "+":
        return "add"
    elif tok == "-":
        return "sub"
    elif tok == "*":
        return "mul"
    elif tok == "/":
        return "div"


def tokenizer(inp: str) -> list:
    i = 0
    ret_list = []
    while i < len(inp):
        if inp[i].isdigit():
            tok, ind = get_int(inp, i)
            i = ind + 1
            tok_type = token_type(tok)
            ret_list.append({"type": tok_type, "value": tok})

        elif inp[i] != " ":
            # ret_list.append(input[i])
            tok_type = token_type(inp[i])
            ret_list.append({"type": tok_type, "value": inp[i]})
            i += 1
        else:
            i += 1

    return ret_list

