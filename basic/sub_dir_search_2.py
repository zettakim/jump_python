import os


for (path, dirs, files) in os.walk(os.getcwd()):
    for filename in files:
        ext = os.path.splitext(filename)[-1]
        if ext == ".py":
            print("%s%s" % (path, filename))
