[![Build Status](https://travis-ci.com/nt27web/statistical-calculator.svg?branch=main)](https://travis-ci.com/github/nt27web/statistical-calculator)

# Statistical-calculator

## Task list
No. |Task | Short Description | Developer 
------- | --------------- | ---------- | ----------- | 
1| Class Diagram | An outline showing how each of the statistical and calculator functions relates to each other | Nayana 
2| Connect Travis-CI with Github repo | Configure automation testing on all branches using Travis | Nayana
3| Project management board | Development task breakdown to the function level | Nayana
4| Baseline the Basic Calculator functions | Addition, Subtraction, Division, Multiplication, Square, Square Root | Nayana, Sourav
5| Descriptive Statistics functions | Functions- mean, median, mode, standard Deviation, Z-Score | Sourav
6| Population Sampling | Simple random sampling, Confidence Interval For a Sample, Margin of Error, Cochran’s Sample Size Formula, How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation) | Nayana
7| Random Generator | Generate a random number without a seed between a range of two numbers, Generate a random number with a seed between a range of two numbers, Generate a list of N random numbers with a seed and between a range of numbers, Select a random item from a list, Set a seed and randomly. select the same value from a list, Select N number of items from a list without a seed, Select N number of items from a list with a seed | Nayana
8| Readme | Task breakdown, description, formulas and result | Nayana

## Function list
No. | Function | Short Description  Formula | Example | Result 
------- | --------------- | ---------- | ----------- | ----------- | 
1 | Addition | float(a) + float(b) | float(12)+float(3) | 15
2 | Subtraction| float(b)-float(a) | float(13)-float(2) | 11
3 | Multiplication| float(a) * float(b) |float(5)* float(2) | 10
4 | Division | float(b)/float(a) | float(12)/float(4) | 3
5 | Square | float(a)* float(a) | float(5)* float(5) |25
6 | Sqaureroot | round(math.sqrt(float(a)), 8)| math.sqrt(635)| 25.19920633
data=[1,2,3,4,5]
7 | Mean | sum(data)/len(data)| 15/3 | 3
8 | Median |  {(n + 1) ÷ 2}th , n is len(data)| (5+1)/2 | 3
data=[1,2,5,1,2,3,6,2,9,10,2]
9 | Mode | max(data.count) | max(data.count) | 2
data=[1,2,3,4,5]
10 | Variance | s=((sum(x-x")* * 2/len(data))|((sum(data[i]-mean(data))* * 2/len(data))| 2
11 | Standard deviation | sqrt(variance) | sqrt(2) | 1.414
data=[1,2,3,4,5]
12 | z_score | z=(data[i]-mean(data))/standard deviation | z=(1-3)/1.414 | -1.414



