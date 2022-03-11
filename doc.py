import click


@click.command()
@click.argument('string')
def add_to_database(string):
    print(string, "by python3")


if __name__ == '__main__':
    add_to_database()
