# CAP4630_Project_1

Project 1 
Assignment Overview 
In this assignment you will implement two games using the easyAI framework: 
http://zulko.github.io/easyAI/  
Project Specification  
This is a group assignment.  
 
Students are encouraged (but not required) to work in groups of max 3 students. No exceptions. 
 
Ideally, the group should be organized around three main tasks / duties: 
- Design of the solution (“architect” role) 
- Coding of the solution (“developer” role) 
- Documentation of the solution (“reporter” role) 
 
You are required to indicate in your report “who did what” and document the entire process, from 
sketching the original plans and dividing up the tasks all the way to polishing the interface, testing 
the solution, and preparing the report. 
 
The basic functionality for each part is specified below. 
 
Part 1 – Setup (10%) 
 
1. Python installation and configuration 
You can use either method, but method (2) is preferred. 
 
(1) Using pip (recommended method) 
i. Download python for your operating system (OS), see here1 
ii. Installed downloaded file to your OS. 
iii. Validate that you have python install make sure that you have python by 
running the following command below. 
python --version 
      It will print current version of your python interpreter.  
iv. Install pip with python, see here2 
python -m pip install --upgrade pip  
v. Validate that you have pip install make sure that you have pip by running the 
following command below 
python -m pip --version  
 
 1 https://www.python.org/downloads/ 2 https:// pip.pypa.io/en/stable/installation/ 
(2) Using Conda 
a. Download conda for you operating system, see here3 
b. Open terminal and check that conda is installed.  
Note: if you use Windows, you must search for “Anaconda Prompt” 
c. Create conda environment create conda environment and install python version 
3.8 (you can use any python version that is compatible with easyAI).  
conda create -n py38 python=3.8 
d. Activate conda environment 
conda activate py38 
e. Check that your conda environment is activated.  
There are many ways to check. One way is to run the following command. 
conda info --envs 
 
 
2. EasyAI installation 
Follow instructions in the easyAI GitHub repo: https://github.com/Zulko/easyAI  
 
sudo python -m pip install easyAI 
 
Part 2: Run tic-tac-toe and connect-four example presented in easyAI documentation (40%) 
 
Note that code in the easyAI documentation has typos. Github links for both games are pasted below 
Tic-Tac-Toe and Connect Four:  https://github.com/Awannaphasch2016/easy-ai-examples-fixed  
 
 
Part3: Implement a modified version of the game of checkers (50%) 
 
In this part you will implement a two-player game based on the game of Checkers. See references 
for implementation from the examples given in Easy AI, here. 
 
 
 3 https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html 
 
 
Objective: 
The objective of the game is to get as many pieces as you can from the opponent. 
 
Material  
An 8 x 8 board of checkers is used with two colors one for each opponent. 
 
How to Win 
The game can be won when the opponent is unable to make a move. This can be done in two ways: 
The entirety of a player’s pieces was captured by the opponent (when the piece is a King)  
 
Additional Rules  
1. Only one jump is possible per move. 
2. Forward move is only allowed for each opponent. 
3. When a player jumps over another opponent’s piece, the piece is not removed by the 
opponent. 
4. There are two types of moves Step or Jump. 
5. The pieces always move diagonally only on dark colored squares. 
6. When a player’s piece reaches the last row on the opponent’s side of the board, they can use 
one of their captured pieces to crown the piece as a king. 
7. The first player who has a piece promoted to king wins immediately.  
 
Implement the following functions: 
 
See starter code at 
https://github.com/Awannaphasch2016/checker_easyAI/blob/main/checker_questions.py  
and complete the code for the functions (12.5 pts each): 
• make_move() 
• lose() 
• is_over()  
• scoring() 
 
 
