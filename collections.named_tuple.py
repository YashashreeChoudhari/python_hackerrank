#Que. Read the student records, where the columns (`ID`, `MARKS`, `NAME`, `CLASS`) can appear in any order, and use `namedtuple` to store each record. Print the average of the students MARKs correct to 2 decimal places.

from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())

total = 0
for _ in range(n):
    student = Student(*input().split())
    total += int(student.MARKS)

print("{:.2f}".format(total / n))