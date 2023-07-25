
<h1>Python Password Generator</h1>
<br/>
<h2>Description</h2>
In this project, I demonstrate fundamental programming concepts by creating a password generator using Python.
<br />

<h2>Program walk-through:</h2>
1. Import the 'secrets' and 'string' modules. These modules are built into python and only require you to type 'import' (see image below).<br />
<br />
2. Define the alphabet. The alphebet is the pool of possible characters that we will be pulling from. 'string.ascii_letters' = all lowercase and upercase letters, 'string.digits' = '0123456789', 'string.punctuation' = all special characters. <br />
<br />
3. Ask the user how long they want the password to be. For this we use the 'input' function. By default, whatever the user inputs will be saved as a string. However, for our program to work, we need the input to be saved as an integer. To achieve this, we simply add 'int' before the input function. <br />
<br />
4. Generate random password while meeting constraints. This portion of the code randomly selects a character out of the string 'alphabet' and appends it to the end of 'the variable 'pwd'. The loop runs infinitely until all of our conditions are met (password must contain atleast 1 special character and 2 numbers. Once all conditions are met, 'break' will break the loop and print the password! :) <br />

<p align="center">
<img src="https://i.imgur.com/Jl2RvLf.png" height="80%" width="80%"/>
<br />
<br />
