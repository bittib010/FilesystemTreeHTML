import os, sys
from stat import *

root_dir = 'C:\\Users\\Skaft\\Desktop\\'


print(os.listdir(root_dir))


def walktree(top):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            print('<details class="tab"><summary><img class="icon" src="folder.jpg">{}/ </summary>'.format(f))
            walktree(pathname)
            print('</details>')
        elif S_ISREG(mode):
            print('\t<span class="tab"> <img class="icon" src="file.jpg">{} </span><br>'.format(f))
        else:
            # Unknown file type, print a message
            print('************************************** UNKNOWN FILETYPE %s' % pathname)


if __name__ == '__main__':
    walktree(root_dir)
