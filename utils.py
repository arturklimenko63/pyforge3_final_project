import time

start = time.time()

def tic():
    return 'at %1.1f seconds' % (time.time() - start)
