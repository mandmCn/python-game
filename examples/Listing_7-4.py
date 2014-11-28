# Listing_7-4.py
# default arguments in easygui

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           argDefaultText = 'Vanilla')
easygui.msgbox ("You entered " + flavor)