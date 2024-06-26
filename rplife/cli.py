"""
I denne filen importerer den først argparse-modulen. Deretter importerer det noen nødvendige objekter fra rplife.
Her defineres alle lovlige argumenter man kan bruke når man starter programmet.
Man kan også starte programmet med --help og da sørger argparse at vi får en output med en infoliste om hva de forskjellige kommandoene gjør.
"""
import argparse 
from rplife import __version__, patterns, views

def get_command_line_args():
    parser = argparse.ArgumentParser(
        prog="rplife",
        description="Conway's Game of Life in your terminal",
    )
    
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s v{__version__}"
    )
    parser.add_argument(
        "-p",
        "--pattern",
        choices=[pat.name for pat in patterns.get_all_patterns()],
        default="Blinker",
        help="take a pattern for the Game of Life (default: %(default)s)",     
    )
    parser.add_argument(
        "-s",
        "--symbol",
        default="♥",
        help="symbolet som representerer en levende celle"
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="show all available patterns in a sequence",
        )
    parser.add_argument(
        "-r",
        "--random",
        action="store_true",
        help="makes the pattern total random and not using a predefined pattern",
    )
    parser.add_argument(
        "-v",
        "--view",
        choices=views.__all__,
        default="CursesView",
        help="display the life grid in a specific view (default: %(default)s)",
    )
    parser.add_argument(
        "-g",
        "--gen",
        metavar="NUM_GENERATIONS",
        type=int,
        default=10,
        help="number of generations (default: %(default)s)",
    )
    parser.add_argument(
        "-f",
        "--fps",
        metavar="FRAMES_PER_SECOND",
        type=int,
        default=7,
        help="frames per second (default: %(default)s)",
    )
    return parser.parse_args()

