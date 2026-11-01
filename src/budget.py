class TokenBudget:
    def __init__(self,limit:int):
        self.limit=limit
        self.used=0
    def spend(self,tokens:int):
        if self.used+tokens> self.limit:
            raise ValueError("Budget exceed")
        else:
            self.used+=tokens
    def remaining(self)-> int:
        return self.limit-self.used

if __name__=="__main__":  
    budget=TokenBudget(1000)
    budget.spend(300)
    budget.spend(500)
    print(budget.remaining())
    try:
        budget.spend(300)
    except ValueError as e:
        print("Rejected:",e)               