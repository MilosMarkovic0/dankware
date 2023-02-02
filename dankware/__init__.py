###################################################################################

#                            https://github.com/SirDank                            

###################################################################################

# > Please read the documentation on github before using this module!

import os
import sys
import time
import random
import requests
from datetime import datetime
from colorama import Fore, Style
from traceback import extract_tb
from alive_progress import alive_bar
from concurrent.futures import ThreadPoolExecutor, as_completed

# colorama colours

black = Fore.BLACK + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
red = Fore.RED + Style.BRIGHT
reset = Style.RESET_ALL
white = Fore.WHITE + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT

# dankware variables

chars = ['>','<','.',',','=','-','_','?','!','|','(',')','{','}','/','\\',':','"',"'"]
words_green = ['true', 'True', 'TRUE', 'online', 'Online', 'ONLINE', 'successfully', 'Successfully', 'SUCCESSFULLY', 'successful', 'Successful', 'SUCCESSFUL', 'success', 'Success', 'SUCCESS']
words_red = ['falsely', 'Falsely', 'FALSELY', 'false', 'False', 'FALSE', 'offline', 'Offline', 'OFFLINE', 'failures', 'Failures', 'FAILURES', 'failure', 'Failure', 'FAILURE', 'failed', 'Failed', 'FAILED', 'fail', 'Fail', 'FAIL']
colours_to_replace = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW, Style.BRIGHT, Style.RESET_ALL]
colours_alt = ["BBLACKK", "BBLUEE", "CCYANN", "GGREENN", "MMAGENTAA", "RREDD", "WWHITEE", "YYELLOWW", "BBRIGHTT", "RRESETT"]
bad_colours = ['BLACK', 'WHITE', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'RESET']
codes = vars(Fore); colours = [codes[colour] for colour in codes if colour not in bad_colours]
#styles = [Style.BRIGHT, Style.DIM, Style.NORMAL]
available_colours = ['black','red','green','cyan','blue','purple','random','black-v','red-v','green-v','cyan-v','blue-v','purple-v','pink-v']

