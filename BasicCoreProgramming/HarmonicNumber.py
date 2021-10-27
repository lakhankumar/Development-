def nthHarmonic(number) :
    """
    Description:
        This function genrate harmonic number of nth number
    
    Parameter:
        number parameter is nth harmonic value
        
    Return:
        harmonic return value is nth harmonic value
    """
 
    harmonic = 1.00

    for i in range(2, number + 1) :
        harmonic += 1 / i
 
    return harmonic


print("Enter a number:")
number = int(input())
print(round(nthHarmonic(number),2))