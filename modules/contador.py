import argparse

def check_txt(action='NaN'):
    with open('./modules/contador.txt') as f:
        data = f.read()
        if data == '':
            data = 0
        else:
            data = int(data)
        if action == 'inc':
            data += 1
        elif action == 'dec':
            data -= 1
        print(data)
    with open('./modules/contador.txt', 'w') as f:
        f.write(str(data))

if __name__ == '__main__':
    check_txt()
    parser = argparse.ArgumentParser()
    parser.add_argument('action', type=str, help='Accion a realizar')
    args = parser.parse_args()
    check_txt(args.action)