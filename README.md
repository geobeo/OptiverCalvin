# OptiverCalvin

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
But his approach is a bit different (uses random generators to randomly guess route-length). 

I think my approach is better. Better because in his approach the answer is always different and may or may not deviate significantly from the statistically average, minimum and maximum possible values. My approach (hopefully) takes into account the equal probability distribution of the chance of the signal being red or green upon arrival as well as the amount of seconds until the signal changes after arrival. The answers of my script are always the same giving the same input parameters and it gives a range of possible waiting times: minimum, maximum and average waiting time... 
"""
