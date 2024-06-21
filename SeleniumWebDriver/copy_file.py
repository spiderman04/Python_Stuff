import os

SOURCE_PATH = 'C:\\Temp\\'
TEMPLATE_FILENAME = "template.txt"
LIST_OF_NAMES = [
    'a','b','c','d'
]


def main():

    for entry in LIST_OF_NAMES:
        src = SOURCE_PATH + TEMPLATE_FILENAME
        dest = SOURCE_PATH + entry + '.txt'

        print(str(os.name))
        if os.name == 'nt':
            cmd = f'copy "{src}" "{dest}"'
            print("windows")
        elif os.name == 'posix':
            cmd = f'cp "{src} "{dest}"'
        else:
            print("OS not recognized; expecting Windows or Linux system!")
            exit

        #copy the file
        os.system(cmd)

    if __name__ == '__main__':
        main()
