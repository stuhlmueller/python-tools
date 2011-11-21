#!/usr/bin/python

import os
import signal
import time
from pytools.external.asyncproc import Process
from pytools.datastructures.string import IncStringIO
from threading import Thread, Lock, Event
from datetime import datetime


__all__ = ['AsyncThread', 'run_async']


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
    Thread class that encapsulates an asynchronous command and an
    incremental string file object.
    """

    def __init__(self, cmd):
        super(AsyncThread, self).__init__()
        self.proc = Process(cmd)
        self.out = IncStringIO()
        self.err = IncStringIO()

    def run(self, graceperiod=.1):
        while True:
            poll = self.proc.wait(os.WNOHANG)
            out = self.proc.read()
            err = self.proc.readerr()
            if out != "":
                self.out.write(out)
            if err != "":
                self.err.write(err)
            if poll != None:
                break                
            if self.stopped():
                os.kill(self.proc.pid(), signal.SIGTERM)
                time.sleep(graceperiod)
                os.kill(self.proc.pid(), signal.SIGKILL)
                break
                

def run_async(cmd, timeout=None, handler=None):
    thread = AsyncThread(cmd)
    thread.start()
    t0 = datetime.now()
    runtime = t0 - t0
    while thread.is_alive() and not (timeout and (runtime.seconds > timeout)):
        if handler:
            handler(thread.out, thread.err)
        runtime = (datetime.now() - t0)
    thread.stop()
    thread.join()
    return (runtime, thread.out, thread.err)
