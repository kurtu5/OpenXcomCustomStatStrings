#!/usr/bin/python3
#
#    Instructions: You need python3 to run this.   I run this in cygwin, but there are other options.
#  If your statsStrings are in mystrings.rul then run;
#     ./Boohina_Piratez_StatStrings.py > mystrings.rul 
#
#   What does it do?   Well you ever get tired of statstrings that don't help for your gals as they
# Level and want to change them?  This removes the tedium of manually rewriting your ranges.  Lets look
# at some examples;
#
# Boohina Badass/F#br
# 
# I want F# to represent firing over 100
# 
#   # firing
#   ranges = [0, 50, 75, 90, 100, '~']
#   values = "_  =   +   *   #"
#   createStatString("firing", "F")  # The F is printed first then _,=,+,*,# as necessary.  Spaces are
#                                    # ignored to help you easily see it lines up with ranges above. 
#
# I want b to represent bravery between 40 and 50, B is for above 50 and don't show anything below 40
#
#   # bravery
#   ranges = [0, 40, 50, '~`]
#   values = "!  b   B"
#   createStatString("bravery", "")  # Notice the "", I left that out as I only want one character
#
# I want r to show bad reactions below 50 and R to show good ones above 60.  Nothing is printed between 50 and 60
#
#   # reactions
#   ranges = [0, 50, 60, '~'}
#   values = "r  !   R"
#   createStatString("reactions", "") # Notice that ! is a special character to not print itself.
#                                     # Again, I set the first character to "" as I only want one.

# Set some default values
defaultValues = "_.,-~=+*@#0123456789xxxxxxxxxxxxxxxxx"
defaultRanges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 130, 150, 160, 170, 180]
def defaults():
    global ranges
    global values
    ranges = defaultRanges
    values = defaultValue
	
# Create stats string
def createStatString(stat, string):
    valuesT = values.replace(" ", "")
    print("# stat for %s" % stat)
    if string != "":
        print("  - string: \"%s\"" % string)
        #print("    %s: [%s, %s]" % (stat, ranges[0], '~'))
        print("    %s: [%s, %s]" % (stat, ranges[0], ranges[len(ranges)-1]))
    for i in range(len(ranges)):
        try:
            char = valuesT[i]
        except:
            continue

        lower = ranges[i]
        try:
            upper = ranges[i+1]
            #print(len(ranges),i+2)
            if upper != '~' and i+2 != len(ranges):
                upper = upper - 1
        except:
            continue

        if char != '!':
            print("  - string: \"%s\"" % char)
            print("    %s: [%s, %s]" % (stat, lower, upper))
print("  statStrings:\n")


# Decent cutoffs?
# tu 95+  sta??  hlth??  brave??  react 85+  firing 100+  throw??  melee 115+  psistr/skill 50+

# tu
ranges = [0, 60, 80, 100, '~']
values = "-  +   t   T"
createStatString("tu", "")

# stamina 
ranges = [0, 30, 130, '~']
values = "s  !   S"
createStatString("stamina", "")

# health ?
ranges = [0, 60, 80, '~']
values = "h   !   H"
createStatString("health", "")

# bravery .
ranges = [0, 40, 80, '~']
values = "b   !  B"
createStatString("bravery", "")

# reactions .
ranges = [0, 70, 90, '~']
values = "!  r   R"
createStatString("reactions", "")

# firing .
ranges = [0, 50, 75, 90, 100, '~']
values = "_  =   +   *   #"
createStatString("firing", "F")

# throwing ?
ranges = [60, 70, 80, '~']
values = "+   *   #"
createStatString("throwing", "W")

# melee .
ranges = [0, 75, 90, '~']
values = "m   !  M"
createStatString("melee", "")

# strength  .
ranges = [0, 50, 75, '~']
values = "g  !   G"
createStatString("strength", "")

# psiStrength
#createStatString("psiStrength", "P")

# psiSkill
#createStatString("psiSkill", "V")
