
from statistics import mean

grades = {
    'python': [10, 5, 6, 8],
    'git': [3, 4, 6],
    'django': [8, 7, 9]
}

print(len(grades))

sum_ = 0
for el in grades.items():
    print(mean(el[1]))
    sum_ += mean(el[1])
print(round(sum_ / len(grades), 1))