excluded_prefixes_one = ['6.', '7.', '10.', '11.', '21.', '22.', '26.', '28.', '29.', '30.', '33.', '55.', '127.', '136.', '205.', '214.', '215.']
excluded_prefixes_two = ['23.27.', '31.25.', '50.117.', '74.115.', '75.127.', '81.87.', '100.64.', '128.16.', '128.40.', '128.41.', '128.86.', '128.232.', '128.240.', '128.243.', '129.11.', '129.12.', '129.31.', '129.67.', '129.123.', '129.169.', '129.215.', '129.234.', '130.88.', '130.159.', '130.209.', '130.246.', '131.111.', '131.227.', '131.231.', '131.251.', '134.36.', '134.83.', '134.151.', '134.219.', '134.220.', '134.225.', '136.148.', '136.156.', '137.44.', '137.50.', '137.73.', '137.108.', '137.195.', '137.222.', '137.253.', '138.38.', '138.40.', '138.250.', '138.253.', '139.133.', '139.153.', '139.166.', '139.184.', '139.222.', '140.97.', '141.163.', '141.241.', '142.111.', '142.252.', '143.52.', '143.117.', '143.167.', '143.210.', '143.234.', '144.32.', '144.39.', '144.82.', '144.124.', '144.173.', '146.87.', '146.97.', '146.169.', '146.176.', '146.179.', '146.191.', '146.227.', '147.143.', '147.188.', '147.197.', '148.79.', '148.88.', '148.197.', '149.155.', '149.170.', '150.204.', '152.71.', '152.78.', '152.105.', '153.11.', '155.198.', '155.245.', '157.140.', '157.228.', '158.94.', '158.125.', '158.143.', '158.223.', '159.92.', '160.5.', '160.9.', '161.73.', '161.74.', '161.76.', '161.112.', '163.1.', '163.119.', '163.160.', '163.167.', '164.11.', '165.160.', '166.88.', '169.254.', '172.252.', '192.168.', '192.177.', '192.186.', '193.60.', '194.66.', '194.80.', '195.194.', '198.18.', '205.164.', '212.121.', '212.219.']
excluded_prefixes_three = ['4.53.201.', '5.152.179.', '8.12.162.', '8.12.163.', '8.12.164.', '8.14.84.', '8.14.145.', '8.14.146.', '8.14.147.', '8.17.250.', '8.17.251.', '8.17.252.', '23.231.128.', '31.25.2.', '31.25.4.', '37.72.112.', '37.72.172.', '38.72.200.', '46.254.200.', '50.93.192.', '50.93.193.', '50.93.194.', '50.93.195.', '50.93.196.', '50.93.197.', '50.115.128.', '50.118.128.', '63.141.222.', '64.62.253.', '64.92.96.', '64.145.79.', '64.145.82.', '64.158.146.', '65.49.24.', '65.49.93.', '65.162.192.', '66.79.160.', '66.160.191.', '68.68.96.', '69.46.64.', '69.176.80.', '72.13.80.', '72.52.76.', '74.82.43.', '74.82.160.', '74.114.88.', '74.115.2.', '74.115.4.', '74.122.100.', '85.12.64.', '89.207.208.', '92.245.224.', '103.251.91.', '108.171.32.', '108.171.42.', '108.171.52.', '108.171.62.', '118.193.78.', '130.93.16.', '132.206.9.', '132.206.123.', '132.206.125.', '141.170.64.', '141.170.96.', '141.170.100.', '146.82.55.93', '149.54.136.', '149.54.152.', '159.86.128.', '173.245.64.', '173.245.194.', '173.245.220.', '173.252.192.', '178.18.16.', '178.18.26.', '178.18.27.', '178.18.28.', '178.18.29.', '183.182.22.', '185.83.168.', '192.12.72.', '192.18.195.', '192.35.172.', '192.41.104.', '192.41.112.', '192.41.128.', '192.68.153.', '192.76.6.', '192.76.8.', '192.76.16.', '192.76.32.', '192.82.153.', '192.84.5.', '192.84.75.', '192.84.76.', '192.84.80.', '192.84.212.', '192.88.9.', '192.88.10.', '192.88.99.', '192.92.114.', '192.94.235.', '192.100.78.', '192.100.154.', '192.107.168.', '192.108.120.', '192.124.46.', '192.133.244.', '192.149.111.', '192.150.180.', '192.150.184.', '192.153.213.', '192.155.160.', '192.156.162.', '192.160.194.', '192.171.128.', '192.171.192.', '192.173.1.', '192.173.2.', '192.173.4.', '192.173.128.', '192.188.157.', '192.188.158.', '192.190.201.', '192.190.202.', '192.195.42.', '192.195.105.', '192.195.116.', '192.195.118.', '192.249.64.', '192.250.240.', '193.32.22.', '193.37.225.', '193.37.240.', '193.38.143.', '193.39.80.', '193.39.172.', '193.39.212.', '193.107.116.', '193.130.15.', '193.133.28.', '193.138.86.', '194.32.32.', '194.35.93.', '194.35.186.', '194.35.192.', '194.35.241.', '194.36.1.', '194.36.2.', '194.36.121.', '194.36.152.', '194.60.218.', '194.110.214.', '194.187.32.', '198.12.120.', '198.12.121.', '198.12.122.', '198.51.100.', '198.144.240.', '199.33.120.', '199.33.124.', '199.48.147.', '199.68.196.', '199.127.240.', '199.187.168.', '199.188.238.', '199.255.208.', '203.12.6.', '204.13.64.', '204.16.192.', '204.19.238.', '204.74.208.', '204.113.91.', '205.159.189.', '205.209.128.', '206.108.52.', '206.165.4.', '208.77.40.', '208.80.4.', '208.123.223.', '209.51.185.', '209.54.48.', '209.107.192.', '209.107.210.', '209.107.212.', '211.156.110.', '212.121.192.', '216.151.183.', '216.151.190.', '216.172.128.', '216.185.36.', '216.218.233.', '216.224.112.']

