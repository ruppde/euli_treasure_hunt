#!/usr/bin/python3 -u

# CGI script which doesn't give the secret unless the GET parameter "admin" is changed from False to True
# Put on your own webserver/raspi
# Players need to get the URL containing the available parameters, e.g. printed in a message or QR code
# http://example.com/treasure/vault.py?cowsay=Cow_says_moo&admin=False

# If you can't install cowsay on your webserver, uncomment that part, it's just decoration

#########################################
# configure secret here:
secret ='The last number is 6'
#########################################

import cgi
import cgitb; cgitb.enable()  # for troubleshooting
import re
import os

def poor_mans_cowsay(text):

    print("<pre><font size=+2>")
    length=len(text)
    print('  ' + '_' * length)
    # yeah, that's xss injectable, let's not care around here (or make it a challenge ;)
    print('&lt; ' + text + ' &gt;')
    print('  ' + '-' * length)


    print("""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\\
                ||----w |
                ||     ||
</pre>""")


print("Content-type: text/html")
print()

print ("""
<html>

<head><title>Secret Vault</title></head>

<body>

  <h3> Secret Vault, only for admins!!! </h3>
""")




form = cgi.FieldStorage()
admin = form.getvalue("admin")
cowsay = form.getvalue("cowsay")
print('admin:' + admin )

if admin=='True':
    print('You are an admin, take a SECRET cow:')
    poor_mans_cowsay('Well done! ' + secret)
else:
    # no admin:
    print('You are not an admin, take a cow:')
    poor_mans_cowsay(cowsay)
    



print("<p>&nbsp;<p><font size=-2>Well, and how do you become an admin now?!")
#print("<p>&nbsp;<p><font size=-2>Tja, wie und wo fiddelt man sich jetzt zum Admin?!")

print (
"""
</body>

</html>
"""
)

