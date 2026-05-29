import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S state game")
image = "Quiz_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
correct_guess = []

data = pandas.read_csv("Quiz_game/50_states.csv")
states = data.state.to_list()

while len(correct_guess) < 51:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct", 
                                        prompt="What is the other state name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in states if state not in correct_guess]
        # missing_states =[]
        # for state in states:
        #     if state not in correct_guess:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Quiz_game/missedstates.csv")
        break
    if answer_state in states:
        state_data = data[data.state == answer_state]

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state)
        correct_guess.append(answer_state)

