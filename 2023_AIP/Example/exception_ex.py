def main():
    try:
        fileName = input("Enter the name of a file: ")
        infile = open(fileName, 'r')
        num = float(infile.readline())
        print(1 / num)
    # except FileNotFoundError as exc1:
    #     print('FileNotFoundError')
    #     print(exc1)
    # except TypeError as exc2:
    #     print('TypeError')
    #     print(exc2)
    # except ZeroDivisionError as exc3:
    #     print('ZeroDivisionError')
    #     print(exc3)

    except Exception as exc: # 뭔 에러인지 모를땐 ... 
        print('{} is occured'.format(exc.__class__.__name__))
        print(exc)

    else:
        print('No error occured')
    finally:
        infile.close()
        print('Try statement is finished')

    

main()