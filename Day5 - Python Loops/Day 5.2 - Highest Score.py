score = input("Enter the students score : ").split()

max = 0
for n  in range(0 , len(score)):
    score[n] = int(score[n])

for i in score:
    if i > max:
        max = i
print(f"The highest score in the student list is {max}")
