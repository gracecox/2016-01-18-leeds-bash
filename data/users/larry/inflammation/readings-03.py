import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    for filename in sys.argv[2:]:
        data = numpy.loadtxt(filename, delimiter=',')
        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)

        for m in values:
            print(m)

main()
