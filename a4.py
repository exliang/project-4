
"""
a4.py

Module that handles user input and generates the user interface

"""

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path
from shlex import split
import sys
import ui


def main():
    """
    Function summary: entrance of program -> calls the
                      function that handles user input
    Parameters: None
    Return value: None
    """
    print("Welcome!")
    # pass in admin as False to run the interface
    user_input(printing_user_interface(False))


def user_input(user_command):
    """
    Function summary: handles the user's command
                      by calling the respective function
    Parameters: user command (string)
    Return value: None
    """
    is_admin = False
    while True:
        if user_command == "admin":  # user command is admin
            is_admin = True
            user_command = input()
        else:  # user_command is not admin
            if is_admin:  # if admin mode was already called
                user_command = input()

        if user_command[0] == 'P' or user_command[0] == 'E':
            command_list = split(user_command)
        else:
            command_list = user_command.split()
        command = command_list[0]

        if command == 'Q':
            sys.exit()
        elif command == 'server':  # post journal entries to DSP server
            ui.post_to_server()
        elif len(command_list) == 1 and command != "admin":
            print("ERROR")  # user only inputs a letter & no dir
        elif command == "admin":
            is_admin = True
            user_command = input()
        else:
            path = command_list[1]
            my_path = Path(path)

            if command not in ('P', 'E'): # dont check for E & P
                my_path = handle_whitespace(my_path, command_list)

            if my_path.exists():  # ensure that directory exists
                if command == 'L':  # list contents of directory
                    if len(command_list) == 2:  # [COMMAND] [INPUT]
                        if "." in str(my_path):  # last part is a file
                            print("ERROR")
                        else:
                            ui.list_directories(my_path)
                    elif len(command_list) == 3:  # [C] [INPUT] [[-]OPTION]
                        option = command_list[2]
                        if option == '-r':
                            ui.recursive(my_path)
                        elif option == '-f':  # output files only
                            ui.list_files(my_path)
                        else:  # invalid command
                            print("ERROR")
                    elif len(command_list) == 4:  # [C][I][[-]O][I]
                        option = command_list[2]
                        if option == '-s':  # output files that match file name
                            file_name = command_list[3]
                            if "." not in file_name:  # ensure file is entered
                                print("ERROR")
                            else:
                                ui.matching_files(my_path, file_name)
                        elif option == '-e':
                            file_extension = command_list[3]
                            if len(file_extension) != 3:
                                print("ERROR")
                            else:
                                ui.matching_extension(my_path, file_extension)
                        elif option == '-r':  # -r -f
                            option2 = command_list[3]
                            ui.recursive_f(my_path)
                        else:  # invalid command
                            print("ERROR")
                    elif len(command_list) == 5:  # [C][I][[-]O][I][I]
                        option = command_list[2]
                        option2 = command_list[3]
                        if option == '-r' and option2 == '-s':  # -r -s filen.e
                            file_name = command_list[4]
                            if "." not in file_name:  # ensure file is entered
                                print("ERROR")
                            else:
                                ui.recursive_s(my_path, file_name)
                        elif option == '-r' and option2 == '-e':  # -r -e filee
                            file_extension = command_list[4]
                            if file_extension.isnumeric():  # fileex has nums
                                print("ERROR")
                            else:
                                ui.recursive_e(my_path, file_extension)
                        else:  # invalid command
                            print("ERROR")
                elif command == "C":  # create new DSU file
                    if command_list[2] != "-n":
                        print("ERROR")
                    else:
                        filename = command_list[3]
                        my_profile, new_path = ui.command_C(my_path, filename)
                elif command == "D":  # delete DSU file
                    ui.command_D(my_path)
                elif command == "R":  # read file contents
                    ui.command_R(my_path)
                elif command == "O":  # open exisiting dsu file
                    my_profile, new_path = ui.command_O(my_path)
                else:  # invalid command
                    print("ERROR")
            else:
                if command in ('D', 'R'):
                    ui.command_D(my_path)
                elif command == "E":  # edit dsu file
                    ui.command_E(new_path, command_list, my_profile)
                elif command == "P":  # printing data from dsu file
                    ui.command_P(my_path, command_list, my_profile)
                else:
                    print("Directory doesn't exist. Try again.")
        if not is_admin:  # after executing command & not admin
            # print interface & get next command
            user_command = printing_user_interface(is_admin)


