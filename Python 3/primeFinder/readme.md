# primeFinder

**What it does**
This function finds any prime numbers between 3 and a given range. The highest prime it can detect is 993997. 

**How it works**
The function has a built-in list of all primes from 2 to 997. It then generates a list of all primes equal to or lower than the number being checked. This list of primes is then used to generate a new list containing the modulo result of the primes%number. Lastly the list of modulo results is checked for any entries of 0, and decided whether the number is a prime based on this information. Since a prime number is only divisible by 1 and itself, it will always leave something greater than 0 in modulo. 

*Any comments and feedback are greatly appreciated*