def multithread(function, threads: int = 1, input_one = None, input_two = None, progress_bar: bool = True) -> None:
    
    """
    input one/two can be any of these: None, List, Variable
    """

    futures = []
    executor = ThreadPoolExecutor(max_workers=threads)
    one_isList = type(input_one) is list
    two_isList = type(input_two) is list
    if input_one is None: one_isNone = True
    else: one_isNone = False
    if input_two is None: two_isNone = True
    else: two_isNone = False

    if one_isNone:
        for _ in range(threads): futures.append(executor.submit(function))
    
    elif two_isNone:
        if one_isList:
            for item in input_one: futures.append(executor.submit(function, item))
        else:
            for _ in range(threads): futures.append(executor.submit(function, input_one))

    elif not one_isNone and not two_isNone:
        if one_isList and two_isList:
            if len(input_one) != len(input_two):
                print(clr(f"\n  > MULTITHREAD ERROR! - input_one({len(input_one)}) and input_two({len(input_two)}) do not have the same length!",2))
                if len(input_one) < 50 and len(input_two) < 50:
                    print(clr(f"\n  > input_one = {str(input_one)}",2))
                    print(clr(f"\n  > input_two = {str(input_two)}",2))
                sys.exit(1)
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two[index]))
        elif one_isList:
            for index in range(len(input_one)): futures.append(executor.submit(function, input_one[index], input_two))
        elif two_isList:
            for index in range(len(input_two)): futures.append(executor.submit(function, input_one, input_two[index]))
        elif not one_isList and not two_isList:
            for _ in range(threads): futures.append(executor.submit(function, input_one, input_two))

    if progress_bar:
        with alive_bar(int(len(futures)), title='') as bar:
            for future in as_completed(futures):
                try: future.result(); bar()
                except: bar()
    else:
        for future in as_completed(futures):
            try: future.result()
            except: pass

def github_downloads(user_repo: str) -> list:

    """
    
    this function extracts download urls from latest release on github and returns as list
    
    Example Input: EXAMPLE/EXAMPLE ( from https://api.github.com/repos/EXAMPLE/EXAMPLE/releases/latest )
    
    Example Output: ['https://github.com/EXAMPLE/EXAMPLE/releases/download/VERSION/EXAMPLE.TXT']
    
    """
    
    urls = []

    #if "https://api.github.com/repos/" not in url or "/releases/latest" not in url:
    #    print(clr('  > Invalid url! Must follow: "https://api.github.com/repos/NAME/NAME/releases/latest"',2))
    #    sys.exit(1)    
    while True:
        try: response = requests.get(f"https://api.github.com/repos/{user_repo}/releases/latest").json(); break
        except: input(clr("  > Make sure you are connected to the Internet! Press [ENTER] to try again... ",2))
    
    for data in response["assets"]:
        urls.append(data["browser_download_url"])

    return urls

def github_file_selector(user_repo: str, filter_mode: str, name_list: list) -> list:
    
    """
    
    This function is used to filter the output from github_downloads()
    
    user_repo = 'USER_NAME/REPO_NAME' ( from https://api.github.com/repos/USER_NAME/REPO_NAME/releases/latest )
    filter_mode = 'add' or 'remove'
    name_list = list of names to be added or removed
    
    Example output from github_downloads("EX_USER/EX_REPO"): [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
        ]
        
    ==================================================================================
    
    Example Input: "EX_USER/EX_REPO", "add", ["EXAMPLE"]
        
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/EXAMPLE_3.TXT'
        ]
        
    Note: Only urls with filenames containing "EXAMPLE" were returned.

    ==================================================================================

    Example Input: "EX_USER/EX_REPO", "remove", ["EXAMPLE"]
    
    Example Output: [
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_2.TXT'
        'https://github.com/EX_USER/EX_REPO/releases/download/VERSION/TEST_3.TXT'
        ]
    
    Note: Only urls with filenames not containing "EXAMPLE" were returned.
    
    """

    urls = []
    for file_url in github_downloads(user_repo):
        if filter_mode == "add": valid = False
        elif filter_mode == "remove": valid = True
        for name in name_list:
            if name in file_url.split('/')[-1]:
                if filter_mode == "add": valid = True
                elif filter_mode == "remove": valid = False
        if valid: urls.append(file_url)
    return urls

