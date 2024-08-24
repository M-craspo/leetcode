class Solution(object):
    def fizzBuzz(self, n):
        out=[]
        for i in range(n):
            if (i+1)%3==0 and (i+1)%5==0:
                out.append('FizzBuzz')
            elif (i+1)%3==0:
                out.append('Fizz')
            elif (i+1)%5==0:
                out.append('Buzz')
            else:
                out.append(str(i+1))
        return out