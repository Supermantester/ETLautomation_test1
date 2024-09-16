import pandas as pd
'''//////taFrame(data, index = , columns = )

data = [15,30,45,60]

names = ['ganesh','amul','nandini','doodla']

dataframe_1 = pd.DataFrame(data,index = names, columns= ['age'])
print(dataframe_1)


o/p :

         age
ganesh    15
amul      30
nandini   45
doodla    60

'''
'''
#ex:2

fruits_dic = {"names":['apple','banana','chikku'],
              "rate":[200,440,800]}

print(pd.Series(fruits_dic))
print(pd.DataFrame(fruits_dic, index=['a','b','c']))

#o/p :

names    [apple, banana, chikku]
rate             [200, 440, 800]
dtype: object
    names  rate
a   apple   200
b  banana   440
c  chikku   800

'''

'''
#ex:3 Nested list (without column name, index)

emp = [["john", 2000, "swimming"],
       ["henry",25000, "treskking"]]

nested_list = pd.DataFrame(emp)
print(nested_list)

#o/p: 

       0      1          2
0   john   2000   swimming
1  henry  25000  treskking

'''

'''
#ex:4 Nested list (with column name, index)

emp2 = [["john", 2000, "swimming"],
       ["henry",25000, "treskking"]]

nested_list2 = pd.DataFrame(emp2, index = ['a','b'], columns= ['name','salary','hobby'])
print(nested_list2)

#o/p :
    name  salary      hobby
a   john    2000   swimming
b  henry   25000  treskking

'''

'''
#ex:4 How many columns are there in the data frame
emp2 = [["john", 2000, "swimming"],
       ["henry",25000, "treskking"]]

nested_list2 = pd.DataFrame(emp2, index = ['a','b'], columns= ['name','salary','hobby'])

print(nested_list2.columns)

#o/p :

Index(['name', 'salary', 'hobby'], dtype='object')
'''

'''
#ex:5 display only a particular column

list_emp = {'emp_name':['ganesh','pavan','veeresh','harish'],
            'emp_sal': [10000,20000,30000,40000],
            'emp_age': [25,35,45,55]}
emp_list1 = pd.DataFrame(list_emp)

print(emp_list1.columns)
print(emp_list1['emp_name'])
print(emp_list1[['emp_name','emp_sal']])

'''

'''
#ex:6 display only one row & one column

list_emp = {'emp_name':['ganesh','pavan','veeresh','harish'],
            'emp_sal': [10000,20000,30000,40000],
            'emp_age': [25,35,45,55]}
emp_list1 = pd.DataFrame(list_emp)
print(emp_list1['emp_name'][0])

#o/p :
ganesh

'''

'''
#ex:7 display only multiple row & one column

list_emp = {'emp_name':['ganesh','pavan','veeresh','harish'],
            'emp_sal': [10000,20000,30000,40000],
            'emp_age': [25,35,45,55]}
emp_list1 = pd.DataFrame(list_emp)
print(emp_list1['emp_name'][0:])

#o/p :
0     ganesh
1      pavan
2    veeresh
3     harish

'''

##################################################
'''
# convert data type using astype() 
# ex_1: float to int

num = { 'age':[10.5,23.9,46.1,90.05]}
num_df = pd.DataFrame(num)
print(num_df.age)
num_df_type_1 = num_df.astype(int)
print(num_df_type_1)

#o/p:

0    10.50
1    23.90
2    46.10
3    90.05
Name: age, dtype: float64
   age
0   10
1   23
2   46
3   90

'''
###################################
'''
#series attribute:
1. index -- Series.index
2. array -- Series.array
3. values -- Series.values
4. name -- Series.name
5. shape -- Series.shape 
6. ndim -- Series.ndim --n-dimention
7. size -- Series.size
8. nbyte -- Series.nbytes
9. memory usuage -- memory occupied by both index & values
10. empty -- Series.empty
'''
#####################################
'''
# 1. shape in seies

b = pd.Series([4,6,8,10,12], name = 'even')
print(b)
b_shape = b.shape
print(b_shape)

#o/p : 
0     4
1     6
2     8
3    10
4    12
Name: even, dtype: int64
(5,)

'''
###################################################

'''
# 1. shape in DataFrame

c = pd.DataFrame( {'size':[4,6,8,10,12]})
print(c)
c_shape = c.shape
print(c_shape)

#o/p:

   size
0     4
1     6
2     8
3    10
4    12
(5, 1)

'''
########################################
'''
# ndim in series & dataframe
b = pd.Series([4,6,8,10,12], name = 'even')
b_ndim  = b.ndim
print(f'series ndim details are {b_ndim}')

# dataframe:

c = pd.DataFrame( {'size':[4,6,8,10,12]})
c_ndim = c.ndim
print(f'series ndim details are {c_ndim}')

#o/p: 
series ndim details are 1
series ndim details are 2

'''
#####################################################

