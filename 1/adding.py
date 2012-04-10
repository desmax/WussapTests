total = 0
while True:
    try:
        var = raw_input()
    except (EOFError, KeyboardInterrupt):
        print 'Total:' + str(total)
        break
    else:
        if len(var):
            total += float(var)