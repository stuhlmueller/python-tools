from pytools import run_async

def print_new(store):
    out = store.read_new().strip()
    if out:
        print out

run_async("./async.sh",
          handler=print_new)
