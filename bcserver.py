from subprocess import Popen, STDOUT, PIPE
from threading import Thread

class ProcessOutputThread(Thread):
    def __init__(self,p):
        super().__init__() #initialize Parent Class's (Thread) constructor
        self.p = p

    def run(self):
        for line in self.p.stdout:
            print(line.decode(), end='')

p = Popen(['bc'],stdin=PIPE,stdout=PIPE,stderr=STDOUT)
out_t = ProcessOutputThread(p)
out_t.start()

#Keep looping while the child process is still running
while p.poll() is None: 
    try:
        inp = input('')
        inp = inp + "\n"
        p.stdin.write(inp.encode())
        p.stdin.flush()
    except KeyboardInterrupt :
        break