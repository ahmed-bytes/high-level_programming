# Learning For Loops
Users = {"Adam": "active", "Jane": "active"}

for w, status in Users.copy().items():
    if status == "active":
        print("active")

for i in range(2):
    print(i)


a = ["Mary", "laffette", "soma", "angel"]

for j in range(len(a)):
    print(j, a[j])
