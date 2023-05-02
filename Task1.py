# This is a sample Python script.
#test code for all cases to put in functions
#first case
string= "abracadabra"  #intialize the string
l = list(string) #use other character to path the
l[5] = 'k' #add the character in position number 5
string = '\t'.join(l) #use join to add it the list and '\t' to make space
print (string) #the output

#second code
string= "abracadabra" #intialize the string
string = string[:5] + 'k' + string [5:] #trying another way to add the character by using + it is a concatenate type
print (string) #the output

#task solution
#we will put the last code in tow different functions
#first function will have the first option
def function (string='abracadabra', position=5, character='k'): #intilize the function

    task = list(string)  # use other character to path the
    task[position] = character  # add the character in position number 5
    string = '\t'.join(task)  # use join to add it the list and '\t' to make space
    print(string)  # the output
    #i have faced error bcause i ddidn't call the function or put exit code
function()#exit code


#second function
#in the second function we will use the other option to solve this task
def function(string='abracadabra',position=5,character='k'):#intilize the function
    string = string[:position] + character + string[position:] #trying another way to add the character by using + it is a concatenate type
    print(string) #the output
    # i have faced error bcause i ddidn't call the function or put exit code
function()#exit code
