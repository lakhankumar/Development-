import random
    
def gamblerProblem():
     """
    Description:
        This function Simulates a gambler who start with stake and place fair 1 bets until
        he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
        times he/she wins and the number of bets he/she makes. Run the experiment N
        times, averages the results, print the results.
    """

stake=int(input("Enter The The Stake Amount:"))
goal=int(input("Enter The Amount You Want To Win:"))
bet_made=int(input("Enter The The Number Of Bets You Want To Make:"))
no_of_times_won=0
no_of_time_lost=0
no_of_bets_made=0

while(stake >= 0 and stake <= goal and no_of_bets_made < bet_made):
        no_of_bets_made+=1
        gambler_choice=random.randint(0, 1)  #generates a random number 0 or 1
        
        if gambler_choice==0:   #if the random number generated is 0
            no_of_times_won+=1
            stake=stake+1 
        else:
            no_of_time_lost+=1
            stake=stake-1

print("Number Of Times Won",no_of_times_won)
print("Percentage Of Win", (no_of_times_won/bet_made)*100) 
print("Percentage Of Loss", (no_of_time_lost/bet_made)*100)
print("Number Of Bets Made", no_of_bets_made) 
    
gamblerProblem()