def random_ip() -> str:
    
    """
    generates a random valid computer ip
    [NOTE] https://github.com/robertdavidgraham/masscan/blob/master/data/exclude.conf
    """
    
    while True:

        ip = f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(0,255)}"

        if any(ip.startswith(prefix) for prefix in excluded_prefixes_one): continue
        elif any(ip.startswith(prefix) for prefix in excluded_prefixes_two): continue
        elif any(ip.startswith(prefix) for prefix in excluded_prefixes_two): continue

        if ip.startswith("172.") and int(ip.split('.')[1]) >= 16 and int(ip.split('.')[1]) <= 31: continue
        elif ip.startswith("192."):
            if ip.endswith(".170") or ip.endswith(".171") or ip.split('.')[2] == "2": continue
        elif ip.startswith("203.") and ip.split('.')[2] == "113": continue
        elif ip.startswith("216.83.") and int(ip.split('.')[2]) >= 33 and int(ip.split('.')[2]) <= 63: continue
        elif ip.endswith(".255.255.255"): continue

        break
        
    return ip

def clr(text: str, mode: int = 1, colour: str = magenta) -> str:
    
    """
    
    this function colours special characters inside the 'chars' list
    
    mode: 1 | to display general text (default)
    spl = magenta (default) / specified colour
    text = white
    
    mode: 2 | to display error messages
    spl = white
    text = red
    
    mode: 3
    spl = white
    text = random
    
    mode: 4 | to display banners
    spl & text = random
    
    """
    
    if mode != 3:
        for _ in range(len(colours_to_replace)):
            text = text.replace(colours_to_replace[_], colours_alt[_])
    else:
        for _ in range(len(colours_to_replace)):
            text = text.replace(colours_to_replace[_], '')

    # default

    if mode == 1:
        text = text.replace("[",f"{colour}[{white}").replace("]",f"{colour}]{white}")
        for char in chars: text = text.replace(char, f"{colour}{char}{white}")
        for word in words_green:
            replacement = green.join(list(word))
            text = text.replace(word, f"{green}{replacement}{white}")
        for word in words_red:
            replacement = red.join(list(word))
            text = text.replace(word, f"{red}{replacement}{white}")
    
    # for error messages
    
    elif mode == 2:
        text = text.replace("[",f"{white}[{red}").replace("]",f"{white}]{red}")
        for char in chars: text = text.replace(char, f"{white}{char}{red}")
        for word in words_green: text = text.replace(word, f"{green}{word}{red}")
    
    # random | TRUE, FALSE will not be coloured!
    
    elif mode == 3 or mode == 4:
        text = [char for char in text]
        if mode == 3: colour_spl = True
        else: colour_spl = False
        for _ in range(len(text)):
            char = text[_]
            if char != ' ' and char != '\n':
                if colour_spl:
                    if char in ( ['[',']'] + chars ): text[_] = white + char
                    else: text[_] = random.choice(colours) + Style.BRIGHT + char
                else:
                    text[_] = random.choice(colours) + Style.BRIGHT + char
        text = ''.join(text)

    else: print(str(f"\n  {white}> {red}CLR ERROR{white}! - {red}Wrong mode {white}[{red}{mode}{white}]" + reset)); sys.exit(1)

    if mode != 3:
        for _ in range(len(colours_to_replace)):
            text = str(text).replace(colours_alt[_], colours_to_replace[_])

    if mode == 1: return white + text + reset
    elif mode == 2: return red + text + reset
    elif mode == 3 or mode == 4: return text + reset

