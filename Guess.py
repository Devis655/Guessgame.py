import random
def guessnum():
   num = random.randint(1,99)
   guess = int(input('Enter your guess: '))
   chance = 0

   while guess!=num:
     if guess<num:
      print('Your guess is too low')
     if guess>num:
      print('Your guess is too high ')

     chance=chance+1
     guess = int(input('Enter your guess: '))


   print(f'Bingo!!! You guessd in {chance} chances')

guessnum()