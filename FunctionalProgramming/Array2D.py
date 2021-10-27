def two_d_array():
    """
    Description:
        This function prints 2d array. It takes number of rows and colums
        as well as values of array from user.    
    """
     # take number of rows and columns fom user
    num_of_rows = int(input("Enter number of rows: "))
    num_of_columns = int(input("Enter number of columns: "))
    array = []
    for i in range(0,num_of_rows):
        array.append([])

    for i in range(0, num_of_rows):
        for j in range(0, num_of_columns):
            num = int(input(f"enter value for row {i} column {j} "))
            array[i].append(num)
    print(array)

two_d_array()