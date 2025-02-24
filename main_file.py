# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 14:53:53 2025

@author: mdyri
"""

# This program calculate tuition cost for students
# Febraury 20, 2025
# CSC-121 m3Pro - Purchases
# Rina Moody


# create the lists (stu_names, courses, tuition)

stu_names = ['Zakari Watson', 'Jerom Williams', 'Dominique Ross', 'Diana Shepard', 'Yuko Mayo', 'Rashad Ahmed', 'Susan Jones']
courses = ['MAT 035(Concepts of Algebra)', 'CTI 115(Computer System Foundations)', 'BAS 120 Intro to Analytics', 'CSC 121 Python Programming']
tuition = [460, 520.98, 500, 783.88]

# define a function to registered students for courses


# create a main

def main():
    
    # display course and menu
    course_display()
    menu()
    
    # ask user to choose an option
    option = int(input('\nEnter your choice: '))
    
    while option != 2:
        
        registrations = []
        
        
        if option == 1:
            for stu, cour in zip(stu_names, courses):
                print(f'Is {stu} taking {cour}?')
                answer = input('Enter "y" for yes: ')
                
                if answer == 'y':
                    registrations.append(courses)
                    
        elif option == 2: #display students
            
            display_students()
            
            
                             
            
        elif option == 3: # exit
            
            print("\nProgram Terminating....")
            break
       

    
    

# function to display the list of courses and tuition
def course_display():
    '''
    Display the course and tuition in a tabular format
    Arguments:
        courses: A list of course names
        tuition: A list of tuition fees

    Returns
    -------
    None.

    '''
   
    # display the table header
    print(f"\n{'Course Name':<40}{'Tuition10'}")
    print('-' * 50)
    
    for i in range(len(courses)):
        print(f'{courses[i]:<40}${tuition[i]:<10.2f}')
    
def display_students():
    """
    displays the list of students

    Returns
    -------
    None.

    """
    print("\nSelect from list of student name below:")
    print()
    for i, student in enumerate(stu_names):
        print(f'{i + 1}) {student}')
    
        
        
        
# display the list of the options
def menu():
    
    print('\n-------------------- MENU --------------------')
    print('1) Calculate Tuition for ALL Students')
    print('2) Calculate Tuition For Specific Students')
    print('3) Exit')    

# function to display the list of students



    
if __name__ == '__main__':
    main()
    
    