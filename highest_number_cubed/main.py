"""This is the entry point of the program."""
def highest_number_cubed(limit):
    answer= 0
    while answer**3 < limit:
        answer+=1
    else:
        return answer - 1

        
        
        
