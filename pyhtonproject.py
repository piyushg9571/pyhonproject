import random

quiz_questions_easy = {
    "Laws of motion": [
        {"question": "Newton's second law of motion is usually stated as:", "options": ["A. F = ma", "B. F = mgh", "C. F = mv", "D. F = ms"], "answer": "A"},
        {"question": "An object at rest will remain at rest, and an object in motion will remain in motion with a constant velocity unless acted on by an external force. This statement is known as:", "options": ["A. Newton's First Law", "B. Newton's Second Law", "C. Newton's Third Law", "D. Archimedes' Principle"], "answer": "A"},
        {"question": "Which law of motion states For every action, there is an equal and opposite reaction:", "options": ["A. Newton's First Law", "B. Newton's Second Law", "C. Newton's Third Law", "D. Kepler's Law"], "answer": "C"},
        {"question": "If the mass of an object increases while the force remains the same, what happens to its acceleration according to Newton's second law?", "options": ["A. Increases", "B. Decreases", "C. Remains same", "D. Becomes zero"], "answer": "B"},
        {"question": "What is inertia?", "options": ["A. The force required to change an object's motion", "B. The resistance of an object to change its state of motion", "C. The speed of an object", "D. The direction of an object's motion"], "answer": "B"},
    ],
    "2. Work Power And Energy": [
        {"question": "which of the following defines work done by a force on an object?", "options": ["A. Force times time", "B. Force times distance moved in the direction of the force", "C. Mass times acceleration", "D. Velocity times displacement"], "answer": "B"},
        {"question": "If no displacement occurs, the work done is:", "options": ["A. Positive", "B. Negative", "C. Zero", "D. Constant"], "answer": "C"},
        {"question": "Power is defined as:", "options": ["A. Force multiplied by velocity", "B. Work done divided by time", "C. Mass multiplied by acceleration", "D. Distance divided by time"], "answer": "B"},
        {"question": "Which type of energy is associated with motion?","options": ["A. Potential energy", "B. Chemical energy", "C. Thermal energy", "D. Kinetic energy"], "answer": "D"},
        {"question":"The law of conservation of energy states that:","options": ["A. Energy cannot be created or destroyed, only transformed", "B. Energy can be created but not destroyed", "C. Energy is constantly increasing", "D. Energy is constantly decreasing"], "answer": "A"},
    ],
    
    "3. Electrostats": [
        {"question": "What is the unit of electric charge?","options": ["A. Volt", "B. Ampere", "C. Coulomb", "D. Ohm"],"answer": "C"},
        {"question": "Like charges _____ and unlike charges _____ each other.","options": [ "A. attract, repel", "B. repel, attract", "C. attract, attract", "D. repel, repel"],"answer": "B"},
        {"question": "Which of the following materials is a good insulator?","options": ["A. Copper", "B. Silver", "C. Glass", "D. Aluminum"],"answer": "C"},
        {"question": "What is the relationship between electric potential and electric potential energy?","options": [ "A. Directly proportional", "B. Inversely proportional", "C. No relationship", "D. Both are constants"],"answer": "A"},
        {"question":  "Which of the following is a fundamental property of an electric field?","options": [ "A. Direction", "B. Magnitude", "C. Both A and B", "D. Neither A nor B"],"answer": "C"},
    ]
}

