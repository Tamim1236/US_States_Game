import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Games")
screen.setup(width=700, height=600)

image = "blank_states_img.gif"
screen.addshape(image)
screen.bgpic(image)


states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()
guessed_correct = []


# def get_mouse_click_coor(x, y):
#     print(x, y)
#

while len(guessed_correct) != 50:
    answer_state = screen.textinput(title=f"{len(guessed_correct)}/50 States Correct",
                                    prompt="What's another state's name").title()

    if answer_state in state_names and answer_state not in guessed_correct:
        state_row = states_data[states_data.state == answer_state]
        state_turtle = turtle.Turtle()
        state_turtle.penup()
        state_turtle.hideturtle()
        state_turtle.goto(int(state_row.x), int(state_row.y))
        state_turtle.write(answer_state)
        guessed_correct.append(answer_state)

    if answer_state == 'Exit':
        break


missing_states = [state for state in state_names if state not in guessed_correct]

missing_states_dataframe = pandas.DataFrame(missing_states)
missing_states_dataframe.to_csv("missing_states.csv")


