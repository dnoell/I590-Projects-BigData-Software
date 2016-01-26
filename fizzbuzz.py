import sys

def fizzbuzz(n):

     for i in range(0,n):
          num = i + 1
          if num % 2 == 0 and num % 3 == 0:
               print '%d. fizzbuzz' % (num)
          elif num % 2 == 0:
               print '%d. fizz' % (num)
          elif num  % 3  == 0:
               print '%d. buzz' % (num)
          else:
               print '%d.' % (num)

if __name__ == '__main__':
     n = int(sys.argv[1])
     fizzbuzz(n)	
