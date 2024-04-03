def Open(file_name, mode):

    try:

        file = open(file_name, mode)

    except:

        print("File", file_name, "wasn't opened!")

        return None

    else:

        print("File", file_name, "was opened!")

        return file

file1_name = "TF2_1.txt"

file2_name = "TF2_2.txt"

file_1_w = Open(file1_name, "w")

if(file_1_w != None):

    file_1_w.write("Ostapenko, how to make all text uppercase")

    print("Information was succesfully added to TF2_2.txt!")

    file_1_w.close();

    print("File TF2_1.txt was closed!")

file_2_r = Open(file1_name, "r")

file_2_w = Open(file2_name, "w")

if file_2_r != None or file_2_w != None:

    for block in file_2_r.read().split(", "):

        for word in block.split(" "):

          if word.isprintable():

             file_2_w.write(word + '\n');

    file_2_r.close()

    file_2_w.close()

    print("Files were closed!")

print("New sequence:")

file_3_r = Open(file2_name, "r")

if file_3_r != None:

    for line in file_3_r.read().split():

        print(line)

    print("File TF2_2.txt was closed!")

    file_3_r.close()