import os


MODULE = 'OldMaid'
s = ''

for f in os.listdir(os.getcwd() + '/src'):
    if MODULE in f and 'Test' not in f and '.pyc' not in f:
        print 'Processing %s: ' % f
        s += 'src/%s ' % f
        
print 'Generating message.pot file'
os.popen('pygettext %s' % s)
