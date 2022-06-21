# Test 환경 : Ubuntu 18.04 (python 3.6.9)
import os
import hashlib

input_base_path = '/home/ubuntu/Coding/img/original/images/'        # test path (테스트 경로)
output_path = './'
upload_file = 'img116.jpg'          # test File (업로드 된 파일 넣으면 됨.)

def hashing(fname):     # hashing
    enc = hashlib.md5(fname.encode('utf-8'))     # md5 
    encText = enc.hexdigest()
    encText = encText + '.jpg'
    return encText

if __name__ == '__main__':
    hash_fname = hashing(upload_file)
    command = './mean-shift ' + input_base_path +upload_file + ' ' + output_path + hash_fname
    #print("command is : "+command)     # Debugging
    os.system(command)
    print("Done")
