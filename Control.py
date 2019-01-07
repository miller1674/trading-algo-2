
import datetime 
from datetime import timedelta
from money import *
from stock import *
from tkinter import *
from graph import *
#array=["SHW", "MU", "TSLA", "JPM", "BIIB", "UFPI", "EOG", "WMT", "SBUX", "NKE","AMD", "BAC", "MSFT","TXN", "MS", "XRX", "PEP", "MKC","EIX", "MET", "NEM", "JNJ", "INTC", "T", "BBY"]
#array= ["DIS", "","EBAY", "PG", "MRO", "MS", "ABC", "TXT", "CSCO", "CF", "PLD", "DUK"] #one from each GICS sector
array=["MSFT","AAPL", "AMZN","JNJ","JPM", "GOOG", "FB", "XOM", "PFE", "UNH", "VZ", "V", "PG", "BAC"] #top 15 stocks in sp500
porfolio=[]


START_MONEY=10000
START_DATE=datetime.date(2017, 1, 2)
END_DATE=datetime.date(2017, 4, 3)
MONEY_PER_STOCK=3000

class Control:
    def __init__(self):
        self._portfolio=[]
        self._stock_list=[]
        self._money=Money(START_MONEY)
        self._curr_day=START_DATE
        self._graph=Graph()
    
    def launch(self):
        
        #currDay=datetime.date(2017, 3, 6)
        stock_list=[]
        gains_list=[]
        while (self._curr_day!=END_DATE):
            print("next day")
            
            
            print(self._curr_day)
            #if (currDay.weekday()==0):
            stock_list=[]
            for f in range(0, len(array)):
                p=Stock(array[f], self._curr_day)
                p.movingAvg(15, self._curr_day)
                #p.printStock()
                stock_list.append(p)  
            self._stock_list=stock_list   
            
            #print("b4 port")
            self.portfolio()
            self._portfolio[0].printStock()
            self._portfolio[1].printStock()
            self._portfolio[2].printStock()
            print("Current Money: "+str(self._money._curr_money))
            gains_list.append(self._money.gains(self._portfolio))
            
            stock_list.clear()
            self._curr_day=self._curr_day+timedelta(7) #moves to next week
            
        self._graph.draw_graph(gains_list)
        self._money.gains(self._portfolio)
                 
        
    def portfolio(self):
        stock=[]  #current
        stock.append(self._stock_list[0])
        stock.append(self._stock_list[0])
        stock.append(self._stock_list[0])
        
       
        
        
        
        port=[]
        for i in range(0, (len(self._stock_list))):
            if (stock[0]._moving_avg<self._stock_list[i]._moving_avg):
                stock[0]=self._stock_list[i]
        if (stock[0]==self._stock_list[0]):
            stock[1]=self._stock_list[1]
            
        for z in range(0, (len(self._stock_list))):
            if (stock[1]._moving_avg<self._stock_list[z]._moving_avg and self._stock_list[z]!=stock[0]):
                stock[1]=self._stock_list[z]
                
        if (stock[1]==self._stock_list[0] or stock[0]==self._stock_list[0]):
            for w in range(0, len(self._stock_list)):
                if (stock[0]==self._stock_list[0] and stock[1]!=self._stock_list[w] and stock[0]!=self._stock_list[w]):
                    stock[2]=self._stock_list[w]
                    w=len(self._stock_list)
                if (stock[1]==self._stock_list[0] and stock[0]!=self._stock_list[w] and stock[0]!=self._stock_list[w]):
                    stock[2]=self._stock_list[w]
                    w=len(self._stock_list)
                
        #elif(stock[0]==self._stock_list[1] and self._stock_list[0]!=self._stock_list[3]):
            #stock[2]=self._stock_list[2]
        for y in range(0, (len(self._stock_list))):
            if (stock[2]._moving_avg<self._stock_list[y]._moving_avg and self._stock_list[y]!=stock[0] and self._stock_list[y]!=stock[1]):
                stock[2]=self._stock_list[y]
        
        if (len(self._portfolio)!=0):
            
            #curr_in=False
            for t in range(0,3):
                curr_in=False
                again=""
                for r in range(0, 3):
                    if (stock[t]._symbol==self._portfolio[r]._symbol and again!=stock[t]._symbol):
                        port.append(self._portfolio[r])
                        curr_in=True
                        again=stock[t]._symbol
                        
                    
                if (curr_in==False):
                    stock[t]._number_owned=int(MONEY_PER_STOCK/stock[t]._currPrice)
                    self.buy(stock[t])
                    port.append(stock[t])
                    
            if (not self._portfolio[0] in port):  #checks if the items needs to be sold
                self.sell(self._portfolio[0])
                self._portfolio[0]._number_owned=0
            if (not self._portfolio[1] in port): 
                self.sell(self._portfolio[1])
                self._portfolio[1]._number_owned=0
            if (not self._portfolio[2] in port): 
                self.sell(self._portfolio[2])
                self._portfolio[2]._number_owned=0
            

            
        else:
            stock[0]._number_owned=int(MONEY_PER_STOCK/stock[0]._currPrice)
            self.buy(stock[0])
            
            stock[1]._number_owned=int(MONEY_PER_STOCK/stock[1]._currPrice)
            self.buy(stock[1])
            
            stock[2]._number_owned=int(MONEY_PER_STOCK/stock[2]._currPrice)
            self.buy(stock[2])
           
            
            port.append(stock[0])
            port.append(stock[1])
            port.append(stock[2])      
        
        
        
        
        
        
        self._portfolio=port
        
        
    def buy(self, stock):
        print("buy")
        #print(stock._currPrice)
        price=temp=quandl.get("WIKI/"+(str(stock._symbol)), end_date=self._curr_day, rows=1)
        self._money.buy(price.Close[0] , stock._number_owned)
        
    def sell(self, stock):
        print("sell")
        price=temp=quandl.get("WIKI/"+(str(stock._symbol)), end_date=self._curr_day, rows=1)
        number=stock._number_owned
        self._money.sell(price.Close[0], number)
        #print("end of sell")
        
        
        
        

f=Control()
f.launch()


