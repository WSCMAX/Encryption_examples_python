#!/usr/bin/env python
import sys
def encrypt(list, shift):
    encrypt=[]
    while True:
        try:
            for string in list:
                cipher = ''
                for char in string:
                    if not ((65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)):
                        cipher = cipher + char
                    elif char.isupper():
                        cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
                    else:
                        cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
                encrypt.append(cipher)
            print('encryption complere!')
            return(encrypt)
            break
        except OSError as err:
            print("OS error: {0}".format(err))
        except ValueError:
            print("Could not convert.")
        except TypeError as err:
            print("TypeError: {0}".format(err))
            return(0)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise


def file_w(w_list,filename):
    while True:
        try:
            with open(filename, 'w') as f:
                for item in w_list:
                    f.write("%s\n" % item)
            f.close
            print(filename,' write successfule')
            return()
            break
        except OSError as err:
            print("OS error: {0}".format(err))
            return()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            return()

def file_r(filename):
    text_list=[]
    while True:
        try:
            with open(filename, 'r') as myfile:
                for line in myfile:
                    text_list.append(line)
            if myfile.close:
                print(filename," is closed")
            else:
                myfile.close
                print(filename," is closed")
            return(text_list)
            break
        except OSError as err:
            print("OS error: {0}".format(err))
            return(0)
def main():
    s=100005
    stringlist=file_r(sys.argv[1])
    file_w(encrypt(stringlist,int(sys.argv[3])),sys.argv[2])
    return()

if __name__ == "__main__":
    main()
SystemExit(0)