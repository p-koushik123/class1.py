try:
    klu1 = open("file.txt","w+")
    try:
        klu1.write("xyz This is s17 Section CRT Class")
    finally:
        klu1.close()
except IOError:
    print("File not found")
else:
    print(" The File opened successfully ")
    klu1.close()