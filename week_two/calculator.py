def add(x: int, y: int) -> int:
    return x + y

def sub(x: int, y: int) -> int:
    return x - y

def mul(x: int, y: int) -> int:
    return x * y

def div(x: int, y: int) -> int:
    try:
        return x / y
    except:
        print("You divided by 0")


if __name__ == '__main__':
    print("Enter two numbers separated by a space")
    nums = input()
    print("enter the operation")
    op = input()

    match op:
        case "a":
            print(add(int(nums.split(" ")[0]), int(nums.split(" ")[1])))
        case "s":
            print(sub(nums.split(" ")[0], nums.split(" ")[1]))
        case "m":
            print(mul(nums.split(" ")[0], nums.split(" ")[1]))
        case "d":
            print(div(nums.split(" ")[0], nums.split(" ")[1]))



