# Python3 implementation to find the 
# number of ways to place two 
# queens on the N * N chess board 
import math 
  
# Function to find number of valid 
# positions for two queens in the 
# N * N chess board 
def possiblePositions(n): 
      
    term1 = pow(n, 4); 
    term2 = pow(n, 3); 
    term3 = pow(n, 2); 
    term4 = n / 3; 
      
    ans = ((math.ceil(term1)) / 2 - 
           (math.ceil(5 * term2)) / 3 + 
           (math.ceil(3 * term3)) / 2 - term4); 
             
    return ans; 
  
# Driver code 
if __name__ == '__main__': 
      
    n = int(input())
  
    # Function call
    ans = possiblePositions(n) 
      
    print(int(ans)) 
#https://www.geeksforgeeks.org/number-of-ways-to-place-two-queens-on-a-nn-chess-board/