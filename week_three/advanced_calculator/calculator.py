from token import tokenizer

def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int:
    try:
        return x / y
    except Exception as e:
        print(f"Unable to divide by zero! Full exception: {e}")


class MyIndex():
    def __init__(self, tok: list):
        self.index = 0
        self.tokens = tok
        self.cur_tok = self.tokens[0]

    def next_token(self):
        self.index += 1

        if self.index < len(self.tokens):
            self.cur_tok = self.tokens[self.index]


def split_input(user_input: str) -> list:
    ret_list = []
    lnum_string = ""
    rnum_string = ""
    rnum_index = 0

    for i in range(0, len(user_input)):
        if user_input[i] != " ":
            lnum_string += user_input[i]
        else:
            rnum_index = i + 1
            break

    for i in range(rnum_index, len(user_input)):
        rnum_string += user_input[i]

    ret_list.append(int(lnum_string))
    ret_list.append(int(rnum_string))

    return ret_list


def num(my_ind: MyIndex):
    if my_ind.cur_tok["type"] == "int":
        num = my_ind.cur_tok
        my_ind.next_token()
        return num


def mul_div(my_ind: MyIndex):
    node = num(my_ind)

    while my_ind.cur_tok["type"] in ("mul", "div"):
        tok = my_ind.cur_tok
        my_ind.next_token()
        node = {"left": node, "op": tok, "right": num(my_ind)}

    return node


def add_sub(my_ind: MyIndex):
    node = mul_div(my_ind)

    while my_ind.cur_tok["type"] in ("add", "sub"):
        tok = my_ind.cur_tok
        my_ind.next_token()
        node = {"left": node, "op": tok, "right": mul_div(my_ind)}

    return node

def tree(my_ind: MyIndex):
    tree = add_sub(my_ind)
    return tree


def visit(node):
    print(f"calling visit() on {node}")
    if "type" in node:
        return node["value"]
    else:
        return visit_op(node)
    

def visit_op(node: dict):
    print(f"calling visit_op() on {node}")
    if node["op"]["type"] == "add":
        return visit(node["left"]) + visit(node["right"])
    elif node["op"]["type"] == "sub":
        return visit(node["left"]) - visit(node["right"])
    elif node["op"]["type"] == "mul":
        return visit(node["left"]) * visit(node["right"])
    elif node["op"]["type"] == "div":
        return visit(node["left"]) / visit(node["right"])  
    

def main():
    tok_list = tokenizer("5 + 8 * 22 - 16 * 24")
    print(tok_list)
    my_ind = MyIndex(tok_list)
    ast = tree(my_ind)
    print(ast)
    solution = visit_op(ast)
    print(f"The solution is: {solution}")


if __name__ == '__main__':
    main()
#    while True:
        # First show separate number inputs
        # print("Enter the first number")
        # n1 = input()
        # print("Enter the second number")
        # n2 = input()
        # print("Please enter two numbers separated by a space (ex. '3 5')")
        # # num = input().split(" ")
        # num_str = input()
        # num_list = split_input(num_str)
        # print("Please choose the operation, [a]dd, [s]ubtract, [m]ultiply, [d]ivide")
        # c = input()
 
        # match c:
        #     case "a":
        #         # print(f"Sum is: {add(int(n1), int(n2))}. Perform another operation? [y/n]")
        #         # print(f"Sum is: {add(int(num[0]), int(num[1]))}. Perform another operation? [y/n]")
        #         print(f"Sum is: {add(num_list[0], num_list[1])}. Perform another operation? [y/n]")
        #         con = input()
        #     case "s":
        #         # print(f"Difference is: {subtract(int(n1), int(n2))}. Perform another operation? [y/n]")
        #         # print(f"Difference is: {subtract(int(num[0]), int(num[1]))}. Perform another operation? [y/n]")
        #         print(f"Difference is: {subtract(num_list[0], num_list[1])}. Perform another operation? [y/n]")
        #         con = input()
        #     case "m":
        #         # print(f"Product is: {multiply(int(n1), int(n2))}. Perform another operation? [y/n]")
        #         # print(f"Difference is: {multiply(int(num[0]), int(num[1]))}. Perform another operation? [y/n]")
        #         print(f"Product is: {multiply(num_list[0], num_list[1])}. Perform another operation? [y/n]")
        #         con = input()
        #     case "d":
        #         # print(f"Quotient is: {divide(int(n1), int(n2))}. Perform another operation? [y/n]")
        #         # print(f"Difference is: {divide(int(num[0]), int(num[1]))}. Perform another operation? [y/n]")
        #         print(f"Quotient is: {divide(num_list[0], num_list[1])}. Perform another operation? [y/n]")
        #         con = input()
        #     case _:
        #         print("Invalid operation, would you like to try again? [y/n]")
        #         con = input()
 
        # if con != "y":
        #     break


# 5 + 8 * 10 - 2
            