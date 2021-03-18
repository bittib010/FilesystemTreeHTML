import os
from stat import *

# Access denied was a huge problem. This link solved it for me:
#   https://stackoverflow.com/questions/54042613/python-getting-errors-reading-directory-in-windows/54046850
# Learning about hard links and junctions. This is one of the disadvantages of the output,
# not showing hardlinks and junctions

root_dir = '/Users/adriankydlandskaftun/Documents/'



def walktree(top):
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname)[ST_MODE]
        if S_ISDIR(mode):
            print('\t<details class="tab"><summary><img class="icon" src="folder.jpg">{}/ </summary>'.format(f))
            try:
                walktree(pathname)
            except Exception as e:
                #print('!ERROR: {}, {}'.format(e, pathname))
                pass
            print('</details>')

        elif S_ISREG(mode):
            # The <p hidden> is for containing tags for searching
            # TODO: Make more visible by adding linebreaks for tooltips (to come), filenames and tags?????
            print('\t\t<span class="tab myTags"> <img class="icon" src="file.jpg">{} <p hidden> </p> </span><br>'.format(f))
        else:
            # Unknown file type, print a message
            print('************************************** UNKNOWN FILETYPE %s' % pathname)  #TODO: Check if this is outputted


if __name__ == "__main__":
    print('''
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Forensic pocket reference for file structure view</title>
        <link rel="stylesheet" type="text/css" href="stylesheet.css">
    </head>
    <body>
        <form id="searchForm" action="javascript:search();">
            <div class="input-group">
                <input type="text" id="searchItem" class="form-control" placeholder="Enter filename or any text/tag">
                <button id="go" type="button" onclick="document.getElementById('searchForm').submit(); return false;"> </button>

            </div>
        </form>
        

        ''')
    
    print('<details class="tab"><summary><img class="icon" src="folder.jpg">{}/ </summary>'.format(root_dir))
    walktree(root_dir)
    print('''
            </details>
            <script src="javascript.js"></script>
    </body>
</html>''')
