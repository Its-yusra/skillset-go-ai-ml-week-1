# %%
file_name = "student.txt"

with open(file_name, "w") as file:
    file.write("Name: Yusra\n")
    file.write("Department: Computer Science\n")

with open(file_name, "r") as file:
    content = file.read()

print(content)
# %%
