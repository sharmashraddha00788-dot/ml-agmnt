# # Pandas Implementation Notebook
# 
# Three simple implementations/demonstrations for each required Pandas function.

import pandas as pd
import numpy as np


# ## 1. Structures & Inspection

# pd.Series() - Implementation 1
s1 = pd.Series([10, 20, 30, 40])
print(s1)

# Implementation 2
s2 = pd.Series([10, 20, 30], index=["a", "b", "c"])
print(s2)

# Implementation 3
s3 = pd.Series({"Math": 80, "Python": 90, "DBMS": 75})
print(s3)


# pd.DataFrame() - Implementation 1
df1 = pd.DataFrame({"Name": ["Aman", "Riya"], "Marks": [80, 90]})
print(df1)

# Implementation 2
df2 = pd.DataFrame([[1, "A"], [2, "B"]], columns=["ID", "Name"])
print(df2)

# Implementation 3
df3 = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, 21, 19],
    "Marks": [75, 88, 92]
})
print(df3)


# pd.head() - Implementation 1
df = pd.DataFrame({"A": range(1, 8), "B": range(11, 18)})
print(df.head())

# Implementation 2
print(df.head(3))

# Implementation 3
print(df.head(2))


# df.info() - Implementation 1
df = pd.DataFrame({"Name": ["A", "B"], "Marks": [80, 90]})
df.info()

# Implementation 2
df2 = pd.DataFrame({"A": [1, 2, 3], "B": ["x", "y", "z"]})
df2.info()

# Implementation 3
df3 = pd.DataFrame({"Age": [20, 21, 22]})
df3.info()


# df.describe() - Implementation 1
df = pd.DataFrame({"Marks": [60, 70, 80, 90, 100]})
print(df.describe())

# Implementation 2
df2 = pd.DataFrame({"Age": [18, 19, 20, 21]})
print(df2.describe())

# Implementation 3
df3 = pd.DataFrame({"Math": [70, 80, 90], "Python": [75, 85, 95]})
print(df3.describe())


# ## 2. Selection & Data Cleaning

# df.loc[] - Implementation 1
df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [70, 85, 90]})
print(df.loc[0])

# Implementation 2
print(df.loc[0:1, ["Name", "Marks"]])

# Implementation 3
print(df.loc[df["Marks"] >= 85])


# df.iloc[] - Implementation 1
df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [70, 85, 90]})
print(df.iloc[0])

# Implementation 2
print(df.iloc[0:2, 0:2])

# Implementation 3
print(df.iloc[:, 1])


# df.query() - Implementation 1
df = pd.DataFrame({"Name": ["A", "B", "C"], "Marks": [70, 85, 90]})
print(df.query("Marks > 80"))

# Implementation 2
print(df.query("Marks == 85"))

# Implementation 3
print(df.query("Marks >= 70 and Marks < 90"))


# df.fillna() - Implementation 1
df = pd.DataFrame({"A": [1, np.nan, 3]})
print(df.fillna(0))

# Implementation 2
df2 = pd.DataFrame({"A": [10, np.nan, 30]})
print(df2.fillna(df2["A"].mean()))

# Implementation 3
df3 = pd.DataFrame({"A": [5, np.nan, 15]})
print(df3.fillna(method="ffill"))


# df.dropna() - Implementation 1
df = pd.DataFrame({"A": [1, np.nan, 3]})
print(df.dropna())

# Implementation 2
df2 = pd.DataFrame({"A": [1, 2, np.nan], "B": [4, np.nan, 6]})
print(df2.dropna())

# Implementation 3
df3 = pd.DataFrame({"A": [1, np.nan, 3]})
print(df3.dropna(axis=1))


# df.replace() - Implementation 1
df = pd.DataFrame({"Status": ["Yes", "No", "Yes"]})
print(df.replace("Yes", "Y"))

# Implementation 2
df2 = pd.DataFrame({"Marks": [40, 50, 40]})
print(df2.replace(40, 45))

# Implementation 3
df3 = pd.DataFrame({"Grade": ["A", "B", "C"]})
print(df3.replace({"A": "Excellent", "B": "Good"}))


# ## 3. Grouping & Transformations

# df.groupby() - Implementation 1
df = pd.DataFrame({
    "Dept": ["IT", "IT", "HR"],
    "Salary": [50000, 60000, 45000]
})
print(df.groupby("Dept")["Salary"].mean())

# Implementation 2
print(df.groupby("Dept")["Salary"].sum())

# Implementation 3
print(df.groupby("Dept").size())


# pd.merge() - Implementation 1
left = pd.DataFrame({"ID": [1, 2], "Name": ["A", "B"]})
right = pd.DataFrame({"ID": [1, 2], "Marks": [80, 90]})
print(pd.merge(left, right, on="ID"))

# Implementation 2
print(pd.merge(left, right, on="ID", how="inner"))

# Implementation 3
right2 = pd.DataFrame({"ID": [1, 3], "Marks": [80, 70]})
print(pd.merge(left, right2, on="ID", how="outer"))


# pd.concat() - Implementation 1
df1 = pd.DataFrame({"A": [1, 2]})
df2 = pd.DataFrame({"A": [3, 4]})
print(pd.concat([df1, df2]))

# Implementation 2
x = pd.DataFrame({"A": [1, 2]})
y = pd.DataFrame({"B": [3, 4]})
print(pd.concat([x, y], axis=1))

# Implementation 3
print(pd.concat([df1, df2], ignore_index=True))


# df.apply() - Implementation 1
df = pd.DataFrame({"Marks": [50, 60, 70]})
print(df["Marks"].apply(lambda x: x + 5))

# Implementation 2
print(df["Marks"].apply(lambda x: "Pass" if x >= 50 else "Fail"))

# Implementation 3
def double_value(x):
    return x * 2

print(df["Marks"].apply(double_value))


# pd.pivot_table() - Implementation 1
df = pd.DataFrame({
    "Dept": ["IT", "IT", "HR", "HR"],
    "Gender": ["M", "F", "M", "F"],
    "Salary": [50, 60, 45, 55]
})
print(pd.pivot_table(df, values="Salary", index="Dept", aggfunc="mean"))

# Implementation 2
print(pd.pivot_table(df, values="Salary", index="Gender", aggfunc="sum"))

# Implementation 3
print(pd.pivot_table(df, values="Salary", index="Dept",
                     columns="Gender", aggfunc="mean"))


# ## Quick Practice

students = pd.DataFrame({
    "Name": ["Aman", "Riya", "Karan", "Neha"],
    "Department": ["CSE", "CSE", "ECE", "ECE"],
    "Marks": [78, 91, 68, 85]
})

print(students.head())
print("\nStudents with marks above 75:")
print(students.query("Marks > 75"))
print("\nAverage marks by department:")
print(students.groupby("Department")["Marks"].mean())

