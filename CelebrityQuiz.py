#The calculator function recieves the score of the user, then returns their percent mark and how much of a fan the user is of the celebrity.
def calculator(total):
    percent = round((total/5)*100)
    if percent <= 20:
        return "Your score is " + str(percent) + "%\n" + "Do you even know who this celebrity is?"
    elif percent > 20 and percent <= 40:
        return "Your score is " + str(percent) + "%\n" + "You don't really know this celebrity..."
    elif percent > 40 and percent <= 60:
        return "Your score is " + str(percent) + "%\n" + "You are a regular fan of this celebrity."
    elif percent > 60 and percent <= 80:
        return "Your score is " + str(percent) + "%\n" + "You are an enthusiast of this celebrity!"  
    else:
        return "Your score is " + str(percent) + "%\n" + "You are a TRUE FAN of this celebrity."

#The score must be defined here so it can count each correct answer the user gets.
score = 0

print("Welcome to \nHow Much Are You a Fan of...?")

#The while loop is used to allow the user to repick a celebrity if they input the wrong number at first and allow the user to play again at the end.
while True:
    score=0
    print("\nHere are your celebrity choices: \n"
        +"1) Taylor Swift\n"
        +"2) Beyonce\n"
        +"3) Selena Gomez\n"
        +"4) Drake\n")
    celebrity = int(input("Input the number corresponding to your celebrity:"))
    print("")
    
    #This if condition checks if the user inputted a celebrity corresponding number, if not the user will be prompted to input again.
    if celebrity < 1 or celebrity > 4:
        print("Error. This number does not correspond to a celebrity.")
        continue
    else:
        #This if condition checks which of the 4 celebrities the user chose, to proceed with the right questions.
        if celebrity == 1:
            #This print statment makes the user aware of their selection, so they can decide in the would like to proceed.
            print("\nYou have selected Taylor Swift!")
            
            #This if condition asks the user if they want to proceed with their selection, if not then it brings them back to the options and selection process.
            check = input("Are you sure? Input Y to proceed or N to choose again.")
            if check == "N":
                continue
            
            else:
            #Questions: The program displays the questions, and answer options. Once the user answers the program checks if they were correct or not and updates the score.
                print("\nQuestion 1: What is Taylor Swift's Middle Name? \n"
                +"1) Rose\n"
                +"2) Alison\n"
                +"3) Jen\n"
                +"4) Sicily\n")
                ans1 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans1 == "2":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Alison. \n")
                    
                print("\nQuestion 2: What is Taylor Swift's Second Album? \n"
                    +"1) Evermore\n"
                    +"2) Folklore\n"
                    +"3) Red\n"
                    +"4) Fearless\n")
                ans2 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans2 == "4":
                    print("Correc.\n")
                    #when the user gets a correct answer 1 point is added their score 
                    score+=1
                else:
                    print("Incorrect. The correct answer is Fearless.\n")
                    
                print("\nQuestion 3: What is Taylor Swift's Mom's Name? \n"
                    +"1) Andrea\n"
                    +"2) Matilda\n"
                    +"3) Jess\n"
                    +"4) Taylor\n")
                ans3 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans3 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Andrea.\n")
                                        
                print("\nQuestion 4: What Year did Taylor Swift Release her First Album? \n"
                    +"1) 2006\n"
                    +"2) 2004\n"
                    +"3) 1989\n"
                    +"4) 2000\n")
                ans4 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans4 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 2006.\n")
                    
                print("\nQuestion 5: Where was Taylor Swift Born? \n"
                    +"1) Pennsylvania\n"
                    +"2) New York\n"
                    +"3) Canada\n"
                    +"4) Virginia\n")
                ans5 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans5 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Pennsylvania.\n")
                
                #The variable score counted how many questions the user got correct, it gets sent to the calculator function to determine the user's overall results.
                print(calculator(score))
                
                #The user has the option to play again or exit the program.
                again = input("\nWould you like to play again?\nInput Y to play again, N to exit the game.")
                if again == "Y":
                    #continue is used to take the code back to the start of the while loop
                    continue
                else:
                    print("Goodbye!")
                    
        elif celebrity == 2:
            #This print statment makes the user aware of their selection, so they can decide in the would like to proceed.
            print("You have selected Beyonce!")
            
            #This if condition asks the user if they want to proceed with their selection, if not then it brings them back to the options and selection process.
            check = input("Are you sure? Input Y to proceed or N to choose again.")
            if check == "N":
                continue
            
            else:
            #Questions: The program displays the questions, and answer options. Once the user answers the program checks if they were correct or not and updates the score.
                print("\nQuestion 1: What is Beyonce's Middle Name? \n"
                +"1) Giselle\n"
                +"2) Alison\n"
                +"3) Jen\n"
                +"4) Mia\n")
                ans1 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans1 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Giselle.\n")
                    
                print("\nQuestion 2: What Girl Group was Beyonce Formerly Part of? \n"
                    +"1) Maroon 5\n"
                    +"2) Destiny's Child\n"
                    +"3) Fifth Harmony\n"
                    +"4) No Group\n")
                ans2 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans2 == "2":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Destiny's Child.\n")
                    
                print("\nQuestion 3: What Year Was Beyonce Born in? \n"
                    +"1) 1981\n"
                    +"2) 1979\n"
                    +"3) 1989\n"
                    +"4) 2000\n")
                ans3 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans3 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 1981.\n")
                                        
                print("\nQuestion 4: Where Was Beyonce Born? \n"
                    +"1) Texas\n"
                    +"2) California\n"
                    +"3) Wisconsin\n"
                    +"4) Canada\n")
                ans4 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans4 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("lesson7.py\n")
                    
                print("\nQuestion 5: How Many Siblings Does Beyonce Have? \n"
                    +"1) 3\n"
                    +"2) 2\n"
                    +"3) 1\n"
                    +"4) 0\n")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                ans5 = input("Input the number corresponding to your answer:")
                if ans5 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 3.\n")
                
                #The variable score counted how many questions the user got correct, it gets sent to the calculator function to determine the user's overall results.
                print(calculator(score))
                
                #The user has the option to play again or exit the program.
                again = input("\nWould you like to play again?\nInput Y to play again, N to exit the game.")
                if again == "Y":
                    #continue is used to take the code back to the start of the while loop
                    continue
                else:
                    print("Goodbye!")
            
        elif celebrity == 3:
            #This print statment makes the user aware of their selection, so they can decide in the would like to proceed.
            print("You have selected Selena Gomez!")
            
            #This if condition asks the user if they want to proceed with their selection, if not then it brings them back to the options and selection process.
            check = input("Are you sure? Input Y to proceed or N to choose again.")
            if check == "N":
                continue
            
            else:
            #Questions: The program displays the questions, and answer options. Once the user answers the program checks if they were correct or not and updates the score.
                print("\nQuestion 1: What Show Did Selena Gomez NOT Appear on? \n"
                +"1) Wizards of Waverly Place\n"
                +"2) Hannah Montana\n"
                +"3) iCarly\n"
                +"4) Selena + Chef\n")
                ans1 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans1 == "3":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is iCarly.\n")
                    
                print("\nQuestion 2: What is Selena Gomez's Zodiac Sign? \n"
                    +"1) Gemini\n"
                    +"2) Cancer\n"
                    +"3) Libra\n"
                    +"4) Leo\n")
                ans2 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans2 == "2":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Cancer.\n")
                    
                print("\nQuestion 3: What Year Was Selena Gomez Born in? \n"
                    +"1) 1992\n"
                    +"2) 1999\n"
                    +"3) 1989\n"
                    +"4) 2001\n")
                ans3 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans3 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 1992.\n")
                                        
                print("\nQuestion 4: Where Was Selena Gomez Born? \n"
                    +"1) Texas\n"
                    +"2) California\n"
                    +"3) Wisconsin\n"
                    +"4) Canada\n")
                ans4 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans4 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Texas.\n")
                    
                print("\nQuestion 5: How Tall is Selena Gomez? \n"
                    +"1) 5'4\n"
                    +"2) 5'6\n"
                    +"3) 5'7\n"
                    +"4) 4'8\n")
                ans5 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans5 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 5'4.\n")
                
                #The variable score counted how many questions the user got correct, it gets sent to the calculator function to determine the user's overall results.
                print(calculator(score))
                
                #The user has the option to play again or exit the program.
                again = input("\nWould you like to play again?\nInput Y to play again, N to exit the game.")
                if again == "Y":
                    #continue is used to take the code back to the start of the while loop
                    continue
                else:
                    print("Goodbye!")
            
        else:
            #This print statment makes the user aware of their selection, so they can decide in the would like to proceed.
            print("You have selected Drake!")

            #This if condition asks the user if they want to proceed with their selection, if not then it brings them back to the options and selection process.
            check = input("Are you sure? Input Y to proceed or N to choose again.")
            if check == "N":
                continue
            
            else:
            #Questions: The program displays the questions, and answer options. Once the user answers the program checks if they were correct or not and updates the score.
                print("\nQuestion 1: What is Drake's First Name? \n"
                +"1) Rob\n"
                +"2) Cameron\n"
                +"3) Aubrey\n"
                +"4) Bob\n")
                ans1 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans1 == "3":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Aubrey.\n")
                    
                print("\nQuestion 2: What is Drake's First Album? \n"
                    +"1) Thank Me Later\n"
                    +"2) For All the Dogs\n"
                    +"3) More Life\n"
                    +"4) Certified Lover Boy\n")
                ans2 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans2 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Thank Me Later.\n")
                    
                print("\nQuestion 3: What is Drake's Mom's Name? \n"
                    +"1) Audrey Graham\n"
                    +"2) Sandi Graham\n"
                    +"3) Julia Drake\n"
                    +"4) Denise Graham\n")
                ans3 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans3 == "2":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Sandi Graham.\n")
                                        
                print("\nQuestion 4: What Year did Drake Release his First Album? \n"
                    +"1) 2010\n"
                    +"2) 2004\n"
                    +"3) 1989\n"
                    +"4) 2000\n")
                ans4 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans4 == "1":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is 2010.\n")
                    
                print("\nQuestion 5: Where was Drake Born? \n"
                    +"1) Pennsylvania\n"
                    +"2) New York\n"
                    +"3) Mississipi\n"
                    +"4) Toronto\n")
                ans5 = input("Input the number corresponding to your answer:")
                #This nested if statment checks if the user's answer corresponds to the correct answer, and will update their score accordingly.
                if ans5 == "4":
                    print("Correct.\n")
                    score+=1
                else:
                    print("Incorrect. The correct answer is Toronto.\n")
                
                #The variable score counted how many questions the user got correct, it gets sent to the calculator function to determine the user's overall results.
                print(calculator(score))
                
                #The user has the option to play again or exit the program.
                again = input("\nWould you like to play again?\nInput Y to play again, N to exit the game.")
                if again == "Y":
                    #continue is used to take the code back to the start of the while loop
                    continue
                else:
                    print("Goodbye!")
            
        #break is used to end the loop, and end the game   
        break




