# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 12:27:29 2019

@author: DH319684
"""

import hashlib
import os

def md5(f):
#takes file f as an argument and generates an md5checksum
    return hashlib.md5(open(f,'rb').read()).hexdigest()

def rm_dup(path):
#relies on the md5 function above to remove duplicate files
    if not os.path.isdir(path):
        print('Incorrect directory path')
    else:
        md5_dict={}
        for root, dirs, files in os.walk(path):
        #os.walk for checking sub-directories
            for f in files:
                if not md5(os.path.join(root,f)) in md5_dict:
                    md5_dict.update({md5(os.path.join(root,f)):[os.path.join(root,f)]})
                else:
                    md5_dict[md5(os.path.join(root,f))].append(os.path.join(root,f))
        for key in md5_dict:
            while len(md5_dict[key])>1:
                for item in md5_dict[key]:
                    os.remove(item)
                    md5_dict[key].remove(item)
        print('Deletion successful!')
# Logic: If two files have same md5checksum, remove one.
if __name__=='__main__':
    path=input(r'Please provide the target path\directory')
    print()
    rm_dup(path)