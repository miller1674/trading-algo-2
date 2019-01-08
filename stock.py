import quandl
import matplotlib.pyplot as plt
import pandas as pd
quandl.ApiConfig.api_key = "bAqiaN9tTgprMomJXhzu"

NUM_OF_DAYS=2000
#NUM_OF_DAYS_FOR_LOW=2000


class Stock:
    def __init__(self, symbol, currentDay):
        
        self._symbol = symbol
        temp=quandl.get("WIKI/"+(str(symbol)), end_date=currentDay, rows=1)
        self._currPrice=temp.Close[0]
        self._moving_avg=0
        self._number_owned=0
        self._high=0
        
        days=0
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay)
        
        if (len(temp.Close)<NUM_OF_DAYS):
            days=len(temp.Close)
        else:  
            days=NUM_OF_DAYS
        
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=days)
        high=0
        for y in range(0, days):
            if (high<temp.High[y]):
                high=temp.High[y]
        
        self._high=high
        
        
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=days)
        low=temp.Low[0]
        for y in range(0, days):
            if (low>temp.Low[y]):
                low=temp.Low[y]
        
        self._low=low
		
		
    def printStock(self):
        print("Symbol "+self._symbol+" Curr Price:"+ str(self._currPrice)+" Moving Avg:"+ str(self._moving_avg)+" HIGH:"+str(self._high)+ " LOW:"+str(self._low)+" Owned #:"+str(self._number_owned))
	
    def movingAvg(self, numDays, currentDay):
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=numDays)
        #print(temp)
        sum=0
        for y in range(0, numDays):
            sum+=temp.Close[y]
        move=sum/numDays
        self._moving_avg=move/self._currPrice
        
        
        
    def all_time_high(self):
        
        print("Calculate All Time High:")
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=NUM_OF_DAYS)
        high=0
        for y in range(0, NUM_OF_DAYS):
            if (high<temp.High[y]):
                high=temp.High[y]
        
        self._high=high
        
        
    def all_time_low(self):
        temp=quandl.get("WIKI/"+self._symbol, end_date=currentDay ,rows=NUM_OF_DAYS)
        low=temp.Low[0]
        for y in range(0, NUM_OF_DAYS):
            if (low>temp.Low[y]):
                low=temp.Low[y]
        
        self._low=low
        
    def buy(self, number):
        self._number_owned=number
	
		



