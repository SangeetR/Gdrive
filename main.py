from auth import *
import pyperclip


def main():
    service = gauth()
    id = get_id(pyperclip.paste())
    dwnld(service, id)

if __name__ == '__main__':
    main()