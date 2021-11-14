from math import floor

'''
Calculate the sum of natural numbers from 1 to n
'''
def sum_1_n(n: int) -> int:
    return n*(n+1)/2

'''
Calculate the sum of multiples of x from 1 to n
'''
def sum_x_mults_n(x: int, n: int) -> int:
    k_x = floor((n-1)/x)
    return x*sum_1_n(k_x)

'''
Calculate the sum of multiples of x and y from 1 to n
'''
def sum_xy_mults_n(x: int, y: int, n: int) -> int:  
    return int(sum_x_mults_n(x,n) + sum_x_mults_n(y,n) - sum_x_mults_n(x*y,n))

'''
Driver code
'''
if __name__ == "__main__":
    x = int(input("Enter a value for x: "))
    y = int(input("Enter a value for y: "))
    n = int(input("Enter the upper bound of the range: "))
    print(sum_xy_mults_n(x,y,n))
