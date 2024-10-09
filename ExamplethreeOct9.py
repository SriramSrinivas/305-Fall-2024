lower=int(input('Enter Lower bound:'))
upper=int(input('Enter Upper bound:'))
theSum=0
for number in range(lower,upper+1):
    theSum=theSum+number
print('Output:',theSum)