english_marks = int(input("Enter the marks in english:"))
maths_marks = int(input("Enter the marks in maths:"))

# if both marks are more than 80, then print A grade
if english_marks > 80 and maths_marks > 80:
    print("A grade")

# if either of marks are more than 80, then print B grade
elif english_marks > 80 or maths_marks > 80:
    print("B grade")

# if both tha marks are below 80, then print C grade
else:
    print("C grade")            