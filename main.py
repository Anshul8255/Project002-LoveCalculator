print("Love calculator")
word1 = input('What is the 1st name ')
word2 = input('What is the 2nd name ')
sum = word1 + word2
sum_lowered = sum.lower()
#TRUE
t = sum_lowered.count('t')
r = sum_lowered.count('r')
u = sum_lowered.count('u')
e = sum_lowered.count('e')
#LOVE
l = sum_lowered.count('l')
o = sum_lowered.count('o')
v = sum_lowered.count('v')
e = sum_lowered.count('e')

true = t + r + u + e
love = l + o + v + e
uk = str(true)
uk2 = str(love)
print("Your love compatibility is :- ")
print(true + love + "%")