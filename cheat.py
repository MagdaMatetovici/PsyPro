## Assignment 3.2P.9 - 2022 Programming in Psychological Science
#
# Record of Revisions
#
# Date            Programmer              Descriptions of Change
# ====         ================           ======================
# 27-Jan-22    Magda Matetovici               Original code


def cheat(exercise):
    """"Prints the solution for the requested exercises
        *Only first 5 exercises of week 1 are available*

    Parameters:
        exercise(string): The exercise for which the solution is wanted
    Returns:
        A printed text containing the correct solution for the exercise
    """

    exercises = ["exercise_1_week1", "exercise_2_week1", "exercise_3_week1", "exercise_4_week1", "exercise_5_week1"]
    if exercise == "exercise_1_week1":
        print("""
            #Here we need to import numpy as np, before calling the np.zeros function,
            #it does not have to be on top of the script, but before I call these functions
            
            import numpy as np
            another_array = np.zeros((2, 4, 6))
            print(another_array)
        """)
    elif exercise == "exercise_2_week1":
        print("""
              another_array = np.zeros((2, 4, 6))

            # valid solution #1 - indexes the single element
            print(another_array[-1, 0, 2])
            
            # valid solution #2 - subsets the full dimension
            print(another_array[:, 0, :])
            print(another_array[:, :, 2])
            print(another_array[-1, :, :])
            
            # Generally, remember that Python (in contrast to R) 
            #     - is zero-indexed (indices go from 0 to (n-1))
            #     - negative indices "invert" the access instead of deselection
            #     - you need to indicate fully indexed dimensions with a colon     
        """)
    elif exercise == "exercise_3_week1":
        print("""
                     
            another_array = np.zeros((2, 4, 6))
            new_array = another_array.copy() 
            # alternatively: new_array = np.copy(another_array)
            new_array[1, 2, 2] = 1
            print(f"another: '{another_array[1, 2, 2]}' vs. new: '{new_array[1, 2, 2]}'")
            
            # In Python, when using =, we only assign a reference to an object in memory,
            # so both new_array and another_array are pointing to the same memory
            # allocation, namely, the one created by np.zeros(). To make a true copy, you
            # can use the .copy() method or np.copy().     
        """)
    elif exercise == "exercise_4_week1":
        print("""
            %paste  # does not work in a python script
            # it is only defined for iPython terminal execution
            #
            # in native Python, `%` is the modulo operator 
               """)
    elif exercise == "exercise_5_week1":
        print("""
                 # to change the working directory: 
                %cd "your directory" 
                # print the current working directory: 
                %pwd
                # list the contents of the working directory: 
                %ls
                # list current workspace variables: 
                %who   # variable names
                %whos  # objects with additional information
                       """)
    else:
        print("Please insert either: 'exercise_1_week1', 'exercise_2_week1', 'exercise_3_week1', 'exercise_4_week1'"
            " or 'exercise_5_week1'")

