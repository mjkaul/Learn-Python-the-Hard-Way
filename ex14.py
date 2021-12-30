from sys import argv

script, user_name, number_of_kids = argv
prompt = 'Type your answer: '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me, {user_name}?")
likes = input(prompt)

print(f"Where do you live, {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f'''
Alright. So you said \"{likes}\" about liking me. You live in {lives}. I'm not sure where that is. And you have a {computer} computer. Nice.
''')

print(f"How many kids do you have, {user_name}?")
print("Wait, let me guess...")
print(f"{number_of_kids}")

print("Am I right?")
right = input(prompt)