#!/usr/bin/env python3


src_fname = '/bin/ls'

dest_fname = 'jials'

with open(src_fname,'rb') as sf:
     with open(dest_fname,'wb') as df:
          while True:
                data = sf.read(4096)
                if not data:
                    break
                df.write(data)   



