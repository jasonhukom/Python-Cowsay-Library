import cowsay, sys, os

char_name = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux', 'exit']

def main():
    ch = char_name[character()]
    
    if len(sys.argv) == 2 and ch != char_name[-1]:
        os.system("cowsay" + " -t " + sys.argv[1] + " -c "+ ch )

def character():
    print("Pick a character:")
    for i in range(len(char_name)):
        print(f"({i+1}) {char_name[i]}")
    try:
        n = (int(input(": "))) - 1
    except ValueError:
        sys.exit("Exiting...")
    return n
if __name__ == "__main__":
    main()