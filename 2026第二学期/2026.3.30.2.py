class VoteSystem():
    def __init__ (self,options):
        self.options = options
        self.votes = [0] * 3
    def vote(self,index):
        if 1<=index<=3:
            self.votes[index-1] += 1
        else:
            print('麻溜点你投错了')
    def show_results(self):
        for op , i in zip(self.options,self.votes):
            print(f'{op}:{i}票')
    def max_vote(self):
        max_votes = max(self.votes)
        if max_votes == 0:
            print('为何没人投票')
        else:
            max_index = self.votes.index(max_votes)
            print(f'最高票数是{self.options[max_index]} : {max_votes}')
def test():
    sys = VoteSystem(['A','B','C'])
    while True:
        choice = int(input())
        if choice == 0 : 
            break
        elif choice in [ 1,2,3,]:
            sys.vote(choice)
        else:
            print('不是哥你还能投错？')
    print('投票结束，结果是：')
    sys.show_results()
    sys.max_vote()
test()



