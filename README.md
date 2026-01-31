# Algos-HW-1-Matching-and-Verifying

## Students
-  Joshua Labasbas: 3766-3960
-  Asha Miller: 2619-5990

## Instructions
In order to generate a random preference list with hospitals and students of *n*, run the following:
```
cd data
python generate.py [n]
```

Then to run the matcher:

```
cd src
python matcher.py [n]
```

Then to check:
```
cd src
python checker.py [n]
```

In all the above [n] is to be replaced with the desired n

## Assumptions

We assume that the preference list fits the described format, with the first line being n, and the next n lines is the preference list for hospitals, and the next n lines are the preference lists for the students.
Then we assume that all preference lists and matchings are done using numbers to label the students/hospitals. Additionally, we assume that there are n hospitals and n students, essentially that number of hospitals = number 
of students.

## Graph

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/88fe8b7d-94d2-46f3-8d10-ed8a433d20a0" />

Figure 1: Scatter Line Graph measuring the runtime of matcher.py with respect to the input size

<img width="752" height="452" alt="image" src="https://github.com/user-attachments/assets/a33217ae-93c5-4b20-bcb1-fe499c5c3587" />

Figure 2: Scatter Line Graph measuring the runtime of checker.py with respect to the input size



From these two graphs, the trend exhibited by both is that runtime increases exponentially as input size increases. 
This exponential runtime scaling is consistent with the G-S algorithm's O(n^2) time complexity.
