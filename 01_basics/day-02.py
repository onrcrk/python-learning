class1 = [85, 90, 78, 92, 88]
print(class1)
print("You can see the list of exam scores. Now, I will sort the list in ascending order.")
class1.sort()
print(class1)
print("You can see the sorted list. Now let's say the last integer of the list is my exam score.\n" \
"I can remove it with the pop command and store it in the sinav_notum variable.\n" \
"As you can see, this shows us my exam score.")
my_exam_score = class1.pop()
print("Other exam scores are:",class1)
print("My exam score is:", my_exam_score)

print("Now, I will add 8 points to my exam score and print it.")
my_exam_score += 8
print("My exam score is now:", my_exam_score)

class2 = [75, 82, 91, 89, 95]
print("Now, I created a new list named class2. There is the list:", class2)
print("I can extend the class1 list with the class2 list. This will add all the elements of class2 to class1.")
class1.extend(class2)
print("The combined list is:", class1)

print("My exam score isn't on the list. Let's add it back to the list with the append command.")
class1.append(my_exam_score)
print("The list after adding my exam score back is:", class1)

print("What we do if we want to find the minimum value of the list? We can use the min function.")
print(min(class1))
print("You can see the minimum value of the list. Now, I will find the maximum value of the list.")
print("Maximum value is:", max(class1))
print("If we want to learn the arithmetic mean of the list, we can use the sum and len functions.")
print("Arithmetic mean is:", sum(class1)/len(class1))