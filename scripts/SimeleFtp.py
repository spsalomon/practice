import sys

def greeting():
    print("Hello world!")

def main():
    greeting()


if __name__ == '__main__':
    print("Version: {}".format(sys.version))
    main()

