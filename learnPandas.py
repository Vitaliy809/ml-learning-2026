import pandas as pd

# DataFrame — це таблиця (як Excel але в Python)
# data = {
#     "name": ["Віталік", "Аня", "Олег"],
#     "age": [18, 20, 19],
#     "grade": [95, 88, 72]
# }

# df = pd.DataFrame(data)
# # print(df)
# print(df.head(3))
# print(df.name)
# print(df.grade)
# print(df.shape)
# print(df.describe())


# data = {
#     "name": ["Віталік", "Аня", "Олег", "Катя", "Дмитро"],
#     "age": [18, 20, 19, 21, 18],
#     "grade": [95, 88, 72, 91, 65],
#     "city": ["Львів", "Київ", "Львів", "Харків", "Київ"]
# }

# df = pd.DataFrame(data)

# print(df[df["grade"] > 85])
# print(df[df["city"] == "Львів"])
# print(df[(df["grade"] > 85) & (df["city"] == "Львів")])


# df["passed"] = df["grade"] >= 75
# df = df.sort_values("grade", ascending= False)
# print(df)
# print(df[["name" , "grade"]])

# print(df.groupby("city")["grade"].mean())
# print(df.groupby("city")["grade"].max())
# print(df.groupby("city")["name"].count())

# df["passed"] = df["grade"] >= 75
# print(df[df["passed"] == True])

# passed_df = df[df["passed"] == True]
# print(passed_df.groupby("city")["grade"].mean())

# df = df.sort_values("grade", ascending=False)  # ← "grade" без "s"
# print(df.head(3))
# print(passed_df.groupby("city")["name"].count())


# students = pd.DataFrame({
#     "id": [1, 2, 3, 4],
#     "name": ["Віталік", "Аня", "Олег", "Катя"]
# })

# # Таблиця оцінок
# grades = pd.DataFrame({
#     "id": [1, 2, 3, 5],
#     "grade": [95, 88, 72, 91]
# })

# print(pd.merge(students, grades, on="id", how="inner"))
# print(pd.merge(students, grades, on="id", how="left"))
# print(pd.merge(students, grades, on="id", how="outer"))


# data = pd.DataFrame({
#     "name": ["Віталік", "Аня", "Олег", "Катя", "Дмитро"],
#     "age": [18, None, 19, None, 18],
#     "grade": [95, 88, None, 91, None]
# })

# df = pd.DataFrame(data)

# print(df.isnull().sum())
# print(df["age"].fillna(df["age"].mean()))
# print(df["grade"].fillna(df["grade"].median()))
# print(df.dropna())

data = pd.DataFrame({
    "name": ["Віталік", "Аня", "Олег", "Катя", "Дмитро", "Соня"],
    "city": ["Львів", "Київ", "Львів", "Харків", "Київ", "Львів"],
    "subject": ["Math", "Math", "Python", "Python", "Math", "Python"],
    "grade": [95, 88, 72, 91, 65, 84]
})
df = pd.DataFrame(data)

print(pd.pivot_table(df, values="grade", index="subject", columns="city", aggfunc="mean"))
# print(pd.pivot_table(df, values="grade", index="city",aggfunc="max"))
