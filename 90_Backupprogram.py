#!/usr/bin/env python3

import time
import os
import tarfile
import hashlib
import pickle

#  1、既要可以实现完全备份，又要实现增量备份
#  2、完全备份时，将目录打个tar包，计算每个文件的md5值
#  3、增量备份时，备份有变化的文件和新增加的文件，更新md5值

def check_md5(fanme):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while True:
            data = fobj.read(4096)
            if not data:    
                break
            m.update(data)                
    return m.hexdigest()

def full_backup(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir.rstrip('/'))
    fname = '%s_full_%s.tar.gz' % (fname,time.strftime('%Y%m%d'))
    fname = os.path.join(dst_dir,fname)
    md5file = {}
    tar = tarfile.open(fname,'w:gz')
    tar.add(src_dir)
    tar.close()
    for path,folders,files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)
    with open(md5file,'wb') as fobj:
        pickle,dump(md5dict,fobj)

def incr_backup(src_dir,dst_dir,md5file):
    fname = os.path.basename(src_dir,rstrip('/')) 
    fname = '%s_incr_%s.tar.gz'  % (fname,time,strftime('%Y%m%d')
    fname = os.path.join(dst_dir,fname)
    md5dict = {}
    
    with open(md5file,'rb') as fobj:
        oldmd5 = pickle.load(fobj)
    for  path,folders,files in os.walk(src_dir):
        for each_file in files:
            key = os.path.join(path,each_file)
            md5dict[key] = check_md5(key)
    
    with open(md5file,'wb') as fobj:
        pickle.dump(md5dict,fobj)

    tar = tarfile.open(fname,'w:gz')
    for key in md5dict:
        if oldmd5.get(key) != md5dict[key]:
            tar.add(key)
    tar.close()

if __name__ == '__main__':
    src_dir = '/tmp/demo/security'
    dst_dir = '/var/tmp/backup'  
    md5file = '/var/tmp/backup/md5.data'
    if time.strftime('%a') == 'Mon':
        full_backup(src_dir,dst_dir,md5file)
    else:
        incr_backup(src_dir,dst_dir,md5file)









    
