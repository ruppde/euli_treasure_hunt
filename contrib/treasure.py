#!/usr/bin/python3 -u

# This script is part of euli

#########################################################################
# This is the one thing, you need to configure:
next_place = 'in your largest cooking pot'

#########################################################################

# Import modules for CGI handling
import cgi, cgitb

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
token = form.getvalue('token')

with open('tokens.txt') as f:
    filetokens = f.read().splitlines()

with open('usedtokens.txt') as f:
    usedtokens = f.read().splitlines()

count_token = len(filetokens)
count_used = len(usedtokens)

print(
'''Content-Type: text/html

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd">
<HTML>
<HEAD>

<title>Treasure Hunt Status</title>

</HEAD>
<BODY>

<h1>Treasure Hunt Status</h1>

''')

if token:
    print('<p>Entered Secret Code: ' + token + '<br>')

    if not "Treasure-" in token:
        print('<b>Error:</b> Secret code has to begin with "Treasure-".<br>')
    else:

        good_token=False
        for filetoken in filetokens:
            if token == filetoken:
                print('<b>OK:</b> Correct secret code entered!<br>')
                good_token=True
                used = False
                for usedtoken in usedtokens:
                    if token == usedtoken:
                        print('<b><font color=red size=+1>Fail:</font></b> ... but this code was already entered, not counted.<br>')
                        used = True
                        break
                if not used:
                    count_used += 1
                    try:
                        with open('usedtokens.txt', 'a') as f:
                            f.write(token + '\n')
                    except:
                        print('cant open file')
                        raise
                    print('<b><font color=green>Hurray:</font></b> Secret code counted!<br>')
        if good_token==False:
            print('<b><font color=red>Fail:</font></b>Wrong code (typo?)<br>')
                        


print('<p>Status: ' + str(count_used) + ' of ' + str(count_token) + ' secret codes found.<br>')

# Think about giving them the solution after 95% of the tokens to not break the game if one gets lost
if count_used >= count_token -1:
    print('<p>Hurray, all codes entered, here is the next stage: ' + next_place + '<br>')


# once I used an ev3-robot to fetch the amount of found tokens from the webpage and token by token pull a curtain away from a note with solution on it. A smartphone was pointed at it and 
# logged in the videochat with the name "treasure progress". 
#print('<p>Den Fortschritt auf dem Weg zum Schatz findet Ihr im Video-Chat im Fensterle von "Schatz-Versteck"!<br>')

print('''
<h3>Enter secret code:</h3>

<form action = "/treasure.py" method = "post">
Secret code: <input type = "text" name = "token">

<input type = "submit" value = "Submit" />
</form>
</BODY>
</HTML>
''')

