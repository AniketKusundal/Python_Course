questions = [
    ["Which language was used to create FB?", "Python", "JavaScript", "PHP", "Java", "None", 3],

    ["A process is a ______.", "Single thread of execution", "Program in execution", "Program in memory", "Code segment", "None", 2],

    ["What does RAM stand for?", "Random Access Memory", "Read Access Memory", "Run Access Memory", "Read And Memory", "None", 1],


    ["Which part of the computer is considered the brain?", "Hard Drive", "CPU", "RAM", "Motherboard", "None", 2],


    ["What does HTTP stand for?", "Hypertext Transfer Protocol", "Hyper Transfer Text Protocol", "Hyperlink Text Protocol", "Hypertext Transmit Protocol", "None", 1],


    ["Which device is used to input data?", "Printer", "Monitor", "Keyboard", "Speaker", "None", 3],


    ["What is the full form of IP in 'IP Address'?", "Internet Provider", "Internal Protocol", "Internet Protocol", "Internal Provider", "None", 3],


    ["What is the shortcut for copying text?", "Ctrl + A", "Ctrl + V", "Ctrl + C", "Ctrl + X", "None", 3],


    ["What is the binary representation of the decimal number 5?", "101", "110", "100", "111", "None", 1],


    ["What is an algorithm?", "A step-by-step solution to a problem", "A computer program", "A type of software", "A mathematical equation", "None", 1],


    ["Which company developed the Windows operating system?", "Apple", "Google", "Microsoft", "IBM", "None", 3],


    ["What does GUI stand for?", "Graphical User Internet", "Graphical User Interface", "General User Interface", "Global User Interaction", "None", 2],

    ["What is the main function of the operating system?", "Word processing", "Managing hardware and software resources", "Storing data", "Connecting to the internet", "None", 2],


    ["What does URL stand for?", "Uniform Resource Locator", "Unique Resource Locator", "Universal Resource Locator", "Universal Routing Locator", "None", 1],


    ["Which key is used to refresh a webpage?", "F1", "F3", "F5", "F7", "None", 3],
]


levels = [1000 , 2000 , 3000 , 5000 , 10000 , 20000 , 40000 , 80000 , 120000 , 320000]
money = 0


for i in range(0 , len(questions)):
    question = questions[i]
    print(f"\n\nQuestion for Rs. {levels[i]}")

    print(f"{question[0]}")                                 # this for the question 
    print(f"a. {question[1]}        b. {question[2]}")
    print(f"c. {question[3]}        d. {question[4]}")
    replay = int(input("Enter  Your Answer (1-4) :"))

    if (replay == question[-1]):
        print(f"Correct Answer ,  You Won  Rs. {levels[i]} ")

        if (i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 12):
            money = 1000000
    else:
        print("Wrong Answer ")
        break

print(f"Your Take Home money is {money}")