score = 0
print("Hello User!","Welcome to the Quiz Game.",sep="\n")
a = input("Enter your name: ")
print("Hi %s!!" % a, "Would you like to start the Quiz?","1. Yes","2. No",sep="\n")
x = input("Enter your choice: ")

if x == "1":
    print("What level would you like to play?","1. Easy","2. Medium","3. Hard",sep="\n")
    y = input("Enter the level you want to play: ")
    
    if y == "1":
        correct = ['c', 'd', 'd', 'c']
        print("Let's start!")
        quest = ["Q1. If 1=3, 2=3, 3=5, 4=4, 5=4\nThen, 6=?",
                 "Q2. Which number is equivalent to 3^(4) ÷ 3^(2)?",
                 "Q3. I am an odd number. Take away one letter and I become even. What number am I?",
                 "Q4. Sally is 54 years old and her mother is 80, how many years ago was Sally’s mother times her age?"]
        option = [["a. 5", "b. 7", "c. 3", "d. 2"],
                  ["a. 12", "b. 8", "c. 10", "d. 9"],
                  ["a. four", "b. seventeen", "c. eight", "d. seven"],
                  ["a. 41", "b. 35", "c. 43", "d. 40"]]
        for i in range(len(quest)):
            print(quest[i])
            for j in option[i]:
                print(j)
            choice = input("What is your choice: ")
            if choice == correct[i]:
                print("Correct answer!")
                score += 1
            else:
                print("Wrong answer!")
        print("%s" % a, "Your final score is:", score, "out of", len(quest))
        print("Congratulations! You won the game" if score == 4 else "Better luck next time!!" )
            
    elif y == "2":
        correct = ['b', 'd', 'a', 'c']
        print("Let's start the game!")
        quest = ["Q1. Which among the following is the largest known number in the world?",
                 "Q2. If + means ÷, ÷ means –, – means x and x means +, then: 9 + 3 ÷ 5 – 3 x 7 = ?",
                 "Q3. How many hours are there in a year (rounded to the nearest hour)?",
                 "Q4. Which number is equivalent to 3^(4)/3^(2)?"]
        option = [["(a) ∞", "(b) googol", "(c) googolplex", "(d) gram"],
                  ["(a) 5", "(b) 15", "(c) 25", "(d) None of these"],
                  ["(a) 8760", "(b) 8000", "(c) 7658", "(d) 8568"],
                  ["(a) 6", "(b) 8", "(c) 9", "(d) 10"]]
        for i in range(len(quest)):
            print(quest[i])
            for j in option[i]:
                print(j)
            choice = input("What is your choice: ")
            if choice == correct[i]:
                print("Correct answer!")
                score += 1
            else:
                print("Wrong answer!")
        print("%s" % a, "Your final score is:", score, "out of", len(quest))
        print("Congratulations! You won the game" if score == 4 else "Better luck next time!!" )
            
    elif y == "3":
        correct = ['d', 'b', 'b', 'a']
        print("Let's start the level!")
        quest = ["Q1. A tank can be filled by two pipes in 10 and 30 minutes, respectively, and a third pipe can empty in 20 minutes. How much time will the tank fill if three pipes are opened simultaneously?",
                 "Q2. Adding the numbers between 1 to 100 consecutively (1+2+3+4+…) gives you what final answer?",
                 "Q3.What is the value of x for the equation 3x+5/2x+1 = 1/3?",
                 "Q4.What is the value of z for the linear equation (z+6)/4 + (z-3)/5 = (5z-4)/8 ?"]

        option = [["(a) 10 min", "(b) 8 min", "(c) 7 min", "(d) None of these"],
                  ["(a) 5045", "(b) 5050", "(c) 5145", "(d) 5200"],
                  ["(a) 4","(b) -2","(c) 5","(d) 2"],
                  ["(a) 8","(b) 4","(c) 3","(d) 7"]]

        for i in range(len(quest)):
            print(quest[i])
            for j in option[i]:
                print(j)
            choice = input("What is your choice: ")
            if choice == correct[i]:
                print("Correct answer!")
                score += 1
            else:
                print("Wrong answer!")
        print("%s" % a, "Your final score is:", score, "out of", len(quest))
        print("Congratulations! You won the game" if score == 4 else "Better luck next time!!" )
    else:
        print("Invalid choice")
        
else:
    print("Thank you for visiting.")
