heights = input("Enter the height of students : ").split()
sum = 0
students = 0
for n  in range(0 , len(heights)):
    heights[n] = int(heights[n])

for height in heights:
    sum =  sum + height
    students += 1
average =  sum/students
round(average)
print(f"The average height in the student list is {average}")

