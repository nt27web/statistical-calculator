[![Build Status](https://travis-ci.com/nt27web/statistical-calculator.svg?branch=main)](https://travis-ci.com/github/nt27web/statistical-calculator)

# Statistical-calculator

## Task list
No. |Task | Short Description | Developer 
------- | --------------- | ---------- | ----------- | 
1| Class Diagram | An outline showing how each of the statistical and calculator functions relates to each other | Nayana 
2| Connect Travis-CI with Github repo | Configure automation testing on all branches using Travis | Nayana
3| Project management board | Development task breakdown to the function level | Nayana
4| Baseline the Basic Calculator functions | Addition, Subtraction, Division, Multiplication, Square, Square Root | Nayana 
5| Descriptive Statistics functions | Functions- mean, median, mode, standard Deviation, Z-Score | Sourav
6| Population Sampling | Simple random sampling, Confidence Interval For a Sample, Margin of Error, Cochran’s Sample Size Formula, How to Find a Sample Size Given a Confidence Interval and Width (unknown population standard deviation) | Nayana
7| Random Generator | Generate a random number without a seed between a range of two numbers, Generate a random number with a seed between a range of two numbers, Generate a list of N random numbers with a seed and between a range of numbers, Select a random item from a list, Set a seed and randomly. select the same value from a list, Select N number of items from a list without a seed, Select N number of items from a list with a seed | Nayana
8| Readme | Task breakdown, description, formulas and result | Nayana, Sourav

## Function list
No. | Function | Short Description  Formula | Example | Result 
------- | --------------- | ---------- | ----------- | ----------- | 
1 | Addition | a + b | 12+3 | 15
2 | Subtraction| b-a | 13-2 | 11
3 | Multiplication| a * b |5 * 2 | 10
4 | Division | b/a | 12/4 | 3
5 | Square | a * a | 5 * 5 | 25
6 | Sqaure Root | math.sqrt(a)| math.sqrt(635)| 25.19920633
7 | Mean | sum(data)/len(data)| 15/3 |data=[1,2,3,4,5] Result = 3
8 | Median |  ((n + 1)/2)th (even number of elements) (((n+1)/2) -1)(odd number of elements), n is len(data)| (5+1)/2 |odd:data=[1,2,3,4,5] Result = 3,even:[1,2,3,4,5,6] Result = 3.5 
9 | Mode | max(frequency) Mode is calculated by counting the frequencies of an element in a list and calculating the max of all frequencies. | max(2,3,1,1,1,1,1) |data=[1,2,5,1,2,3,6,2,9,10,2] Result = 2(count 3)
10 | Variance | s=((sum(x-x")* * 2/len(data-1))|((sum(data[i]-mean(data))* * 2/len(data)-1)| data=[1,2,3,4,5] Result = 2
11 | Standard deviation | sqrt(variance) | sqrt(2) | data=[1,2,3,4,5] Result = 1.414
12 | z_score | z=(data[i]-mean(data))/standard deviation | z=(1-3)/1.414 |data=[1,2,3,4,5] -1.414


## Class Diagram of Statistics, Calculator and related classes 
<object data="Diagram_Nayana.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="Diagram_Nayana.pdf">
        <p>Click here to veiw/download the class diagram in PDF format: <a href="Diagram_Nayana.pdf">Class Diagram</a>.</p>
    </embed>
</object>



