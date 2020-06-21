#!/usr/bin/python3 -u

# This script is part of euli

#########################################################################
# This is the one thing, you need to configure:
next_place = 'in Eurem größten Kochtopf'

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

<title>Schatzsuching Status</title>

</HEAD>
<BODY>

<h1>Schatzsuching Status</h1>

''')

if token:
    print('<p>Eingegebener Geheim-Code: ' + token + '<br>')

    if not "Schatz-" in token:
        print('<b>Fehler:</b> Geheim-Code muss mit "Schatz-" anfangen.<br>')
    else:

        good_token=False
        for filetoken in filetokens:
            if token == filetoken:
                print('<b>Fein:</b> Richtiger Geheim-Code eingegeben!<br>')
                good_token=True
                used = False
                for usedtoken in usedtokens:
                    if token == usedtoken:
                        print('<b><font color=red size=+1>Zonk:</font></b> ... aber leider wurde der schon mal eingegeben, wird nicht gewertet.<br>')
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
                    print('<b><font color=green>Hurra:</font></b> Geheim-Code wurde gewertet!<br>')
        if good_token==False:
            print('<b><font color=red>Zonk:</font></b>Falscher Geheim-Code<br>')
                        


print('<p>Euer aktueller Stand: ' + str(count_used) + ' von ' + str(count_token) + ' Geheim-Codes gefunden <br>')

# Think about giving them the solution after 95% of the tokens to not break the game if one gets lost
if count_used >= count_token -1:
    print('<p>Hurra, hier ist Eure nächste Station: ' + next_place + '<br>')


# once I used an ev3-robot to fetch the amount of found tokens from the webpage and token by token pull a curtain away from a note with solution on it. A smartphone was pointed at it and 
# logged in the videochat with the name "treasure progress". 
#print('<p>Den Fortschritt auf dem Weg zum Schatz findet Ihr im Video-Chat im Fensterle von "Schatz-Versteck"!<br>')

print('''
<h3>Gefundenen Code eingeben:</h3>

<form action = "/schatz.py" method = "post">
Geheim-Code: <input type = "text" name = "token">

<input type = "submit" value = "Eingeben" />
</form>
</BODY>
</HTML>
''')

