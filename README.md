# NIH-Project-NLP

There are two python code file. 

The first file titled "newCode.py" takes the question file and generate a text file titled selectedDep.txt at the specified location mentioned in the code.
the selectedDep file contains the questions with only required 13 dependencies. 


the second file "newCodeSim.py" reads the selectedDep.txt file and generates the fScore.txt file at the end and replace the file, if it already exists.

( The reason to separate the file, as I was running the code again and again, I don’t want the code to reproduce the parsed data using parser again and again.)


The similarity is checked using Option1 of your algorithm.
and in the fScore file, there are three columns. 
The code takes one input question and matches it with all other questions including itself.

and the columns are showing, the first question and the second column showing the number of second matching question and the third column is showing the similarity score.

if you see the fScore file, it shows that question 1 similarity with question1 is 1.5
if I check with algo; its right as the match score is 15, and the length of the tuples of question 1 is 5. so it gives 1.5. You can also check the file 'selectedDep.txt' for cross- check.

If you have to run the code on any other file. 
First, you will run the code file "newCode.py" and change the paths where you want read and store the files. I have mentioned the paths at the start of the code. 

it will create the selectedDep.txt file at your desired location.

Then you will run the second code file. and all you have to change the count variable value, as I worked on 10 questions.

it is bit more efficient because I am not separating the dependencies and creating files for each of them. Now, I am directly matching from the parsed data, its just that I extracted the desired data(i.e. of 13 dependencies). 

