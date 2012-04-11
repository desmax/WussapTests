import sys
try:
    total = 0
    input = sys.stdin.readlines()
    for line in input:
        if line.strip():
            total += float(line)
    print 'Total:' + str(total)
except KeyboardInterrupt:
    print 'KeyboardInterupt'
except Exception:
    print 'Something went wrong'