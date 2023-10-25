PLACEHOLDER="[name]"
with open("./Input/Letters/starting_letter.txt") as letter:
    starting_letter=letter.read() #read() method returns a sting
with open("./Input/Names/invited_names.txt",mode="r") as invited_names:
    names=invited_names.readlines() #readlines() resturns a list
for name in names:
    stripped_name=name.strip() #.strip() method has been used to chip off the extra line
    completed_letter = starting_letter.replace(PLACEHOLDER,stripped_name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt",mode="w") as completed_file:
        completed_file.write(completed_letter)

