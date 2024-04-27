import sys

from rplife import patterns, views #her importerer jeg de to filene "patterns og views"
from rplife.cli import get_command_line_args

def main():
    args = get_command_line_args() # henter inn argumenter som skal styre grunnleggende funksjoner
    View = getattr(views, args.view)
    if args.random: # Hvis man spsifiserer -r peramenter ignorerer vi -a og -p
        pattern = patterns.Pattern.from_random()
        _show_pattern(View, pattern, args)
    elif args.all: # hvis man kjører koden med -a eller --all kjøres alle mønsterne etter hverandre
        for pattern in patterns.get_all_patterns(): 
            _show_pattern(View, pattern, args)
    else: # Hvis ikke kjører den bare det ene deafult pattern som er blinker
        _show_pattern(
            View,
            patterns.get_pattern(name=args.pattern),
            args
        )


def _show_pattern(View, pattern, args):
    try:
        View(pattern=pattern, alivesymbol=args.symbol, gen=args.gen, frame_rate=args.fps).show() # her tar vi resten av verdiene fra args for å styre patterns, symboler hvor mange generasjoner og frame raten som er hastigheten den kjøres
    except Exception as error:
        print(error, file=sys.stderr)
        
if __name__ == "__main__": # Når man opner programmet (siden main py er hoved filen) så kjøres koden over
    main()
