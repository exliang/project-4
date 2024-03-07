
"""
ui.py

Module including all the functions necessary for the commands
"""

# Emily Liang
# exliang@uci.edu
# 79453973

from pathlib import Path, PurePath
import Profile
import ds_client
import OpenWeather as ow
import LastFM as lfm


def list_directories(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        dir_list = []
        file_list = []
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_file():  # if is file, put it in the file list
                file_list.append(current_path)
            elif current_path.is_dir():  # if it's a dir, put in the dir list
                dir_list.append(current_path)
        file_list.extend(dir_list)  # combine lists (files first)
        combined_list = file_list
        for directory in combined_list:
            print(directory)


def list_files(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_file():  # list files only
                print(current_path)


def matching_files(my_path, file_name):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_file() and current_path.name == file_name:
                print(current_path)


def matching_extension(my_path, file_extension):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.name.endswith(file_extension):  # file type = file e
                print(current_path)


def recursive(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    dir_list = []
    if not any(my_path.iterdir()):  # if there's no more folders in directory
        return
    elif any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_file():  # if it's a file, print it
                print(current_path)
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_dir():  # if a dir, call func recursively
                dir_list.append(current_path)
                print(current_path)
                recursive(current_path)


def recursive_f(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if not current_path.is_dir():
                print(current_path)
        for current_path in my_path.iterdir():
            if current_path.is_dir():  # if a dir, call func recursively
                recursive_f(current_path)


def recursive_s(my_path, file_name):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.is_file() and current_path.name == file_name:
                print(current_path)
        for current_path in my_path.iterdir():
            if current_path.is_dir():  # if a dir, call func recursively
                recursive_s(current_path, file_name)


def recursive_e(my_path, file_extension):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if any(my_path.iterdir()):  # check if directory isnt empty
        for current_path in my_path.iterdir():  # list contents of the directory
            if current_path.name.endswith(file_extension):  # file type = file e
                print(current_path)
        for current_path in my_path.iterdir():
            if current_path.is_dir():  # if a dir, call func recursively
                recursive_e(current_path, file_extension)


def command_C(my_path, filename):
    """
    Function summary:
    Parameters:
    Return value:
    """
    while True:
        username = input("Enter a unique name: ")
        pw = input("Enter a password: ")
        bio = input("Enter a brief description of the user: ")

        newPath = my_path.joinpath(filename + ".dsu")
        if newPath.is_file() and newPath.exists():  # file already exists
            file = open(filename + ".dsu", "a")  # load file
        else:  # create file only after data is collected
            newfile = open(filename + ".dsu", "a")

        # ensuring empty strings or whitespace strings are not added
        profile = Profile.Profile()  # creating obj Profile
        profile.bio = bio
        if not whitespace_checker(username):
            profile.username = username
        if not whitespace_checker(pw):
            profile.password = pw
        if not whitespace_checker(username) and not whitespace_checker(pw):
            profile.save_profile(newPath)  # saving data
            print("Data saved.")
            break
        else:
            print("Invalid username and password.")
    return profile, newPath


def command_D(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    while True:
        dsufile = get_path_parts(my_path)
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            my_path = get_path(dsufile)  # so that my_path changes
        else:  # file is DSU file
            Path.unlink(dsufile)  # delete file from path
            print(my_path, "DELETED")  # output the path
            break


def command_R(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    while True:
        dsufile = get_path_parts(my_path)
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            my_path = get_path(dsufile)
        elif my_path.stat().st_size == 0:  # file_size = my_path.stat().st_size
            print("EMPTY")
            my_path = get_path(dsufile)
        else:  # print file contents
            print(my_path.read_text().strip())
            break


def command_O(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    while True:
        dsufile = get_path_parts(my_path)
        # check if dsu file follows Profile format
        profile_O = Profile.Profile()
        try:
            profile_O.load_profile(my_path)
        except Exception as ex:
            print("DSU file doesn't follow the Profile format.")
            break
        if not dsufile.endswith(".dsu"):  # if file isn't DSU file
            print("ERROR")
            my_path = get_path(dsufile)
        else:
            f = open(dsufile)
            print(dsufile, "opened!")
            break
    return profile_O, myPath


def command_E(my_path, command_list, profile):
    """
    Function summary:
    Parameters:
    Return value:
    """

    dictionary = user_input_dict(command_list)

    for command, text in dictionary.items():
        # ensuring whitespace or empty strings aren't added
        if isinstance(text, int) or not check_if_only_space(text):
            if command == "-usr":  # add username to dsu file
                if whitespace_checker(text):  # username contains whitespace
                    print("Username won't be added. There is whitespace.")
                    break  # breaking out of loop so options after are not run
                else:
                    profile.username = text
            elif command == "-pwd":  # add password to dsu file
                if whitespace_checker(text):
                    print("Password won't be added. There is whitespace.")
                    break  # breaking out of loop so options after are not run
                else:
                    profile.password = text
            elif command == "-bio":  # add bio to dsu file
                profile.bio = text
            elif command == "-addpost":  # add post to dsu file
                post = Profile.Post()  # create post obj w entry & timestamp
                post.entry = text
                post.timestamp = post.timestamp
                profile.add_post(post)
            elif command == "-delpost":  # delete post from dsu file
                profile.del_post(text)  # text = index
            profile.save_profile(my_path)
        else:  # text is all whitespace or is an empty string
            print("Invalid input.")
            break


def command_P(my_path, command_list, profile):
    """
    Function summary:
    Parameters:
    Return value:
    """
    while True:
        dictionary = user_input_dict(command_list)  # {"-pwd": "", "-post": #}
        for command, text in dictionary.items():
            if command == "-usr":
                print(f'Username: {profile.username}')
            elif command == "-pwd":
                print(f'Password: {profile.password}')
            elif command == "-bio":
                print(f'Bio: {profile.bio}')
            elif command == "-posts":
                print(f'All posts: {profile.get_posts()}')
            elif command == "-post":
                post_list = profile.get_posts()
                for i in range(len(post_list)):
                    if i == text:  # index matches
                        print(f'Post at index {i}: {post_list[i]}')
            elif command == "-all":
                print(f'Username: {profile.username}', end='')
                print(f'\nPassword: {profile.password}', end='')
                print(f'\nBio: {profile.bio}', end='')
                print(f'\nAll posts: {profile.get_posts()}')
        break


def user_input_dict(command_list):  # creating dict
    """
    Function summary:
    Parameters:
    Return value:
    """
    my_dict = {}
    commands = []
    texts = []
    text = ""
    listt = command_list[1:]
    for i in range(len(listt)):  # ignore E & P
        # get commands & options in a dict
        if listt[i].startswith("-"):
            commands.append(listt[i])
            if listt[i] == '-delpost':
                text = int(listt[i+1])  # get index
                texts.append(text)
                text = ""
            elif listt[i] == '-post':
                text = int(listt[i+1])  # get index
                texts.append(text)
                text = ""
            elif listt[len(listt)-1].startswith("-"):
                texts.append(text)  # text = "", last elem is command
            elif command_list[0] == "P":  # commands w no index in b/w
                texts.append(text)
            else:  # append the text after the command
                texts.append(listt[i+1])
        elif not listt[i].startswith("-") and not listt[i].isnumeric():
            text += " " + listt[i]  # still add in b/w entries
    my_dict = dict(zip(commands, texts))
    return my_dict


def get_path(dsufile):
    """
    Function summary:
    Parameters:
    Return value:
    """
    user_command = input()  # keep on asking for input
    command_list = user_command.split()
    my_path = Path(command_list[1])
    return my_path


def get_path_parts(my_path):
    """
    Function summary:
    Parameters:
    Return value:
    """
    p = PurePath(my_path)
    dir_tuple = p.parts[1:]  # getting parts of dir (ignoring C:\)
    dsufile = dir_tuple[len(dir_tuple)-1]
    return dsufile


def whitespace_checker(text):
    """
    Function summary:
    Parameters:
    Return value:
    """
    return text.isspace() or text == "" or " " in text


def check_if_only_space(text):
    """
    Function summary:
    Parameters:
    Return value:
    """
    return text == "" or text.isspace()


def whitespace_string(text):
    """
    Function summary:
    Parameters:
    Return value:
    """
    return text == "" or text.isspace() or text == " "


def post_to_server():
    """
    Function summary:
    Parameters:
    Return value:
    """
    profile = Profile.Profile()  # creating profile obj

    try:
        profile.load_profile(get_path_with_file())  # load a profile
    except Exception:  # profile doesn't exist
        if profile.dsuserver is None:  # no value set to dsuserver
            DSP_server = input("Enter a DSP server to send journal entries: ")
            profile.dsuserver = DSP_server  # storing IP address of DSP server
    else:  # runs if except is not hit
        DSP_server = profile.dsuserver

    username = input("Enter a username for your post: ")
    profile.username = username

    password = input("Enter a password for your post: ")
    profile.password = password

    profile.save_profile(get_path_with_file())  # save dsu server, username, & password

    bio = input("Enter an optional bio for your post: ")
    if not whitespace_string(bio):  # don't send empty bios
        profile.bio = bio

    only_bio = input("Would you like to only send bio? If so, type 'yes': ")
    if only_bio == 'yes':
        if not whitespace_string(bio):  # bio isn't whitespace
            ds_client.send(DSP_server, 3021, username, password, None, bio)
    else:
        # only prompt user for msg when needed
        keywords()  # inform user of keyword options
        message = input("Enter a message for your post: ")
        message = message_check(message)

        if not whitespace_string(message):  # don't send empty posts
            post = Profile.Post()  # create post obj w entry & timestamp
            post.entry = message
            post.timestamp = post.timestamp
            profile.add_post(post)

        if whitespace_string(bio):  # bio is whitespace, message is not
            ds_client.send(DSP_server, 3021, username, password, message)
        elif not whitespace_string(message) and not whitespace_string(bio):
            # bio & message is not whitespace
            ds_client.send(DSP_server, 3021, username, password, message, bio)
        else:
            print("Message is whitespace or empty. Post will not be sent.")


def get_path_with_file():
    """
    Function summary:
    Parameters:
    Return value:
    """
    path = str(Path.cwd())
    if "C:" in path:
        path = path.replace("C:", "")
    path += "\\file.dsu"
    return path


def message_check(message):
    """
    Function summary:
    Parameters:
    Return value:
    """
    if "@weather" in message:
        zipcode = input("Enter a zipcode: ")  # "92697"
        ccode = input("Enter a country: ")  # "US"
        apikey = input("Enter a valid apikey: ")  # "2e3c48c013d9e78fe6363ee699b838db"

        weather = ow.OpenWeather(zipcode, ccode, apikey)
        weather.load_data()
        message = weather.transclude(message)
    elif "@lastfm" in message:
        apikey = input("Enter a valid apikey: ")  # "8a89f4b3dde9fabe1782f291b0d7a2c1"
        track_num = input("Enter a track number between 1-50: ")

        lastfm = lfm.LastFM(track_num, apikey)
        lastfm.load_data()
        message = lastfm.transclude(message)
    return message


def keywords():
    """
    Function summary:
    Parameters:
    Return value:
    """
    print("Optional keywords to add to post:")
    print("- @weather")
    print("- @lastfm")
