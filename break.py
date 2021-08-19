#breqak and continue
"""the magic number is 45""" 
print("#########################################################################################\n")

print("!!!!!!!!!!!!!!!!!! GUESS THE NUMBER !!!!!!!!!!!!!!!!!!\n")
print("Rule : 1) NO of Attempt only 5\n")
print("#########################################################################################\n")
guess_fixed =45


i=0
while(True):
    i=i+1
    guess = int(input("give value : "))
    if guess <guess_fixed:
        print("guess value is gretter....")
    elif(i>=5):
        
        print("Sorry your attempt limit is over!!!!!")
        break
        
    elif(guess>guess_fixed):
        print("guess value is smaller .....")
        
    elif(guess==guess_fixed):
        print("Congratulation !!!!! Your guess value is correct")
        print("No of attemt is : ",i)
        break
    
       
    
    else:
        print("invalid input")  
        
    
# To see magic number see doc string
#print(__doc__)
   
    
        
