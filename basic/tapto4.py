import sys

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_contents = f.read()
f.close()

space_contents = tab_contents.replace("\t", " "*4)

f = open(dst, 'w')
f.write(tab_contents)
f.close()
