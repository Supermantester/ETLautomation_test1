import pandas as pd

#merging of 2 dataframes

#syntax : result = pd.merge(df1,df2, how = 'inner', on='common column)
#df1 & df2 -- dataframes 1,2

'''
students = {'stu_id' : [1,2,3,4,5],
             'stu_name' : ['gani','manju','vikas','tejas','nags'],
             'tea_id' : [10,30,10,40,20]}

df1 = pd.DataFrame(students)
print(df1)

teachers = {'tea_id' : [10,20,30,40,50],
             'sub_name' : ['maths','science','kannada','social','english'],
             }
df2 = pd.DataFrame(teachers)
print(df2)

df_merge = pd.merge(df1,df2, how = 'outer', on = 'tea_id')
print(df_merge)
#printing the headcount using below statement.
print(df_merge.head(3))
'''

#######################################################################################
'''
#renaming the column in pandas.

students = {'stu_id' : [1,2,3,4,5],
             'stu_name' : ['gani','manju','vikas','tejas','nags'],
             'tea_id' : [10,30,10,40,20]}

df1 = pd.DataFrame(students)
print(df1)

teachers = {'tea_id' : [10,20,30,40,50],
             'sub_name' : ['maths','science','kannada','social','english'],
             }
df2 = pd.DataFrame(teachers)
print(df2)

df_merge_renaming_col = pd.merge(df1,df2, how = 'outer', on = 'tea_id')

print(df_merge_renaming_col)

df_merge_2 = df_merge_renaming_col.rename({'stu_id':'student_id','stu_name':'student_name'})
print(df_merge_2)

#o/p :-

   stu_id stu_name  tea_id
0       1     gani      10
1       2    manju      30
2       3    vikas      10
3       4    tejas      40
4       5     nags      20
   tea_id sub_name
0      10    maths
1      20  science
2      30  kannada
3      40   social
4      50  english
   stu_id stu_name  tea_id sub_name
0     1.0     gani      10    maths
1     3.0    vikas      10    maths
2     5.0     nags      20  science
3     2.0    manju      30  kannada
4     4.0    tejas      40   social
5     NaN      NaN      50  english
   stu_id stu_name  tea_id sub_name
0     1.0     gani      10    maths
1     3.0    vikas      10    maths
2     5.0     nags      20  science
3     2.0    manju      30  kannada
4     4.0    tejas      40   social
5     NaN      NaN      50  english

'''
##############################################################################################

#finding the null values in each column using isnull function.

students = {'stu_id' : [1,2,3,4,5],
             'stu_name' : ['gani','manju','vikas','tejas','nags'],
             'tea_id' : [10,30,10,40,20]}

df1 = pd.DataFrame(students)
#print(df1)

teachers = {'tea_id' : [10,20,30,40,50],
             'sub_name' : ['maths','science','kannada','social','english'],
             }
df2 = pd.DataFrame(teachers)
#print(df2)

df_merge_renaming_col = pd.merge(df1,df2, how = 'outer', on = 'tea_id')

'''
 #case_1: 
 print(df_merge_renaming_col.isnull)
 
 #o/p: 
<bound method DataFrame.isnull of    stu_id stu_name  tea_id sub_name
0     1.0     gani      10    maths
1     3.0    vikas      10    maths
2     5.0     nags      20  science
3     2.0    manju      30  kannada
4     4.0    tejas      40   social
5     NaN      NaN      50  english>
'''

'''
#case_2:
print(df_merge_renaming_col.isnull())

#o/p:
   stu_id  stu_name  tea_id  sub_name
0   False     False   False     False
1   False     False   False     False
2   False     False   False     False
3   False     False   False     False
4   False     False   False     False
5    True      True   False     False

'''

'''
#case_3:
print(df_merge_renaming_col.isnull().sum())

#o/p:
stu_id      1
stu_name    1
tea_id      0
sub_name    0
dtype: int64
'''

#######################################################################################

'''
#converting a column  into binary using map function.

print(df_merge_renaming_col)

df_merge_col_to_binary = df_merge_renaming_col['sub_name'].map({'maths':1,'kannada':0})
print((df_merge_col_to_binary))

#o/p:

  stu_id stu_name  tea_id sub_name
0     1.0     gani      10    maths
1     3.0    vikas      10    maths
2     5.0     nags      20  science
3     2.0    manju      30  kannada
4     4.0    tejas      40   social
5     NaN      NaN      50  english
0    1.0
1    1.0
2    NaN
3    0.0
4    NaN
5    NaN
Name: sub_name, dtype: float64

'''

###############################################################################################

