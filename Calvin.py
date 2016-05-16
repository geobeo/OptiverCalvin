"""
Algo written by Georges Meinders @ www.megahard.pro
email: g@megahard.pro 

This is a challenge that was posted on Optiver's website for a job vacancy.
I wrote this for fun and this hasn't been submitted by me to Optiver nor has 
it been checked for correctness. 
http://optiver.com/amsterdam/careers/job-vacancies/details/5341/Junior-Researcher

It tries to solve the following challenge: 
Calvin has to cross several signals when he walks from his home to school. Each of these signals operate independently. They alternate every 80 seconds between green light and red light. At each signal, there is a counter display that tells him how long it will be before the current signal light changes. Calvin has a magic wand which lets him turn a signal from red to green instantaneously. However, this wand comes with limited battery life, so he can use it only for a specified number of times.
a. If the total number of signals is 2 and Calvin can use his magic wand only once, then what is the expected waiting time at the signals when Calvin optimally walks from his home to school?
b. What if the number of signals is 3 and Calvin can use his magic wand only once?
c. Can you write a code that takes as inputs the number of signals and the number of times Calvin can use his magic wand, and outputs the expected waiting time?

=============

To use this code: 
1. Install Python
2. Run this script in any console by typing "python calvin.py"

============

Another guy solved this problem in Java here: http://adaminamsterdam.com/page/06032016/06032016.html
But his approach is a bit different (uses random generators to randomly guess route-length). I think my approach is better :P
"""

def getResult(NrOfSignals, NrOfWands):
	
	# minimum waiting time. This assumes Calvin arrives exactly at each signal when it jumps to green and/or has enough wands to skip all signals.
	minWaitTime = 0 
	
	#the amount of signals Calvin can not use a wand for
	netSignals = (NrOfSignals - NrOfWands)
	
	#when Calvin can use as many wands as there are signals
	if netSignals < 0:
		maxWaitTime = 0
		avgWaitTime = 0
	else:
		maxWaitTime = (netSignals * 80)  
		avgWaitTime = (netSignals * 40)
	
	print("")
	print("------- The solution ------")
	print(" ==> Assumptions: ")
	print("1. Calvin always only uses the wand at or before half of the waiting time (40 seconds) elapsed, that way he optimizes the probability of saving the maximum amount of time possible at each signal. He does this as long as the remaining number of signals is less than the remaining amount of wand-uses. If the amount of wand-uses equals the amount of remaining singals, he will just  use his wand at every remaining signal.")
	print("2. The time Calvin needs to interpret the signal, react and take action is assumed to be 0 seconds.")
	print(" ==> Answer: ")
	print("The expected waiting time for Calvin is between: " + str(minWaitTime) + " seconds (in the rare case all signals turn green as he arrives at each signal) and " + str(maxWaitTime) + " seconds in the worse case.")
	print("The average time he'll have to wait at all signals on his way home will be around " + str(avgWaitTime) + " seconds")
	
def UIgetNrOf(SignOrWand):
	
	print("--------")
	
	if SignOrWand == 'Signals': 
		print("Enter the amount of signals Calvin will encounter on his path.")
	elif SignOrWand == 'Wands':
		print("Enter the number of times Calvin may use a wand during his trip from home to school.")
		
	print("The number entered should be between 0 and 10000")
	# Get input from console.
	UserInput = input()
	
	try:
		#check whether user input is integer
		val = int(UserInput)
		#check input range
		if not ((val < 0) or (val > 10000)):
			return val; 
		else:
			print("The value entered by you was: " + str(val))
			print("That was not a value between 0 and 10000. Try again.")
			#no valid input range. try again:
			return UIgetNrOf(SignOrWand) 
	except ValueError:
		print("The value entered by you was: " + str(UserInput))
		print("That was not an integer number between 0 and 10000. Please enter integer numbers only. Try again.")
		#Value was not an integer. try again:
		return UIgetNrOf(SignOrWand)
		

#################
# Script start: 
#################	
print("Welcome to Calvin's puzzle solver by Georges Meinders. mail: g@megahard.pro")

#get number of Signals from user
NrOfSignals = UIgetNrOf('Signals')

#get number of times Calvin can use Wand from user
NrOfWands = UIgetNrOf('Wands')

#calculate and display result to user
getResult(NrOfSignals, NrOfWands)