def align(text: str) -> str: 
    
    """
    center align banner / line ( supports both coloured and non-coloured )
    [NOTE] align supports: clr, does not support: fade
    """

    width = os.get_terminal_size().columns; aligned = text
    for colour in vars(Fore).values(): aligned = aligned.replace(colour,'')
    for style in vars(Style).values(): aligned = aligned.replace(style,'')
    text = text.split('\n'); aligned = aligned.split('\n')
    for _ in range(len(aligned)): aligned[_] = aligned[_].center(width).replace(aligned[_],text[_])
    return str('\n'.join(aligned) + reset)

def fade(text: str, colour: str = "purple") -> str:
    
    """
    credits to https://github.com/venaxyt/gratient & https://github.com/venaxyt/fade <3
    available_colours = [black,red,green,cyan,blue,purple,random,black-v,red-v,green-v,cyan-v,blue-v,purple-v,pink-v]
    """

    colour = colour.lower()
    if colour in available_colours: valid_colour = True
    else: valid_colour = False
    if not valid_colour: print(clr(f"\n  > FADE ERROR! - Invalid colour: {colour} | Available colours: {', '.join(available_colours)}")); sys.exit(1)
        
    faded = ""
    if len(text.splitlines()) > 1: multi_line = True
    else: multi_line = False

    if colour == "black":
        for line in text.splitlines():
            R = 0; G = 0; B = 0
            for char in line:
                R += 3; G += 3; B += 3
                if R > 255 and G > 255 and B > 255: R = 255; G = 255; B = 255
                faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
            if multi_line: faded += "\n"
            
    elif colour == "red":
        for line in text.splitlines():
            G = 250
            for char in line:
                G -= 5
                if G < 0: G = 0
                faded += f"\033[38;2;255;{G};0m{char}\033[0m"
            if multi_line: faded += "\n"
            
    elif colour == "green":
        for line in text.splitlines():
            R = 0
            for char in line:
                if not R > 200: R += 3
                faded += f"\033[38;2;{R};255;0m{char}\033[0m"
            if multi_line: faded += "\n"
            
    elif colour == "cyan":
        for line in text.splitlines():
            B = 100
            for char in line:
                B += 2
                if B > 255: B = 255
                faded += f"\033[38;2;0;255;{B}m{char}\033[0m"
            if multi_line: faded += "\n"

    elif colour == "blue":
        for line in text.splitlines():
            G = 0
            for char in line:
                G += 3
                if G > 255: G = 255
                faded += f"\033[38;2;0;{G};255m{char}\033[0m"
            if multi_line: faded += "\n"
        
    elif colour == "purple":
        for line in text.splitlines():
            R = 35
            for char in line:
                R += 3
                if R > 255: R = 255
                faded += f"\033[38;2;{R};0;220m{char}\033[0m"
            if multi_line: faded += "\n"

    elif colour == "black-v":
        R = 0; G = 0; B = 0
        for line in text.splitlines():
            faded += (f"\033[38;2;{R};{G};{B}m{line}\033[0m")
            if not R == 255 and not G == 255 and not B == 255:
                R += 20; G += 20; B += 20
                if R > 255 and G > 255 and B > 255: R = 255; G = 255; B = 255
            if multi_line: faded += "\n"
                    
    elif colour == "red-v":
        G = 250
        for line in text.splitlines():
            faded += f"\033[38;2;255;{G};0m{line}\033[0m"
            if not G == 0:
                G -= 25
                if G < 0: G = 0
            if multi_line:faded += "\n"

    elif colour == "green-v":
        R = 0
        for line in text.splitlines():
            faded += f"\033[38;2;{R};255;0m{line}\033[0m"
            if not R > 200: R += 30
            if multi_line: faded += "\n"
        
    elif colour == "cyan-v":
        B = 100
        for line in text.splitlines():
            faded += f"\033[38;2;0;255;{B}m{line}\033[0m"
            if not B == 255:
                B += 15
                if B > 255: B = 255
            if multi_line: faded += "\n"
        
    elif colour == "blue-v":
        G = 10
        for line in text.splitlines():
            faded += f"\033[38;2;0;{G};255m{line}\033[0m"
            if not G == 255:
                G += 15
                if G > 255: G = 255
            if multi_line: faded += "\n"
        
    elif colour == "purple-v":
        R = 40
        for line in text.splitlines():
            faded += f"\033[38;2;{R};0;220m{line}\033[0m"
            if not R == 255:
                R += 15
                if R > 255: R = 255
            if multi_line: faded += "\n"
        
    elif colour == "pink-v":
        B = 255
        for line in text.splitlines():
            faded += f"\033[38;2;255;0;{B}m{line}\033[0m"
            if not B == 0:
                B -= 20
                if B < 0: B = 0
            if multi_line: faded += "\n"

    elif colour == "random":
        for line in text.splitlines():
            for char in line:
                R, G, B = random.randint(0,255), random.randint(0,255), random.randint(0,255)
                faded += f"\033[38;2;{R};{G};{B}m{char}\033[0m"
            if multi_line: faded += "\n"
    
    else: print(clr(f"\n  > FADE ERROR! - [{colour}] is not supported yet!",2)); sys.exit(1)
    
    if multi_line: faded = faded[:-1]
    return faded

