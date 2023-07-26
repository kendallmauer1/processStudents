''' 
*   Professor B would like to know which of his student have a GPA below 3.0.
    To accomplish this, read the file - students.csv into the program. The program
    should evaluate the GPA to see if it is higher or lower than 3.0. If it is,
    then it should be written out to the file - processedStudents.csv. (This file
    already contains headers and the headers should NOT be overwritten.) 

*   Create a dictionary of each student where the student ID is the key
    and the GPA is the value.

*  print out the dictionary

*  print out the corresponding GPA for student - 567890123

I have outlined comments for each step of the program. You are
not required to use them but it is provided to help you work
through the logic of the problem.


'''


import csv


# create a file object to open the file in read mode
with open('students.csv', 'r') as infile:


# create a csv object from the file object
    read = csv.reader(infile)

#skip the header row
    header = next(read)

#create an outfile object for the pocessed record
    with open ('processedStudents.csv', 'w') as outfile:
        write = csv.writer(outfile)


#create a new dictionary named 'student_dict'
        student_dict = {}


#use a loop to iterate through each row of the file
        for row in read:
            stud_id = row[0]
            gpa = float(row[8])

    #check if the GPA is below 3.0. If so, write the record to the outfile

            if gpa < 3.0:
                write.writerow(row)
        



    # append the record to the dictionary with the student id as the Key
    # and the value as the GPA
    student_dict[stud_id] = gpa





#print the entire dictionary
for stud_id, gpa in student_dict.items():
    print(f"{stud_id},{gpa}")

#Print the student id 
if stud_id in student_dict:
    print(stud_id)
'''
#print out the corresponding GPA from the dictionary
for student_id, gpa in student_dict.items():
    print(f"The type of pet is: {i} and the name of the pet is: {j}")

'''







