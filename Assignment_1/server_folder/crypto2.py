import os

def get_size(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

# plain text -> simply returns without encrypting or decrypting the file's content
def plain_text_encode(file):
    return
def plain_text_decode(file):
    return

# transpose (reverse)
def transpose_encode_decode(file):
    curr_file = file.split('.')
    f1 = open(curr_file[0] + '1' + curr_file[1], 'w')
    f2 = open(file, 'r')

    for each_line in f2:
        each_word = each_line.split()
        for i in range(len(each_word)):
            word = each_word[i]
            f1.write(word[::-1])
            if (i != len(each_word) - 1):
                f1.write(' ')
        f1.write('\n')

    fsize = get_size(f1)
    f1.truncate(fsize - 1)
    f1.close()
    f2.close()
    os.remove('./' + file)
    os.rename('./' + curr_file[0] + '1' + curr_file[1], './' + file)

# Substitue (Caesor cypher)
def substitute_encode(file):
    curr_file = file.split('.')
    f1 = open(curr_file[0] + '1' + curr_file[1], 'w')
    f2 = open(file, 'r')

    f3 = f2.read(1)
    while f3:
        f1.write(chr((ord(f3) + 2) % 256))
        f3 = f2.read(1)

    f1.close()
    f2.close()
    os.remove('./' + file)
    os.rename('./' + curr_file[0] + '1' + curr_file[1], './' + file)


def substitute_decode(file):
    curr_file = file.split('.')
    f1 = open(curr_file[0] + '1' + curr_file[1], 'w')
    f2 = open(file, 'r')

    f3 = f2.read(1)
    while f3:
        f1.write(chr((256 + ord(f3) - 2) % 256))
        f3 = f2.read(1)

    f1.close()
    f2.close()
    os.remove('./' + file)
    os.rename('./' + curr_file[0] + '1' + curr_file[1], './' + file)



