# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 17:01:28 2017

@author: Bany
"""
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt  # need to plot

name = ['Schrodinger','Einstein','Feynman','Neumann','Dirac','Bohr','Fermi','Heisenberg','Pauli','Newton','Leibniz','Planck']
score = [64,90,98,100,92,90,91,72,88,93,93,52]
score_a = np.array(score)

avg = sum(score_a)/len(score_a)  # average definition
avg_t = format(avg,'.2f')  # average for Second decimal place
std_dev = (sum((score_a-avg)**2)/len(score_a))**0.5   # standard deviation definition
                       # ^ reason why need avg_t 
std_dev_t = format(std_dev,'.2f')  # standard deviation for Second decimal place

table = {'Name' : name, 'Score' : score_a}  # table column subject
data = DataFrame(table, index=['-','-','-','-','-','-','-','-','-','-','-','-']) # simple index (just makes look good)


data_m = DataFrame({'Name':' ','Score': avg_t, 'rank':' '}, index=['mean'])  # make average row
data_s = DataFrame({'Name':' ','Score': std_dev_t, 'rank':' '}, index=['std'])  # make standard deviation row
# 같은 행,열 개수를 가져야하므로 미리 rank를 넣어준다
# rank의 r을 소문자로 쓴 이유는 R로 쓰면 아스키코드 순서대로 Name Rank Score 순으로 열이 출력된다.


data_sort = data.sort_values(by=['Score'],ascending=False)  # Score reordering for Descending order
data_sort['rank']=data_sort['Score'].rank(ascending=False, method='min') # input rank by score data
                                        # Descending order and 등수 내림

data_sort_prm = DataFrame(data_sort).append(data_m).append(data_s)  # insert mean and std row


print(data, '\n')  # print original table
print(data_sort_prm)   # print modified table

# plt.figure(figsize=(8, 8), dpi=100)  # plot size
plt.plot(data_sort['rank'],data_sort['Score'],label='Test rank')
plt.xlabel('Rank')  # x-axis
plt.ylabel('Score')  # y-axis
plt.title('Physics Test')  # title
plt.grid()  # grid
plt.legend()  # for label
plt.show()  # plot show

data_sort_prm.to_csv("C:\\Users\\Bany\\Documents\\CS\\Problem.2\\Data.csv")  # save as csv


# plot  import seaborn > 예쁘게 해줌

### reference : https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.rank.html

