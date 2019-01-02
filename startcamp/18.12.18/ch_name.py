import os

# os.chdir(r"C:\TIL\dummy")
# for filename in os.listdir("."):
#     os.rename(filename, "SAMSUNG_" + filename)


os.chdir(r"C:\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG", "SSAFY"))