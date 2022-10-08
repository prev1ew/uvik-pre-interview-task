from colorama import init
import actions as ac
from settings import warn_colour, input_colour, info_colour, exit_messages
from misc import initialize_file


init(autoreset=True)  # auto-reset the colour of the output (print function)

initialize_file()
print("Welcome friend! It's a simple TODO app , list of commands:")
ac.show_help()
while True:
    print("-" * 20)
    curr_response = input(input_colour + 'Please select desired action: ')
    if curr_response in exit_messages:
        print('Goodbye!')
        break
    curr_action = ac.actions_dict.get(curr_response, False)
    if curr_action:
        curr_action()
    else:
        print(warn_colour + 'Incorrect input, please try again.')
