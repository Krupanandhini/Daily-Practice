from collections import namedtuple

N = int(input())
fields = input().split()
students = namedtuple('student',fields)

total = 0
for i in range(N):
    f = input().split()
    student = students(*f)
    total += int(student.MARKS)
print('{:.2f}'.format(total/N))