quiz_questions_medium = {
    "Laws of motion": [
        {"question": "Which law of motion states 'Every object persists in its state of rest or uniform motion unless acted upon by an external unbalanced force'?", "options": ["A. First Law of Motion", "B. Second Law of Motion", "C. Third Law of Motion", "D. None of the above"], "answer": "A"},
        {"question": "If two objects with different masses are dropped from the same height in a vacuum, which one will hit the ground first?", "options": ["A. The heavier object", "B. The lighter object", "C. Both will hit at the same time", "D. It depends on the shape of the objects"], "answer": "C"},
        {"question": "What is the term for the force that opposes the relative motion or tendency of such motion of two surfaces in contact?", "options": ["A. Gravitational force", "B. Frictional force", "C. Tension force", "D. Centrifugal force"], "answer": "B"},
        {"question": "Which of the following is NOT a type of friction?", "options": ["A. Static friction", "B. Kinetic friction", "C. Air friction", "D. Elastic friction"],"answer": "D"},
        {"question": "The force required to keep an object moving in a circle at a constant speed is called:","options": ["A. Gravitational force", "B. Centrifugal force", "C. Centripetal force", "D. Frictional force"],"answer": "C"},
    ],

    "2. Work Power And Energy": [
        {"question": "What is the power output of a machine that does 200 J of work in 5 seconds?", "options": ["A. 40 W", "B. 50 W", "C. 30 W", "D. 10 W"], "answer": "A"},
        {"question": "Which energy transformation occurs in a hydroelectric power plant?", "options": ["A. Chemical to Electrical", "B. Kinetic to Potential", "C. Potential to Kinetic", "D. Thermal to Electrical"], "answer" : "C"},
        {"question": "What is the unit of power in terms of base SI units?", "options": [ "A. Joule/second", "B. Watt/second", "C. Newton-meter", "D. Watt"], "answer": "D"},
        {"question": "What is the work done by a force of 10N in moving an object 5 meters against a frictional force of 2N?", "options": ["A. 50 J", "B. 40 J", "C. 30 J", "D. 20 J"],"answer": "B"},
        {"question": "Which formula represents the work-energy theorem?", "options": ["A. \( W = F \cdot d \)", "B. \( W = \frac{1}{2} m v^2 \)", "C. \( W = P \cdot t \)", "D. \( W = \Delta KE \)"],"answer": "D"},
    ],

    "3. Electrostats": [
        {"question":"What is the electric field inside a uniformly charged spherical shell?","options": ["A. Zero", "B. Constant", "C. Varies with radius", "D. Varies with charge"],"answer": "A"},
        {"question": "What does Gauss's Law state about the electric flux through a closed surface?","options": [ "A. It is always positive", "B. It is always negative", "C. It can be positive or negative", "D. It is zero"],"answer": "D"},
        {"question": "Two point charges +Q and -Q are placed 2 meters apart. Where is the electric field zero?","options": ["A. At the midpoint between the charges", "B. At a point 1 meter from +Q", "C. At infinity", "D. Everywhere"],"answer": "A"},
        {"question": "The electric potential due to a point charge varies with distance as:","options": ["A. Linearly", "B. Quadratically", "C. Inversely", "D. Logarithmically"],"answer": "B"},
        {"question": "What does the permittivity of a medium determine?","options": [ "A. Electric field strength", "B. Electric potential", "C. Capacitance", "D. Both A and C"],"answer": "D"},
    ]
}

quiz_questions_difficult = {
    "1. Laws of motion": [
        {"question": "A 50 kg box is pushed with a force of 200 N across a horizontal surface. If the frictional force is 100 N, what is the acceleration of the box?","options": [ "A. 2 m/s²", "B. 4 m/s²", "C. 6 m/s²", "D. 8 m/s²"],"answer": "A"},
        {"question": "A 2 kg object moving with a velocity of 4 m/s collides with a stationary 3 kg object. If the collision is perfectly elastic, what is the velocity of the 3 kg object after the collision?","options": [ "A. 2 m/s", "B. 4 m/s", "C. 6 m/s", "D. 8 m/s"],"answer": "D"},
        {"question": "A ball is thrown vertically upwards with an initial velocity of 20 m/s. What is its maximum height? (Take g = 9.8 m/s²)", "options": [ "A. 20 m", "B. 40 m", "C. 80 m", "D. 100 m"],"answer": "C"},
        {"question": "A car of mass 1000 kg accelerates from rest to 20 m/s in 5 seconds. What is the average power developed by the engine during this time?","options": [ "A. 8 kW", "B. 16 kW", "C. 20 kW", "D. 32 kW"],"answer": "B"},
        {"question": "Which of the following scenarios violates the principle of conservation of momentum?","options": [ "A. A rocket accelerating in space", "B. Two skaters pushing each other apart on ice", "C. A car colliding with a stationary object", "D. A ball bouncing off a wall"],"answer": "B"},
    ],

    

    "2. Work Power And Energy": [
        {"question": "A car accelerates from 0 to 60 mph in 5 seconds. If the car has a mass of 1500 kg, what is the average power developed by the engine?","options": ["A. 50 kW", "B. 100 kW", "C. 200 kW", "D. 250 kW"],"answer": "C"},
        {"question": "A 10 kg block is lifted 2 meters vertically with a constant force of 50 N. What is the work done?","options": ["A. 500 J", "B. 100 J", "C. 980 J", "D. 200 J"], "answer": "A"},
        {"question": "A machine with a power output of 500 W lifts a 200 kg object 5 meters in 10 seconds. What is the efficiency of the machine?", "options": [ "A. 25%", "B. 50%", "C. 75%", "D. 100%"], "answer": "B"},
        {"question": "Which principle states that the total mechanical energy of a system remains constant if no external forces are acting on it?", "options": [ "A. Law of Conservation of Energy", "B. Principle of Relativity", "C. Principle of Least Action", "D. Lagrangian Principle"], "answer": "A"},
        {"question": "In a nuclear power plant, which energy transformation occurs?", "options": [ "A. Chemical to Electrical", "B. Nuclear to Thermal", "C. Thermal to Electrical", "D. Kinetic to Electrical"], "answer": "B"},
    ],
    
    "3. Electrostats": [
        {"question": "A charged particle is placed inside a hollow conductor. What happens to the electric field inside the conductor?","options": ["A. Becomes zero", "B. Becomes infinite", "C. Becomes constant","D. Increases"],"answer": "A"},
        {"question": "If a dielectric material with dielectric constant \( \kappa \) is inserted between the plates of a capacitor, what happens to its capacitance?","options": [ "A. Increases by a factor of \( \kappa \)", "B. Decreases by a factor of \( \kappa \)", "C. Remains unchanged","D. Becomes zero"],"answer": "A"},
        {"question": "What is the electric potential duE to a point charge \( Q \) at a distance \( r \) from it?","options": [ "A. \( \frac{kQ}{r} \)", "B. \( \frac{kQ}{r^2} \)", "C. \( \frac{Q}{4\pi\epsilon_0 r} \)", "D. \( \frac{Q}{4\pi\epsilon_0 r^2} \)"],"answer": "A"},
        {"question": "What is the principle of superposition in electrostatics?","options": ["A. The electric field due to multiple charges is the vector sum of the electric fields due to each charge individually.", "B. The total charge of a system remains constant.", "C. Charges distribute themselves on a conductor to minimize their potential energy.", "D. The electric flux through a closed surface is proportional to the enclosed charge."],"answer": "A"},
        {"question": "What does Coulomb's law describe?","options": ["A. The electric field due to a point charge.", "B. The force between two point charges.", "C. The electric potential due to a point charge.", "D. The capacitance of a parallel plate capacitor."],"answer": "B"},
    ]
}

