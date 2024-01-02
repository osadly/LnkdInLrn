# Consider adding code to iprt Pandas & reading from data/olympics.csv file in the course excercise files

oo100 = oo.groupby(['Edition','Athlete','NOC']).count()   #value_counts()
oo100_2 = oo100.sort_values(by=['Medal','Edition'],ascending=[False,True])
oo100_2[(oo100_2.Medal>5)]