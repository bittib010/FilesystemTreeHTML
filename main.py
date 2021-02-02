import os
from stat import *

# Access denied was a huge problem. This link solved it for me:
#   https://stackoverflow.com/questions/54042613/python-getting-errors-reading-directory-in-windows/54046850
# Learning about hard links and junctions. This is one of the disadvantages of the output,
# not showing hardlinks and junctions

root_dir = 'C:\\'


def walktree(top):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            print('<details class="tab"><summary><img class="icon" src="folder.jpg">{}/ </summary>'.format(f))
            try:
                walktree(pathname)
            except Exception as e:
                #print('!ERROR: {}, {}'.format(e, pathname))
                pass
            print('</details>')

        elif S_ISREG(mode):
            print('\t<span class="tab"> <img class="icon" src="file.jpg">{} </span><br>'.format(f))
        else:
            # Unknown file type, print a message
            print('************************************** UNKNOWN FILETYPE %s' % pathname)  #TODO: Check if this is outputted


if __name__ == "__main__":
    walktree(root_dir)
