import math

# http://www.shafaetsplanet.com/planetcoding/?p=624

status = []
def siv(n):
    n = n + 1
    status = [False for i in range(n)]
    
    for i in range(4,n,2):
        status[i] = True
        
    for i in range(3,n,2):
        if status[i] == False:
            for j in range(i*i,n,i):
                status[j] = True
 
    return status

if __name__=='__main__':
    n = 50
    status = siv(n)

    for i in range(2,len(status)):
        if(status[i] == False):
            print(i)

# for i in range(status.len):
#     print(status[i])