arr_fonts = [
    "0. Arabic Style Font. This is the default font.",
    "1. African culture font.",
    "2. Blackletter Font used for Western European/Hungarian/Croatian/Breton cultures (excluding Celtic).",
    "3. Indian cultures",
    "4. Runic font used for Norse/Turkic/Mogyer/Finno-Uralic cultures",
    "5. Old Church Slavonic style font used for East and South Slavic",
    "6. Insular style font used for Gaelic cultures (in the 867 version of the mod it is used for all cultures on the british isles)",
    "7. Greek/Byzantine font.",
    "8. Chinese font",
    "9. Jewish Hebrew inspired font",
    "10. Mongolian font",
    "11. Tibetan inspired font",
    "12. Coptic font for Ethiopian/Armenian cultures",
    "13. Georgian font for Georgian cultures ... to be implemented",
    "14. Visgothic font for the Visigoth culture (only used in the 867 version of the mod, in the 1066 version of the mod it appears as style 1"
]
s_pause = "Press Enter to Continue!"
s_modName = "Dynamic Cultural Fonts [1066 Style]"
s_intro = f"""Hello! If you're using this program, you must be using the Crusader Kings III
mod {s_modName} and want change the name of your title,
or otherwise fix it to use a certain font. The process is a bit lengthy,
so I've written a script to make it quick and simple!

Just follow the instructions and you should be good to go.
"""

s_instr_1 = f"""First, select the font you want to use! (For instance, for Runic font, type '4' and press enter.)

{arr_fonts[0]}
{arr_fonts[1]}
{arr_fonts[2]}
{arr_fonts[3]}
{arr_fonts[4]}
{arr_fonts[5]}
{arr_fonts[6]}
{arr_fonts[7]}
{arr_fonts[8]}
{arr_fonts[9]}
{arr_fonts[10]}
{arr_fonts[11]}
{arr_fonts[12]}
{arr_fonts[13]}
{arr_fonts[14]}
"""

s_instr_2 = "Now type the name of the title!"

s_instr_3 = """Done! Just copy your title below and paste it into Crusader Kings III!
Don't worry if it doesn't look right -- it will in CK3!"""

def cls():
    print("\n"*100)

# Program Start
cls()
print(s_intro)
input(s_pause)
cls()

# Get Font
while True:
    print(s_instr_1)
    user_font = input()
    try:
        user_font = int(user_font)
    except:
        user_font = ''
    if (user_font != '' and user_font >= 0 and user_font < len(arr_fonts)):
        break
    cls()
    print("Incorrect Input")

cls()

# Get Title
print(s_instr_2)
user_title = input()

# Convert Characters
arr_unicode = [0] * len(user_title)
for i in range(len(user_title)):
    arr_unicode[i] = int(ord(user_title[i]))
    arr_unicode[i] = arr_unicode[i] + (1000 * user_font)

user_title = ""
for i in range(len(arr_unicode)):
    user_title = user_title + chr(arr_unicode[i])

cls()

# Return Title
print(s_instr_3)
print(user_title)

input(s_pause)
