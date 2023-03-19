n = int(input())
student_marks = {}
for _ in range(n):
    name, *marks = input().split()
    student_marks[name] = list(map(float, marks))
query_name = input()

marks = student_marks[query_name]
average = sum(marks) / len(marks)
print("{:.2f}".format(average))