#2303A52313
#Sanju choppara
#batch-45

#TASK_1
#Generate a Python function that accepts a year as input, checks whether it is a leap year, and returns the result.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False
print(is_leap_year(2024))
print(is_leap_year(2023))
#Explanation
# #This function checks leap year conditions:
#Divisible by 4 and not divisible by 100
#OR divisible by 400
#If conditions satisfy, it returns True, else False.



#TASK_2
#Input: 10 cm → Output: 3.94 inches
#Create a Python function that converts centimeters to inches.
def cm_to_inches(cm):
    return cm * 0.3937

print(cm_to_inches(10))
print(cm_to_inches(25))
#Explanation
#1 centimeter equals 0.3937 inches.
#The function multiplies centimeters by 0.3937 to get inches.




#TASK-3
#"John Smith" → "Smith, John"
#"Anita Rao" → "Rao, Anita"
#Create a Python function that formats full name as Last, First.
def format_name(name):
    parts = name.split()
    return parts[1] + ", " + parts[0]

print(format_name("John Smith"))
print(format_name("Anita Rao"))
#Explanation
#The name is split into words.
#First name becomes second position and last name becomes first position.



#TASK_4
#Zero-Shot Prompt
#Generate a Python function to count vowels in a string.

#Zero-Short code
def count_vowels_zero(s):
    count = 0
    for ch in s:
        if ch.lower() in "aeiou":
            count += 1
    return count
#Few-Shot Prompt
#"hello" → 2
#"education" → 5
#Create a Python function to count vowels.

#Few-Shot Code
def count_vowels_few(s):
    vowels = "aeiou"
    return sum(1 for ch in s.lower() if ch in vowels)

print(count_vowels_zero("hello"))
print(count_vowels_few("education"))

#| Feature     | Zero-Shot | Few-Shot  |
#| ----------- | --------- | --------- |
#| Accuracy    | Good      | Excellent |
#| Readability | Medium    | High      |
#| Code Length | Longer    | Shorter   |





#TASK-5
#Prompt Used (Few-Shot)
#File with 3 lines → Output: 3
#File with 5 lines → Output: 5
#Generate a Python function that reads a text file and counts number of lines.
def count_lines(filename):
    with open(filename, "r") as file:
        return len(file.readlines())

print(count_lines("sample.txt"))
#Sample Input File (sample.txt)


#Explanation
#The file is opened in read mode.
#All lines are read and counted using len().



