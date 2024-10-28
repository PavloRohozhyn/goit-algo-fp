# task3.py

def test():
    pass

# Main
if __name__ == '__main__':
    try:
        test()
    except (ValueError) as e:
        print(f'Something went wrong, {e}')
        sys.exit(0)
