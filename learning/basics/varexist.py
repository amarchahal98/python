import sys

def function(parameter):
    parameter = int(parameter)
    if (parameter) < 5:
        print("lower")
    if (parameter) == 5:
        print("exact")
    if (parameter) > 5:
        print("higher")


def main(argv):

    inval = True
    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            function(line.strip())
        inval = False
        
    if len(argv) >= 1:
        for arg in argv:
            try:
                function(arg)
            except ValueError:
                print("value is empty")

            inval = False
    if inval:
        print('Usage: python3.5 varexist.py [domain_name]')
        print('Usage: cat [input file] | python varexist.py')

if __name__== '__main__':
    main(sys.argv[1:])
