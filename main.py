import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
gueesed_states = []

while len(gueesed_states) < 50:
  answer_state = screen.textinput(title=f"{len(gueesed_states)}/50 States Correct", prompt="What's another state name?").title()
  print(answer_state)

  if answer_state in all_states:
      gueesed_states.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(int(state_data.x), int(state_data.y))
      t.write(answer_state)


screen.exitonclick()