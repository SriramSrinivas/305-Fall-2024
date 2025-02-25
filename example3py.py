grade=int(input('Enter score between (0-100)'))
if grade>89:
    print('Grade:A')
if grade>79 and grade <=90:
    print('Grade:B')
if grade>69 and grade<80:
    print('Grade:C')
if grade <70:
    print('Grade:F')