def printing_user_interface(is_admin):  # Menu of options
    """
    Function summary: prints the user interface with all the possible options
    Parameters: is_admin mode (boolean)
    Return value: user command (string)
    """
    if not is_admin:
        print("\nHere are the possible command options:\n")
        print(" L - list contents of directory (has sub-commands) ", end='')
        print("~ FORMAT: 'L path'")
        print("   -r -> ouput directory content recursively ", end='')
        print("~ FORMAT: 'L path -r'")
        print("   -f -> output files only                   ", end='')
        print("~ FORMAT: 'L path -f'")
        print("   -s -> output files given a file name      ", end='')
        print("~ FORMAT: 'L path -s filename.extension'")
        print("   -e -> output files given a file extension ", end='')
        print("~ FORMAT: 'L path -e fileextension'")
        print("    Other valid ~ FORMATS: 'L path -r -f', ", end='')
        print("L path -r -s filename.extension', ", end='')
        print("'L path -r -e fileextension'\n")
        print(" C - create a new journal & acquire username, ", end='')
        print("password, & bio ~ FORMAT: 'C path -n filename'\n")
        print(" D - delete a dsu file ~ FORMAT: 'D path_to_dsu_file'\n")
        print(" R - read contents of a dsu file ", end='')
        print("~ FORMAT: 'R path_to_dsu_file'\n")
        print(" O - open a journal ~ FORMAT: 'O path_to_dsu_file'\n")
        print(" E - edit a journal (has sub-commands) ", end='')
        print("~ FORMAT: 'E subcommand text'")
        print("   NOTE: must call C or O command before calling E command!")
        print("   -usr     -> edits username of the journal  ", end='')
        print("~ FORMAT: 'E -usr username'")
        print("   -pwd     -> edits password of the journal  ", end='')
        print("~ FORMAT: 'E -pwd password'")
        print("   -bio     -> edits biography of the journal ", end='')
        print("~ FORMAT: 'E -bio biography'")
        print("   -addpost -> adds a post to the journal     ", end='')
        print("~ FORMAT: 'E -addpost newpost'")
        print("   -delpost -> deletes a post in the journal  ", end='')
        print("~ FORMAT: 'E -delpost postnumber' (postnumber starts at 0)")
        print("    NOTE: can type in any combination of the options above!\n")
        print(" P - output data stored in journal ", end='')
        print("~ FORMAT: P command optionaltext")
        print("   NOTE: must call C or O command before calling P command!")
        print("   -usr   -> outputs username stored in the journal  ", end='')
        print("~ FORMAT: 'P -usr'")
        print("   -pwd   -> ouputs password stored in the journal   ", end='')
        print("~ FORMAT: 'P -pwd'")
        print("   -bio   -> outputs biography stored in the journal ", end='')
        print("~ FORMAT: 'P -bio'")
        print("   -posts -> outputs all posts stored in the journal ", end='')
        print("~ FORMAT: 'P -posts'")
        print("   -post  -> outputs a post by its postnumber        ", end='')
        print("~ FORMAT: 'P -post postnumber' (postnumber starts at 0)")
        print("   -all   -> outputs all content in the journal      ", end='')
        print("~ FORMAT: 'P -all'")
        print("    NOTE: can type in any combination of the options above!\n")
        print(" Q - quit the program ~ FORMAT: 'Q' \n")
        print(" Admin mode - disables user friendly interface ", end='')
        print("~ FORMAT: 'admin'\n")
        print(" Post to server - post journal entries to DSP server ", end='')
        print("~ FORMAT: 'server'\n")
        user_command = input("Type the format you would like: ")
        return user_command


def handle_whitespace(my_path, command_list):
    """
    Function summary: handles whitespace in paths
    Parameters: path (string)
	            list of commands (list)
    Return value: new path (string)
    """
    # ensuring proper whitespace handling
    path = [command_list[1]]  # part of path
    for part in command_list[2:]:
        if part.startswith("-"):  # reached next command (ex: -r)
            break
        if ("\\" in part) or ("/" in part) or ("." in part):
            path.append(part)  # part of path (file or dir)
    my_path = " ".join(path)
    for part in command_list[:]:  # copy of lst bc of indexing
        if part.startswith("-"):  # reached next command (ex: -r)
            break
        if ("\\" in part) or ("/" in part) or ("." in part):
            command_list.remove(part)  # remove old path
    command_list.insert(1, my_path)  # insert new path into list
    my_path = Path(my_path)  # new path
    return my_path


if __name__ == '__main__':
    main()

# Citations:
# - https://docs.python.org/3/library/pathlib.html
# - https://docs.python.org/3/library/shlex.html#module-shlex