all_quiz_questions =[quiz_questions_easy, quiz_questions_medium,quiz_questions_difficult]


print("PHYSICS QUIZ \n")
name = input("Enter your name: ")
score = 0
level = 0

def GetDifficultyLevel():
    levelChoice = input("Enter 1 for easy, 2 for medium and 3 for difficult: ")
    return int(levelChoice) - 1 



def GetQuizCategory(quiz_questions):
    #takes user's choice
    print("QUIZ CATEGORIES")
    print(list(quiz_questions.keys()))
    choice = input("Enter number of quiz category (enter 'q' to exit):")
    size_of_quiz = len(quiz_questions)

    if(choice >= 'a'):
        return 'q'
    elif(int(choice) > size_of_quiz):
        #users input is incorrect
        print("INVALID INPUT")
        return 'w'
    else:
        #returns users choice if it's correct
        return int(choice)
    
def CheckCorrectAnswer(userInput, correctAnswer):
    #checks if users if input is correct and within range, also updates score
    if(userInput.upper() == correctAnswer):
        message = "Well Done! Your anser is correct"
        isCorrect = True
    elif(userInput.upper() > "D"):
        message = "INVALID INPUT. VALUE DOESN'T MATCHES THE RANGE"
        isCorrect = False
    else:
        message = "Oops! Your answer is incorrect."
        isCorrect = False

    
    return message,isCorrect

def DisplayQuestions():
    #displays quesyions, options. Also takes input from user
    score = 0
    isCorrect = False
    isPlaying = True
    while isPlaying:
        level = GetDifficultyLevel()
        
        choice = GetQuizCategory(all_quiz_questions[level])
        quesNumber = 1
        if(choice == 'w'):
            DisplayQuestions()
        elif(choice == 'q'):
            print("Your Score: ", score)
            print("GOODBYE!", name)
            isPlaying = False
            break

        #get all the categories
        categories = list(all_quiz_questions[level].keys())
        #users selected category
        selected_category = all_quiz_questions[level].get(categories[choice - 1])

        #displays question and options, takes input from user for each question in the selected category
        for i in range(len(selected_category)):
            question = selected_category[i].get("question")
            options = selected_category[i].get("options")
            correctAnswer = selected_category[i].get("answer")
            
            print("{}.".format(quesNumber), question, "\n", options)
            selectedAnswer = input("Enter your option: \n")

            if(selectedAnswer.lower() == "q"):
                print("GOODBYE!", name)
                print("Your Score: ", score)
                isPlaying = False
                break

            message,isCorrect = CheckCorrectAnswer(selectedAnswer, correctAnswer)
            print(message)

            if(isCorrect):
                score += 1
            else:
                 print("Correct Answer is:", correctAnswer, "\n")    
            quesNumber += 1
        
        print("Your Score: ", score)
        continue_choice = input("Press 'C' to continue or 'Q' to exit: ")

        if(continue_choice.lower() == 'c'):
            continue;
        elif(continue_choice.lower() == 'q'):
            print("GOODBYE!", name)
            print("Your Score: ", score)
            isPlaying = False
            break
        

try:
    DisplayQuestions()
except TypeError:
    pass
