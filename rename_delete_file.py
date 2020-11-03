#!/bin/env python3
import os


def delete_file(end_file1, end_file2):
    for f in os.listdir():
        if not f.startswith('.'):
            if os.path.isdir(f):
                os.chdir(f)
                for r in os.listdir():
                    if r.endswith(end_file1) or r.endswith(end_file2):
                        os.remove(r)
                os.chdir('..')


def rename_file(end_file, new_end):
    for f in os.listdir():
        if not f.startswith('.'):
            if os.path.isdir(f):
                os.chdir(f)
                for r in os.listdir():
                    if r.endswith(end_file):
                        rs = r.split('-')[0]
                        n = rs + new_end # '-2020-11-02.conf'
                        os.rename(r, n)
                os.chdir('..')

end_file1 = '11-02.conf'
end_file1 = '11-02.html'

end_file = '11-02.conf'
new_end = '-2020-11-02.conf'

# delete_file(end_file1, end_file2)
rename_file(end_file, new_end)
