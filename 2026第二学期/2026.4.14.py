class PrintQueue:
    def __init__(self):
        self.job = []
    def add_job(self,job):
        self.job.append(job)
        print(f'Add job:{job}')
    def print_job(self):
        if len(self.job) != 0 :
            next_job = self.job.pop(0)
            print(f'print job:{next_job}')
        else:
            print('None')
    def show_job(self):
        if len(self.job) != 0 : 
            print(f'Waiting job:{self.job}')
        else:
            print('No job in queue')
def test():
    pq = PrintQueue()
    pq.add_job('report.pdf')
    pq.add_job('photo.png')
    pq.add_job('notes.doex')
    pq.print_job()
    pq.show_job()
test()