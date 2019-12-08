'''
1.  Ask user to enter scores for Math, Chemistry, and   
    Phyiscs.
2.  If any entered score in below 35, terminate the program 
    and inform the user that the exam has been failed
3.  If all three scores are above 35, inform the user that 
    they have passed them exam and display the average score
4.  Display a grade based on the following criteria:
    a) <= 59  - C
    b) <= 69  - B
    c) >  70  - A

~ Cow.py ~

Made for "Python Core and Advanced" - Bharath Thippireddy Assignment 3: If-Else Ladder https://www.udemy.com/course/python-core-and-advanced/
'''
subjects = ["Math", "Physics", "Chemistry"]
scores = []
total_subjects = len(subjects)


def exam_pass():
    total_score = 0
    print("Congratulations! You passed the exam!")
    for i in range(0, total_subjects):
        print(f'{subjects[i]} : {scores[i]}')
    for i in range(0, total_subjects):
        total_score += scores[i]
    average = total_score / total_subjects
    print(f'Average: {average:.2f}')
    if average <= 59:
        print("You earned a C on this exam.")
    elif average <= 69:
        print("You earned a B on this exam.")
    else:
        print("You earned an A on this exam!")


def exam_fail(subject):
    print(f'You received fewer than 35 points in {subject}. You have failed this exam.')


def enter_score():
    fail = False
    for i in range(0, total_subjects):
        score = int(input(f'{subjects[i]}: '))
        if score >= 35:
            scores.append(score)
        else:
            exam_fail(subjects[i])
            fail = True
            break
    if fail == False:
        exam_pass()


enter_score()
