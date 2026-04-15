class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True 

        if n <= 0 or n % 2 != 0:
            return False

        return self.isPowerOfTwo(n/2)



    def isPowerOfTwo_simple(self, n: int) -> bool:
        return (n > 0) and n & (n-1) == 0

    def isPowerOfTwo_only1(self, n: int) -> bool:
        count = 0        
        for i in range(32):
            if (n & (1 << i)):
                if count > 1:
                    return False
                count += 1
        if count == 1:       
            return True

        return False

            
    def isPowerOfTwo_modular(self, n: int) -> bool:
        if n <= 0:
            return False

        while n != 1 :
            if n % 2 == 0:
                n = n//2  
            else:
                return False          

        return True
               

               
        