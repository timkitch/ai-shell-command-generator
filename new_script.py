import sys

def greeting(name):
    print(f"Hello there {name}")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Please enter your name: ")
    greeting(name)
