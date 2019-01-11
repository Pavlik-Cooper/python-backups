# Mod "a" will create a file if it doesn't exist
# Mod "r+" will throw an error  if file doesn't exist

# with open("appends.txt","a") as file:
#     file.seek(0)  # try to move cursor to the beginning -- seek wont't work
#     file.write("Second Twas brillig, and the slithy toves\n")
#     file.write("seek() method does not work with a mode\n")


with open("appends_r+.txt","r+") as file:
    file.write("Twas brillig, and the slithy toves\n")
    file.write("Second Twas brillig, and the slithy toves\n")
    # file.seek(0)
    file.write("First Twas brillig, and the slithy toves\n")