#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("Mail_Merge_Project_Start/Input/Letters/starting_letter.txt" ,"r") as input:
    letter_input = input.read()

with open ("Mail_Merge_Project_Start/Input/Names/invited_names.txt", "r") as names:
    data = names.readlines()
        
for datas in data:
    stripped_name = datas.strip()
    new_letter = letter_input.replace("[name]", stripped_name)

    with open(f"Mail_Merge_Project_Start/Output/ReadyToSend{stripped_name}.txt","w") as completed_letter:
        completed_letter.write(new_letter)