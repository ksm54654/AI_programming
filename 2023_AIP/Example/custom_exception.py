class JSException(Exception):
    def __init__(self):
        super().__init__("Jinsun's Exception")

def main():
    try:
        print('Hello')
        raise JSException
    except JSException as e:
        print(e)

main()