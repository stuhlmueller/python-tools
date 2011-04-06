#!/usr/bin/python

import os
import signal
import time
from pytools.external.asyncproc import Process
from pytools.datastructures.string import IncStringIO
from threading import Thread, Lock, Event
from datetime import datetime


__all__ = ['AsyncThread', 'run_async', 'make_async_thread']


class StoppableThread(Thread):
    """
    Thread class with a stop() method. The thread itself has to check
    regularly for the stopped() condition.
    """

    def __init__(self):
        super(StoppableThread, self).__init__()
        self._stop = Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    
class AsyncThread(StoppableThread):
    """
    Thread class that encapsulates an asynchronous procedure and an
    incremental string file object.
    """

    def __init__(self, proc, store):
        super(AsyncThread, self).__init__()
        self.proc = proc
        self.store = store

    def run(self, graceperiod=.1):
        while True:
            if self.stopped():
                os.kill(self.proc.pid(), signal.SIGTERM)
                time.sleep(graceperiod)
                os.kill(self.proc.pid(), signal.SIGKILL)
                break
            poll = self.proc.wait(os.WNOHANG)
            if poll != None:
                break
            out = self.proc.read()
            if out != "":
                self.store.write(out)

                
def make_async_thread(cmd):
    proc = Process(cmd)
    store = IncStringIO()
    return AsyncThread(proc, store)


def run_async(cmd, timeout=None, handler=None):
    thread = make_async_thread(cmd)
    thread.start()
    t0 = datetime.now()
    runtime = 0
    while thread.is_alive() and not (timeout and (runtime > timeout)):
        if handler:
            handler(thread.store)
        runtime = (datetime.now() - t0).seconds
    thread.stop()
    thread.join()
    return (runtime, thread.store)
