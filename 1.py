import pandas
import numpy
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

    def __len__(self):
        return len(self.blocklist)

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

def main(firstday,finishday,step):
    ind = [i for i in range(len(firstday))]
    col = ['day'+str(j) for j in range(step+1)]
    df = pandas.DataFrame(index=ind,columns=col)
    df['day0'] = firstday.blocklist
    df['day'+str(step)] = finishday.blocklist
    print(df)

'''
    for i in range(len(firstday)):
        steplen = 0
        steplen = (finishday.blocklist[i].start_timing - firstday.blocklist[i].start_timing)/step
        df[i]
'''


d1 = Day(Time(7,10))
b1 = Block('learn',40,'a')
b2 = Block('game',30,'b')
d1 = d1.blockappend(b1).blockappend(b2)

d2 = Day(Time(7,10))
b3 = Block('learn',30,'a')
b4 = Block('game',20,'b')
d2 = d2.blockappend(b3).blockappend(b4)
main(d1,d2,5)