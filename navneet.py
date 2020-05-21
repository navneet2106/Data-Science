
# coding: utf-8

# In[55]:


import pandas as pd

df = pd.read_csv('C:/Users/BL003/Documents/Python Scripts/201408_trip_data.csv')
df


# In[54]:


# Total number of trips in the data set?
print("Total number of Trips:" + str(df.Trip_ID.count()))


# In[64]:


# Number of unique trips in the data set?
dict = {df.Start_Station[i]: df.End_Station[i] for i in range(len(df.Start_Station))}
print(len(dict))


# In[181]:


#Which bike is used the most in the data set?
pd.value_counts(df.Bike_No).head(1)

#output- bike number 558 appears 569 times


# In[153]:


#Which bike is used the most in the data set?
#above can also be done by using the below function
def most_freq(x): 
    counter = 0
    num = x[0] 
    for i in x: 
        curr_freq = x.count(i) 
        if(curr_freq> counter): 
            counter = curr_freq
            num = i 
  
    return num 
lst=list(df.Bike_No)
print("Most used bike is -  " + str(most_freq(lst)))


# In[183]:


#Which week day has more trips? 

df["Start_Date"] = pd.to_datetime(df["Start_Date"])
#df.Start_Date.date()

date_strings = [d.strftime('%Y-%m-%d') for d in df["Start_Date"]]

date_strings


# In[189]:


import calendar 
  
def findDay(date): 
    year,month,day = (int(i) for i in date.split('-'))     
    dayNumber = calendar.weekday(year, month, day) 
    days =["Monday", "Tuesday", "Wednesday", "Thursday", 
                         "Friday", "Saturday", "Sunday"] 
    return (days[dayNumber]) 
  
# Driver program
lst=[]
for i in range (len(date_strings)):
    lst.append(findDay(date_strings[i]))

pd.value_counts(lst).head(1)


# In[185]:


#Sort start terminals according to frequency of usage and list top ten and bottom ten.

from collections import Counter
sorted_start_terminal = ([item for items, c in Counter(df.Start_Terminal).most_common() for item in [items] * c])
top_ten = sorted_start_terminal[:10]
last_ten=sorted_start_terminal[-10:]

print(" Top 10 elements" + str(top_ten))
print(" Last 10 elements" + str(last_ten))

