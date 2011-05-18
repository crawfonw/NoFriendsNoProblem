import os

for f in os.listdir(os.getcwd()):
    if '.po' in f:
        print 'Generating .mo for %s: ' % f
        os.popen('msgfmt %s -o %s' % (f, f.replace('.po', '.mo')))
