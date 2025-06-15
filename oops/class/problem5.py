import random

class Train:

    def __init__(self,trainNo):
        self.trainNo = trainNo

    def book(self, board,to):
        print(f"your ticket is booked from {board} to {to}")
    def getStatus(self):
        print(f"the train {self.trainNo} is on time")
    def getFare(self,board,to):
        print(f"the fare for {board} to {to} is {random.randint(200,2000)}")

t = Train("12490")
t.book("Vadodara","Delhi")
t.getStatus()
t.getFare("Vadodara", "Delhi")