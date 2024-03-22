# import import_example
from import_example import import_hello, deploy_lab

if __name__ == '__main__':
    print("Hello from main example")
    import_hello()
    output = deploy_lab("sentinel one")
    print(output)