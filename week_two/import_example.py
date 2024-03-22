
print("Hello from import example file")

def import_hello():
    print("Hello from the import example function")

def deploy_lab(lab: str) -> str:
    """
    deploy_lab is a function that will deploy a 'lab' based on the string you provide

    Args:
        lab: type = string - the name of the lab you want to deploy

    Returns:
        a string containing the lab you deployed
    """
    return f"A {lab} lab has been requested"

def add_num(x: int, y: int):
    return x + y

def print1():
    print("hello from 1")

def print2():
    print1()
    print("Hello from 2")


if __name__ == '__main__':
    print1()
    print2()