
def fizzBuzz(a):
    if (a%3==0 and a%5==0):
        return 'FizzBuzz'
    elif a%3==0:
        return 'Fizz'
    elif a%5==0:
        return 'Buzz'
    else:
        return 'Not a Fizz-buzz number'

print(fizzBuzz(int(input('Enput a number: '))))