Age = int(input('kindly tell us your age in years:'))

Max_Heart_Rate = 220-Age
print('your maximum heart rate is',Max_Heart_Rate)


target1 = 0.5 * Max_Heart_Rate
target2 = 0.85 * Max_Heart_Rate

range = (0.85 * Max_Heart_Rate) - (0.5 * Max_Heart_Rate)
print('range of your target heart rate is','%.0f'%range)