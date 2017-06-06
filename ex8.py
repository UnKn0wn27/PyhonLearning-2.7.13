formatter = "%r %r %r %r"

#this awesome
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

# the single qoute in didn't will display with " " in terminal
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type right.",
    "But it didn't sing.",
    "So i said goodnight."
)
