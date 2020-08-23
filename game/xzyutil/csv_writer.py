import csv

class csv_writer:
    the_writer = 0
    the_file = 0
    def __init__(self,filename,deli = ','):
        self.the_file = open(filename,'w')
        self.the_writer = csv.writer(self.the_file,dialect='unix',delimiter = deli)
    def do_it(self,line):
        (self.the_writer).writerow(line)
    def close(self):
        (self.the_file).close()
