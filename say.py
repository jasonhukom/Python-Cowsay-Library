import cowsay, sys, os

char_name = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']

def main():
    ch = sys.argv[2]
    print(sys.argv[1])
    if len(sys.argv) >= 2 and ch != char_name[-1]:
        os.system("cowsay" + ' -t "' + sys.argv[1] + '" -c ' + ch )

if __name__ == "__main__":
    main()