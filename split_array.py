#split the given array into K sub-arrays such that the maximum sum of all the sub arrays is minimum
#given an Array of N elements and a number K, split the given array in K subarrays such that the maximum sum of all the sub# the maximum subarray sum achievable out of K subarrays formed, must be minimum possible
#find that possible subarray sum 
# -------------------------------------------------------------------------

#Function to check if mid can be max sub - arrays sum
def check(mid,array,n,K):
    count = 0
    sum = 0
    for i in range(n):
        #if individual element is greater than maximum possible sum 
        if (array[i] > mid):
            return False
        
        #incerase the sum of current sub - array 
        sum += array[i]
        
        #i the sum is greater than mid increase count
        if(sum>mid):
            count +=1
            sum = array[i]
    
    count +=1
    
    #check condition
    if (count <=K):
        return True
    return False

#Function to find maximum subarray sum which is minimum
def solve(array, n, K):
    start = max(array)
    end = 0
    
    for i in range(n):
        end += array[i]
        
    # Answer stores possible maximum sub array sum
    answer = 0
    while(start<= end):
        mid = (start+end) // 2
        
        #if mid is possible solution , then 
        #put answer = mid
        if (check(mid, array, n , K)):
            answer = mid
            end = mid - 1
        else:
            start = mid +1
            
    return answer

if __name__ == '__main__':
        array = [1,2,3,4]
        n = len(array)
        K = 3
        print(solve(array,n,K))

        
    