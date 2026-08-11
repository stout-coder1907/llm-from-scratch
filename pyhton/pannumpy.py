import numpy as np
import pandas as pd 

a = np.array([[2,3,4],[47,343,3]])

print(a)
print(type(a))

row = [2,3]

print(row in a.tolist())

import numpy as np

num1 = np.array([1, 2])
num2 = np.array([[10, 20],
                 [30, 40]])
for a, b in np.nditer([num1, num2]):
    print(a,b)

n = num2.flatten()

print(n)

print(np.size(num2,0))

num = num2.astype(np.float64)

m = np.array([[9, 9, 9], [8, 8, 8]])
rows = np.size(m,0)
cols = np.size(m,1)

print("Rows:", rows)
print("Columns:", cols)

print(np.sum(num2,0))

import numpy as np

n_arr = np.array([75.42436315, 42.48558583, 60.32924763])
print("Array:")
print(n_arr)

n_arr[n_arr > 50.] = 15.50 
print("Result:")
print(n_arr)

print(np.where(num2>15,1,0))


arr = np.array([[10, 20, 30], [40, 5, 66], [70, 88, 94]])
print("Array:")
print(arr)

res = arr[[0,2]]
print("Accessed Rows :")
print(res)

# Importing Library
import numpy as np

# creating 2d array
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculating mean across Rows
row_mean = np.mean(arr, axis=1)

row1_mean = row_mean[0]
print("Mean of Row 1 is", row1_mean)

row2_mean = row_mean[1]
print("Mean of Row 2 is", row2_mean)

row3_mean = row_mean[2]
print("Mean of Row 3 is", row3_mean)


# Calculating mean across Columns
column_mean = np.mean(arr, axis=0)

column1_mean = column_mean[0]
print("Mean of column 1 is", column1_mean)

column2_mean = column_mean[1]
print("Mean of column 2 is", column2_mean)

column3_mean = column_mean[2]
print("Mean of column 3 is", column3_mean)

import pandas as pd
import numpy as np

data = np.array(['g', 'e', 'e', 'k', 's'])
s = pd.Series(data)
print("Pandas Series:")
print(s)

# read data
import pandas as pd

df = pd.read_csv("data.csv")
print(df.head())

print(df.isnulll().sum())
print(df.isnull().sum())
df = df.fillna(0)

# grouping the data
res = df.groupby('category')['sales'].sum()
print(res)

data = {'Name': ['Jake', 'Mike'],
        'Age': [25, 30],
        'Salary': [50000, 55000]}

df = pd.DataFrame(data)
print(df.head())

df =df.set_index('Name')

# import module
import pandas as pd

# assign data
dataFrame = pd.DataFrame({'Name': [' RACHEL  ', ' MONICA  ', ' PHOEBE  ',
                                   '  ROSS    ', 'CHANDLER', ' JOEY    '],
                          
                          'Age': [30, 35, 37, 33, 34, 30],
                          
                          'Salary': [100000, 93000, 88000, 120000, 94000, 95000],
                          
                          'JOB': ['DESIGNER', 'CHEF', 'MASUS', 'PALENTOLOGY',
                                  'IT', 'ARTIST']})
# filter dataframe
display(dataFrame.loc[(dataFrame['Salary']>=100000) & (dataFrame['Age']< 40) & (dataFrame['JOB'].str.startswith('D')),
                    ['Name','JOB']])