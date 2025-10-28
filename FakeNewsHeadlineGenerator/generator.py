import random 

subjects = ["Monkey","Dhol","Motu","Patlu","Giyan","chutki","Babu Bhaiya","Raju"]
actions = ["nach rahi hai","thoos raha hai","ae tu ja re","cancels meeting"]
objects = ["chat pe", "gali me","office me ","samose ki dukan pe "]

genMore = input("Do you want to generate more sentences? (yes/no): ").strip().lower()
saved_sentence = []

while(genMore == "yes"):
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)
    print(f"{subject} {action} {object}")

    save = input("Do you want to save the sentences to a file? (yes/no): ").strip().lower()

    if(save == "yes"):
        #saved_sentence = saved_sentence.append(f"{subject} {action} {object}\n")  this is wrong as append function return none type and we are assigning it to a list 
        saved_sentence.append(f"{subject} {action} {object}\n")
        print("Headline added to the save list")

    genMore = input("do you want to generate more sentences? (yes/no): ").strip().lower()

if saved_sentence:
    filename = input("Enter the filename to save the sentences: ")
    with open(filename,"w") as file:
        for h in saved_sentence:
            file.write(h + "\n")

        
print("Thank you for using the sentence generator!")

seefile = input("want to see the saved sentences? (yes/no): ").strip().lower()
if seefile == "yes":
    if saved_sentence:
        print("Saved sentences:")
        for sentence in saved_sentence:
            print(sentence.strip())
    else:
        print("No sentences saved.")

