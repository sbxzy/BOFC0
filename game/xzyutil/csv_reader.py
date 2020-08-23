import csv
from numpy import array,vstack

class csv_reader:
    the_reader = 0
    count = 0
    
    def __init__(self,filename,has_header = False,deli = ','):
        self.the_reader = csv.reader(open(filename,'r'),delimiter = deli)
        if has_header:
            self.the_reader.next()
            
    #the following methods can only be correct the first time called, due to you know what iteration reasons
    def get_block(self,block_size):
        block = array([])
        for i in range(block_size):
            tmp = self.the_reader.next()
            if len(block) == 0:
                block = array(tmp,dtype = 'float')
            else:
                block = vstack(block,array(tmp,dtype = 'float'))
        return block

    def get_all(self):
        block_all = []
        for line in self.the_reader:
            block_all.append(array(line,'float'))
        return block_all

    def separate_label(self):
        block_all = []
        label_all = []
        for line in self.the_reader:
            label_all.append(float(line[-1]))
            line.pop()
            block_all.append(array(line,'float'))
        return block_all,label_all

    def down_sample_all(self,rate):
        block_all = []
        i = 0
        if rate < 1:
            leave_rate = int(round((1-rate)*10))
            for line in self.the_reader:
                if i % 10 >= leave_rate:
                    block_all.append(array(line,'float'))
                i += 1
        else:         
            for line in self.the_reader:
                if i % rate == 0:
                    block_all.append(array(line,'float'))
                i += 1
        return block_all

    def down_sample_seperate(self,rate):
        block_all = []
        label_all = []
        i = 0
        if rate < 1:
            leave_rate = int(round((1-rate)*10))
            for line in self.the_reader:
                if i % 10 >= leave_rate:
                    label_all.append(float(line[-1]))
                    line.pop()
                    block_all.append(array(line,'float'))
                i += 1
        else:
            for line in self.the_reader:
                if i % rate == 0:
                    label_all.append(float(line[-1]))
                    line.pop()
                    block_all.append(array(line,'float'))
                i += 1
        return block_all,label_all
    
    def to_blocks(self,block_size):
        block_formation = []
        current = 0
        block = array([])
        for line in self.the_reader:
            if len(block)==0:
                block = array(line,dtype = 'float')
            else:
##                print block.shape,array(line,dtype = 'float').shape
##                print current
                block = vstack((block,array(line,dtype = 'float')))
            current += 1
            if current % block_size == 0:
                block_formation.append(block)
                block = array([])
        return block_formation
