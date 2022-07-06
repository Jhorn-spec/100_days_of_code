def clear():
    import os
    clear = lambda: os.system('clear')
    clear()

def time():
    import os
    systime = lambda: os.system('uptime')
    systime()

time()