from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

def generate_password(min_length,numbers=True,spl_characters=True,Uppercase=True):
    letters = string.ascii_lowercase
    upc = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if spl_characters:
        characters += special
    if Uppercase:
        characters += upc

    pwd = ""
    meet_criteria = False
    has_numbers = False
    has_specials = False
    has_upper = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_specials = True
        elif new_char in upc:
            has_upper = True

        # determine if all required criteria are met
        meet_criteria = True
        if numbers:
            meet_criteria = has_numbers
        if spl_characters:
            meet_criteria = meet_criteria and has_specials
        if Uppercase and not has_upper:
            meet_criteria = meet_criteria and has_upper

    return pwd

"""
this is the basic format to work in the Terminal

min_length = int(input("Enter how many letters passwords you want: "))
has_numbers = str(input("Do you want to have numbers (y/n)?: ")).lower() =="y"
has_specials = str(input("Do you want to have Special characters (y/n)?: ")).lower() =="y"
has_upper = str(input("Do you want to have Upper characters (y/n)?: ")).lower() =="y"
pwd = generate_password(min_length, has_numbers, has_specials, has_upper)
print("The generated Password: ",pwd)

"""

@app.route("/", methods=["GET", "POST"])
def home():
    password = None
    if request.method == "POST":
        length = int(request.form["length"])
        numbers = "numbers" in request.form
        specials = "specials" in request.form
        uppercase = "uppercase" in request.form

        password = generate_password(length, numbers, specials, uppercase)

    return render_template("index.html", password=password)

if __name__ == "__main__":
    app.run(debug=True)