import sys


def main():
    try:
        from xsdata.cli import cli

        cli()
    except ImportError:
        print('Install cli requirements "pip install xsdata[cli]"')
        sys.exit(1)


if __name__ == "__main__":
    main()
