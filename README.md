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
