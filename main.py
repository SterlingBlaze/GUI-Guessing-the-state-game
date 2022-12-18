import turtle
import pandas
from tkinter import messagebox

state_data = pandas.read_csv("50_states.csv")
states = state_data.state.to_list()

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
screen.setup(height=500, width=730)
turtle.shape(image)
guessed_states = []


while len(guessed_states) < 50:
    user_guess = screen.textinput(title=f"{len(guessed_states)}/50Guess State",
                                  prompt="What's another state name?: ").title()
    if guessed_states.count(user_guess) == 1:
        messagebox.showinfo(title="Duplicate Guess", message=f"{user_guess} is already on the map.")

    elif user_guess == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        missing_data = pandas.DataFrame(missing_states)
        missing_data.to_csv("states_to_learn.csv")
        break

    elif user_guess in states:
        guessed_states.append(user_guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
                        # pull the row of user guessed data eg. data[data.state]
        guessed_state_data = state_data[state_data.state == user_guess]
        t.goto(int(guessed_state_data.x), int(guessed_state_data.y))
        t.write(user_guess)








