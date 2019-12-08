import numpy as np
print(' ')

# Can read nx2 matrix form
xi = int(input("Enter number of rows: ")) 
yi = 2
print("Enter values in the matrix: ") 
# Must be exact values (e.g. twice number of row values)
  
R = list(map(int, input().split())) 
  
e = np.array(R).reshape(xi, yi) 
print(e) 
print(' ')
def Python3(e):
    for n in range(len(e)):
        a = np.polyfit(e[:,0], e[:,1],n)
        b = np.polyval(a, e[:,0])
        c = np.linalg.norm(e[:,1] - b)
        x = [n,c]

#Check loop
        if n==0:    
            y = x    
        elif y[1] >= x[1]:    
            c = x[0]
            
    c = np.polyfit(e[:,0],e[:,1],c)
    print('Coefficients: ', c)
Python3(e)
