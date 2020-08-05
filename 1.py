class Time:
    def __init__(self,hour,minute):
        self.hour = hour
        self.minute = minute
        self.timing = hour*60+minute

class Block:
    def __init__(self,name,duration,form,start_timing=0,restrainstart=False):
        self.name = name
        self.duration = duration
        self.form = form
        self.restrainstart = restrainstart
        self.start_timing = start_timing
        self.end_timing = 0

class Day:
    def __init__(self,time):
        self.time = time
        self.starting_timing = time.timing
        self.blocklist = []

    def blockappend(self,block):
        self.blocklist.append(block)
        return self

    def create_schedule(self):
        t = self.starting_timing
        for block in self.blocklist:
            if block.restrainstart == True:
                pass
            else:
                block.start_timing = t
            block.end_timing = block.start_timing + block.duration
            print(block.name,block.start_timing,block.end_timing)
            t = block.end_timing

def main(block):
    if block.form == 'a':
        block.duration = block.duration-10
    return block

d = Day(Time(7,10))
b1 = Block('learn',40,'a')
b2 = Block('game',30,'b')
d = d.blockappend(b1).blockappend(b2)
d.create_schedule()