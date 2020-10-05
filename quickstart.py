from auth import *
import click
import time

## remove glitch

@click.command()
@click.argument('link')
def main(link):
    service = gauth()
    # id = get_id(input("Please Enter the link........\n"))
    click.echo("We will start downloading in a while")
    id = get_id(str(link))
    dwnld(service, id)

if __name__ == '__main__':
    main()
    """
    count = 0 
    try:
            main()
    except ConnectionResetError:
        time.sleep(2)
        count += 1
        print("We are retrying .....")
        if count<=10:
            
    except:
        print("Bad LUCK ........ Error ")
    """




