def primeFinder(num):
    import math
    #This function divides a given number with all primes lower than the square root of the number. 
    #It then checks the modulo result of the primes%number for any 0s, and if none are found the number is a prime.
    
    #A list containing all prime in the range
    primeListResult = [2]
    
    #A list containing all primes from 2 to 1000.
    primeListMaster = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    
    #A list of primes lower than the square root of the number we're checking
    primeListLocal = []
    
    #A list containing the results of the modulo result of our number divided by each prime lower than the number's square root
    moduloResultLocal = []
    
    
    for i in range(3,num,2):
        if i in primeListMaster:
            pass
        
        else:
        iSqrt = math.sqrt(i)
        
        #build a list of all primes equal to or lower than the square root of i
        for prime in primeListMaster:
            if prime<=iSqrt:
                primeListLocal.append(prime)
                
            else:
                break
        
        #Build a list of the modulo result of i%p
        for primeLocal in primeListLocal:
            moduloResultLocal.append(i%primeLocal)
            
        #Check if there are any modulo results that are integers
        if 0 in moduloResultLocal:
            moduloResultLocal = []
            primeListLocal = []
        
        else:
            primeListResult.append(i)
            moduloResultLocal = []
            primeListLocal = []
            
            #Experimental which would allow the function to generate any prime number (in theory)
            if i > primeListMaster[-1]:
                primeListMaster.append(i)
            else:
                pass
         
        
           
            
    return print('The amoumt of primes between 2 and {} are {}. Here is the full list of prime numbers:\n{}'.format(num, len(primeListResult), primeListResult))
            
                
