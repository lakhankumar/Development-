import random

def distinct_coupons():
  """
    Description:
        This function is used to generate random and unique coupon numbers.
        User input is given for number and range of coupon numbers.
        Random fuction is used to generate random coupon numbers.
    
    """         
coupon = []   #empty list
random_numbers=0  #no.of random numbers needed to generate distinct coupons
try:
            number=int(input("Enter The Number Of Coupons You Want To Generate: "))
            print("Distinct Coupon Numbers Generated")
            for element in range(number):
                coupon_number = random.randint(10,100)
                if coupon_number not in coupon:
                    coupon.append(coupon_number)  #adding the distinct random number gnerated to list 
                    print(coupon_number)
                    random_numbers+=1
            else:
                pass           
            print("Total Random Numbers Needed To Get All Distinct Numbers:",end = " ")
            print(random_numbers,end = " ")
except Exception as err:
            print("Not A Valid Number",err)
distinct_coupons() 