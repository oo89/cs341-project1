# project1 Oscar Ojeda 

CS341


## SET UP 
1. Create 

##Overview
We define the language L to consist of strings that represent certain email addresses
(specified below). For this assignment you are to design a DFA to recognize L and write
a program that implements your DFA.

## The Language L 
To precisely specify L, first define Γ = {a, b, c, . . . , z} as the set of lower-case Roman
letters. Also, define ∆ = {.} and Φ = {@}, and let Σ = Γ ∪∆∪ Φ; i.e., Σ is the set
consisting of all the lower-case Roman letters, the dot (or period), and the @ symbol.
Define the following sets of strings:

1. S1 = ΓΓ∗, which consists of strings over Γ of length one or more
2. S2 = ∆ΓΓ∗, which consists of strings starting with a dot and followed by one or
more symbols from Γ
3. S3 = {.net} 

##Then we define the following sets of strings over Σ:
1. L1 = S1ΦS1S3
2. L2 = S1S∗2ΦS1S∗2S3
3. L = L1 ∪ L2

Strings in L1 and L2 are (subsets of) email addresses. For example, the string
abc@njit.net belongs to L1. The strings abc@njit.net, abc.def@cs.njit.net, and
abc.def.g@a.b.cs.njit.net are in L2.
The specification of L does not include all valid email addresses because we included
several restrictions to simplify the assignment. For example, only lower-case Roman
letters, dots, and the @ symbol are allowed, strings in L must end with .net, etc.

##DFA for L
First construct a DFA M = (Q, Σ, δ, q1, F) that recognizes L. The DFA must satisfy
each of the following properties:
 The DFA must be defined with the above alphabet Σ. Your DFA does not have
to handle symbols that are not in Σ.
 The states in the DFA must be labeled q1, q2, q3, . . . , qn, where q1 is the start
state and n is the number of states in the DFA. (It is also acceptable for the states
to be labeled q0, q1, . . . , qn−1, with q0 the start state.)
You will lose points if your DFA is overly complicated (e.g., having more states than
necessary). To simplify your DFA drawing, you may omit any edges going from any
state q to a “trap state” (i.e., a non-accepting state from which the DFA can never
leave). All other edges must be included in your drawing. Clearly identify which state
is the trap state in the drawing of your DFA, and your drawing should include a note
stating that all edges not specified go to a trap state. Also, to simplify your drawing, you
should define Γ−ℓ = Γ − {ℓ} for any symbol ℓ ∈ Γ; i.e., Γ−ℓ is the set of all lower-case
Roman letters except for ℓ. For example, Γ−e = {a, b, c, d, f, g, . . . , z}, so your DFA
might include something like the following:

qi - e -> qj 
qi - Γ-e -> qk

Thus, if the DFA is currently in state qi, then it moves to qj on reading e, and it moves
to state qk on reading any other lower-case Roman letter. You could also define the
notation Γ−a,b = Γ − {a, b}.

##Program Specifications
You must write your program in either C, C++, Java, or Python. All input/output
must be through standard input/output, and your program is to work as follows:
1. Your program first prints:
 
Project 1 for CS 341
Section number: the section number you are enrolled in
Semester: Spring 2021
Written by: your first and last name, your NJIT UCID
Instructor: Marvin Nakayama, marvin@njit.edu

2. Your program next asks the user if they want to enter a string. The user then
enters “y” for “yes”, or “n” for “no”.
-If the user enters “n”, then the program terminates.
-If the user enters “y”, then the user is prompted to enter a string over Σ.

3. If the user chooses to input a string, your program then reads in the string. After
reading in the string, your program prints it. Then your program processes the
entire string on the DFA, one character at a time, in the following manner.
- Your program must begin in the start state of the DFA and print out the
name of that state (q1 or q0).
- After each character from the string is processed on the DFA, your program
must print out the character and the name of the current state of the DFA.
Even if your DFA is in a trap state, your program must do this for each
character in the string until it reaches the end of the string.

To simplify your program, you can check the ASCII code of each character of the
string and process on the DFA accordingly.

4. After processing the entire string on the DFA, your program must indicate if the
string is accepted or rejected based on the state in which the DFA ended. Your
program then should return to step 2.

##Test Cases

Test your program on each of the following input strings:
1. foo@abcdef.net
2. z@n.net
3. ba@ba.ne
4. edfg@.net
5. webweb.ab.c.net@cs.defgh.net
6. foo@goo.net..net
7. abqe.@boom.net
8. educ@netw.netw
9. redblue@green..net
10. random@net
11. poke@a.net.net
12. www@net.nett
13. wwwb@net.ne
14. www.net@bbdef.net
15. food@for.net@
16. net@network.ne.net
17. network@network.net.ne
18. @abcde.net
19. people.dog.cat@.net
20. cable..cord@fort.net

You must create an output file containing your program’s output from each test case
in the order above.

##Deliverables

You must submit all of the following through Canvas by the due date/time given on
the first page:

1. A Microsoft Word document stating, “I certify that I have not violated the University Policy on Academic Integrity”, followed by your first and last name, NJIT
student ID, and UCID. If you do not include this pledge, then you will receive a
0 on the assignment. Anyone caught violating the University Policy on Academic
Integrity will be reported to the dean of students.
2. A drawing of the DFA for L that your program implements. This format of the
file must be either Microsoft Word, pdf, or jpeg (e.g., a photo from your phone’s
camera, but make sure it’s not blurry). The file must be smaller than 5MB in size.

3. A Microsoft Word document giving the 5-tuple specification for DFA as
M = (Q, Σ, δ, q0, F) or M = (Q, Σ, δ, q1, F),

depending on whether your DFA’s start state is q0 or q1. You must explicitly give
each of the elements in the 5-tuple, e.g., Q must be a set with all of the states in
your DFA. Give the transition function δ : Q×Σ → Q as a table; e.g., see slide 1-8
of the lecture notes. Some transitions of your DFA will be taken on reading many
different symbols, so you can simplify the table by combining these possibilities
into a single column of the table. For example, in any state, your DFA on reading
y or z should always make the same transition, so you can combine these columns
in your table into a single column.

4. A single file of your source code, of type .c, .cpp, .java, or .py. Only submit
the source code; do not include any class files. You must name your file

p1_21s ucid.ext

where ucid is replaced by your NJIT UCID (which is typically your initials followed
by some digits) and .ext is the appropriate file extension for the programming
language you used, e.g., .java. The first few lines of your source code must be
comments that include your full name and UCID.

5. A single file containing the output from running your program on all of the test
cases, in the order given in Section 5 of this document. The output file must be
either .txt or in Microsoft Word.

##Hints
To design a DFA for L, start by drawing a DFA to handle only L1 and end in “.net”,
which includes the first three test cases. Initially include only the transitions that will
eventually lead to acceptance. Then modify your DFA to handle the rest of L and the
other test cases.

 


