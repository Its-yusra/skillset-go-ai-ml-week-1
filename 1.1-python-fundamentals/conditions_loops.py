# %%
marks = float(input("Enter marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

print("Numbers from 1 to 10:")

for number in range(1, 11):
    print(number)
# %%
