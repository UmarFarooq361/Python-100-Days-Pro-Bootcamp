name1= input("Enter your name ?")
name2= input("Enter there name ?")

combined_name = name1+name2
combined_name = combined_name.lower()

true_count = 0
love_count = 0

true_count += combined_name.count("t")
true_count += combined_name.count("r")
true_count += combined_name.count("u")
true_count += combined_name.count("e")

love_count +=  combined_name.count("l")
love_count +=  combined_name.count("o")
love_count +=  combined_name.count("v")
love_count +=  combined_name.count("e")

score = str(true_count)+str(love_count)
score = int(score)
if score<10 or score>90:
    print(f"Your score is {score} and you are not perfect for each others .")
elif score>=40 and score<=50:
    print(f"Your score is {score} and you are perfect match for each others .")
else:
    print(f"Your score is {score}")

