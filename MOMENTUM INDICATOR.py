# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:23:11 2019

@author: Dell
"""

'''

Momentum, also referred to as MOM, is an important measure of speed and magnitude of
price moves. This is often a key indicator of trend/breakout-based trading algorithms.

In its simplest form, momentum is simply the difference between the current price and
price of some fixed time periods in the past. Consecutive periods of positive momentum
values indicate an uptrend; conversely, if momentum is consecutively negative, that
indicates a downtrend. Often, we use simple/exponential moving averages of the MOM
indicator, as shown here, to detect sustained trends

'''
import pandas as pd
import matplotlib.pyplot as plt

timePeriod=20

history=[]
MOMvalues=[] #where MOM refers to momentum


fanmilk=pd.read_excel(r'C:\Users\Dell\Downloads\fanmilk VWAP closing prces.xlsx') 
adjustedClosefanmilk=fanmilk['Closing Price VWAP (GHS)'].tail(365)

for x in adjustedClosefanmilk:
    
    history.append(x)
    
    if len(history)>timePeriod:
        del(history[0])
    
    MOM=x-(history[0])
    MOMvalues.append(MOM)
    
momentum=pd.DataFrame(index=fanmilk['Date'].tail(365))  
momentum['MOMvalues']=MOMvalues
momentum['adjustedClose']=fanmilk['Closing Price VWAP (GHS)']

MOMvalues=momentum['MOMvalues']
adjustedCloseplot=momentum['adjustedClose']

fig=plt.figure()
axis=fig.add_subplot(211,ylabel='Stock Prices')
fanmilk['Closing Price VWAP (GHS)'].plot(ax=axis,color='g',lw=2,legend=True)
axis2=fig.add_subplot(212,ylabel='Momentum')
MOMvalues.plot(ax=axis2,color='r',lw=2,legend=True)

plt.show()




    
    
    