def get_duration(then, now = datetime.now(), interval = "default"):

    """
    Returns a duration as specified by variable interval
    Functions, except totalDuration, returns [quotient, remainder]
    """

    duration = now - then # For build-in functions
    duration_in_s = int(duration.total_seconds())
    
    def time_units(duration_in_s):
        years, rem = divmod(duration_in_s, 31536000) 
        days, rem = divmod(rem, 86400) 
        hours, rem = divmod(rem, 3600) 
        minutes, rem = divmod(rem, 60) 
        return int(years), int(days), int(hours), int(minutes), int(rem)
  
    def dynamic():
        y, d, h, m, s = time_units(duration_in_s)
        if y: return f"{y} year{'s' if y > 1 else ''}"
        elif d: return f"{d} day{'s' if d > 1 else ''}"
        elif h: return f"{h} hour{'s' if h > 1 else ''}"
        elif m: return f"{m} minute{'s' if m > 1 else ''}"
        else: return f"{s} second{'s' if s > 1 else ''}"

    def totalDuration():
        y, d, h, m, s = time_units(duration_in_s)
        return f"Time between dates: {y} year{'s' if y > 1 else ''}, {d} day{'s' if d > 1 else ''}, {h} hour{'s' if h > 1 else ''}, {m} minute{'s' if m > 1 else ''} and {s} second{'s' if s > 1 else ''}"

    return {
        'years': int(duration_in_s // 31536000),
        'days': int(duration_in_s // 86400),
        'hours': int(duration_in_s // 3600),
        'minutes': int(duration_in_s // 60),
        'seconds': int(duration_in_s),
        'dynamic': dynamic(),
        'default': totalDuration()
    }[interval]

def err(exc_info) -> str:
    
    """
    [EXAMPLE]:

    import sys
    from dankware import err, clr
    
    try: value = 1/0
    except: print(clr(err(sys.exc_info()), 2))
    """

    ex_type, ex_value, ex_traceback = exc_info
    trace_back = extract_tb(ex_traceback)
    stack_trace = []

    for trace in trace_back:
        stack_trace.append("    - File: {} | Line: {} | Function: {} | {}".format(trace[0].split('\\')[-1], trace[1], trace[2], trace[3]))
        
    report = "  > Error Type: {}".format(ex_type.__name__)
    if ex_value != '': report += "\n\n  > Error Message: \n\n    - {}".format(ex_value)
    report += "\n\n  > Error Stack Trace: \n\n{}".format('\n'.join(stack_trace))

    return report

# functions for windows executables [ dankware ]

def cls() -> None: 
    
    """
    clear screen for multi-os
    """
    
    print(reset)
    if os.name == 'nt': _ = os.system('cls')
    else: _ = os.system('clear')

def title(title: str) -> None:
    
    """
    changes title
    """

    if os.name == 'nt': os.system(f"title {title}")
    
def rm_line() -> None:
    
    """
    deletes previous line
    """

    print("\033[A                             \033[A")

def chdir(mode: str) -> str:
    
    """

    running "os.chdir(os.path.dirname(__file__))" inside example.py will change its directory to the example.py file's location
    running "os.chdir(os.path.dirname(sys.argv[0]))" inside example.exe will change its directory to the example.exe file's location (nuitka)
        
    for changing directory to exe's path as exe: exec(chdir("exe"))
    for changing directory to script's path as script: exec(chdir("script"))
    
    [NOTE] When I build executables, the [ exec_mode = "script" ] is automatically replaced with [ exec_mode = "exe" ] inside the script
    [NOTE] If you run "os.chdir(os.path.dirname(__file__))" as an executable, it will change its directory to its temp folder [ C:\\Users\\user\\AppData\\Local\\Temp\\dankware_PPID ]

    """

    if mode == "script": return "os.chdir(os.path.dirname(__file__))" # as .py
    elif mode == "exe": return "os.chdir(os.path.dirname(sys.argv[0]))" # as .exe

def sys_open(item: str) -> None:
    
    """
    - opens the url on the default browser on windows / linux
    - opens directory
    - starts file
    """
    
    if os.name == 'nt': os.system(f'start {item}')
    else: os.system(f'xdg-open {item}')

def dankware_banner() -> None:
    
    """
    dankware banner printer with github url
    """

    banner="\n 8 888888888o.     \n 8 8888    `^888.  \n 8 8888        `88.\n 8 8888         `88\n 8 8888          88\n 8 8888          88\n 8 8888         ,88\n 8 8888        ,88'\n 8 8888    ,o88P'  \n 8 888888888P'     \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n b.             8\n 888o.          8\n Y88888o.       8\n .`Y888888o.    8\n 8o. `Y888888o. 8\n 8`Y8o. `Y88888o8\n 8   `Y8o. `Y8888\n 8      `Y8o. `Y8\n 8         `Y8o.`\n 8            `Yo\n\n\n 8 8888     ,88'\n 8 8888    ,88' \n 8 8888   ,88'  \n 8 8888  ,88'   \n 8 8888 ,88'    \n 8 8888 88'     \n 8 888888<      \n 8 8888 `Y8.    \n 8 8888   `Y8.  \n 8 8888     `Y8.\n\n\n `8.`888b                 ,8'\n  `8.`888b               ,8' \n   `8.`888b             ,8'  \n    `8.`888b     .b    ,8'   \n     `8.`888b    88b  ,8'    \n      `8.`888b .`888b,8'     \n       `8.`888b8.`8888'      \n        `8.`888`8.`88'       \n         `8.`8' `8,`'        \n          `8.`   `8'         \n\n\n          .8.         \n         .888.        \n        :88888.       \n       . `88888.      \n      .8. `88888.     \n     .8`8. `88888.    \n    .8' `8. `88888.   \n   .8'   `8. `88888.  \n  .888888888. `88888. \n .8'       `8. `88888.\n\n\n 8 888888888o.  \n 8 8888    `88. \n 8 8888     `88 \n 8 8888     ,88 \n 8 8888.   ,88' \n 8 888888888P'  \n 8 8888`8b      \n 8 8888 `8b.    \n 8 8888   `8b.  \n 8 8888     `88.\n\n\n 8 8888888888   \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n 8 8888         \n 8 8888         \n 8 8888         \n 8 8888         \n 8 888888888888 \n "
    cls(); print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    for line in align(clr(banner,4)).splitlines(): time.sleep(0.05); print(line)

    num_lines = os.get_terminal_size().lines
    for _ in range(num_lines): time.sleep(0.1); print("\n")
    print(align(clr("github.com / SirDank"))); sleep_time = 0.01
    for _ in range(int(num_lines/4)): time.sleep(sleep_time); sleep_time += 0.025; print("\n")
    time.sleep(4)
    for _ in range(int(num_lines/2)+5): time.sleep(0.01); print("\n")
    cls()
