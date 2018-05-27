import random
# this code randomly tries different numbers and checks if it corresponds with the password.#
while True:
   PassWord=input("Enter any four-digit code(has to be an numerical value): ")
   #here is where the password you wrote is stored...#
   Trial=""
   while Trial!=PassWord:
      # if the variable "Trial isn't equal to "PassWord" then # is a rough translation of what that means.
       Trial=str(random.randint(0,9999))
       # here is where we choose the range of random numbers it needs to draw from #
       if Trial==PassWord:
           print('The password is: '+PassWord)
