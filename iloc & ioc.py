import pandas as pd

#iloc -- used to fetch the rows & columns
#syntax -- df.iloc[start:stop:step, start:stop:step]
#ioc --- used to fetch the data using column-names
#syntax -- df.loc[:, "column_m":"column_n"]
'''
students = {'stu_id' : [1,2,3,4,5],
             'stu_name' : ['gani','manju','vikas','tejas','nags'],
             'tea_id' : [10,30,10,40,20]}

df1 = pd.DataFrame(students)
print(df1)


print('******************************************************************************')
print(df1.loc[:,"stu_id" : "stu_name"])
#print(df1.iloc[0:3:2,0:1])

#o/p:
   stu_id stu_name  tea_id
0       1     gani      10
1       2    manju      30
2       3    vikas      10
3       4    tejas      40
4       5     nags      20
******************************************************************************
   stu_id stu_name
0       1     gani
1       2    manju
2       3    vikas
3       4    tejas
4       5     nags

Process finished with exit code 0

'''
#############################################################################################

#Group by Function.

df = pd.DataFrame({'Animal': ['Falcon', 'Falcon',
                              'Parrot', 'Parrot'],
                   'Max Speed': [380., 370., 24., 26.]})

df2= df.groupby("Animal")
print(df2.max())