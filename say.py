import cowsay, sys

char_name = ['beavis', 'cheese', 'cow', 'daemon', 'dragon', 'fox', 'ghostbusters', 'kitty',
'meow', 'miki', 'milk', 'octopus', 'pig', 'stegosaurus', 'stimpy', 'trex', 
'turkey', 'turtle', 'tux']

def main():
    if len(sys.argv) < 2: 
        sys.exit("Too few arguments")
    
    ch = sys.argv[2]

    function = getattr(cowsay, ch, None)
    if len(sys.argv) >= 2 and ch != char_name[-1]:
        function(sys.argv[1])

if __name__ == "__main__":
    main()