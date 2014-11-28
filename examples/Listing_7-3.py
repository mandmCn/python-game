# Listing_7-3.py
# easygui text box

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",)
easygui.msgbox ("You entered " + flavor)