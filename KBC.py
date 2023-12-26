Questions = [
    #Question 1
['Which of the following is the largest planet in our solar system?',
 'Earth',
 'Jupiter',
 'Mars',
 'Saturn',2],
    #Queston 2
['Who wrote the famous play "Romeo and Juliet"?',
'William Shakespeare',
'Jane Austen',
'Charles Dickens',
'Mark Twain',1],
    #Queston 3
['What is the capital city of Australia?',
 'Sydney',
 'Melbourne',
 'Canberra',
 'Perth',3],
    #Question 4
['Which famous scientist developed the theory of general relativity?',
 'Isaac Newton',
 'Albert Einstein',
 'Nikola Tesla',
 'Marie Curie',2],
    #Question 5
[ 'What is the largest organ in the human body?',
 ' Heart',
 ' Liver',
 ' Brain',
 ' Skin',4],
    #Question 6
['Which continent is home to the Nile River?',
 'Africa',
 'Asia',
 'Europe',
 'South America',1],
    #Question 7
['Who painted the Mona Lisa?',
 'Pablo Picasso',
 'Leonardo da Vinci',
 'Vincent van Gogh',
 'Michelangelo',2],
    #Question 8
['What is the chemical symbol for the element gold?',
 'Au',
 'Ag',
 'Fe',
 'Pt',1], 
    #Question 9
['Which country is known as the "Land of the Rising Sun"?',
 'China',
 'Japan',
 'India',
 'Australia',2],
    #Question 10
['Who is the current President of the United States?',
 'Joe Biden',
 'Donald Trump',
 'Barack Obama',
 'George W. Bush',1]

]
Level = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
Money = 0
for i in range(0,len(Questions)):
    Question = Questions[i]
    print(f"\n\n Question for Rs. {Level[i]}")
    print(f"Question {i+1} : {Question[0]}")
    print(f"A . {Question[1]}                B . {Question[2]}" )
    print(f"C . {Question[3]}                D . {Question[4]}")
    

    Reply = int(input("Enter (1-4) for Answer or 0 for Quit : "))

    if(Reply==0):
        Money = Level[i-1]
        break
    elif(Reply==Question[-1]):
        print(f"You have enter Corret Answer , You Won Rs. {Level[i]} ")
        if(i==4):
            Money =10000
        elif(i==9):
            Money =320000    
        elif(i==14):
            Money = 10000000
    else:
        print("You have entered Wrong answer .")
        break
print(f"Your home taken Money is : {Money}")    
