class1 = [85, 90, 78, 92, 88]
print(class1)
print("You can see the list of exam scores. Now, I will sort the list in ascending order.")
class1.sort()
print(class1)
print("You can see the sorted list. Now let's say the last integer of the list is my exam score.\nI can remove it with the pop command and store it in the sinav_notum variable.\nAs you can see, this shows us my exam score.")
my_exam_score = class1.pop()
print("Other exam scores are:",class1)
print("My exam score is:", my_exam_score)
print("Now, I will add 8 points to my exam score and print it.")
my_exam_score =+ 8
print("My exam score is now:", my_exam_score)
