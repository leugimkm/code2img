import textwrap
from argparse import ArgumentParser, RawDescriptionHelpFormatter


def parse_args():
    """Function to parse arguments."""
    parser = ArgumentParser(
        prog="carbonpy",
        formatter_class=RawDescriptionHelpFormatter,
        description=textwrap.dedent("""\
            CarbonPy
            --------
                CarbonPy is a simple tool to generate an image from a local
                file or from a GitHub repository. It can also be used to
                send the source code to carbon.now.sh and generate the
                image there.
            """
        ),
        epilog="",
    )
    parser.add_argument(
        "file",
        help="File path of source code.",
    )
    parser.add_argument(
        "-s",
        "--save",
        action="store_true",
        help="Generate an image from a local file.",
    )
    parser.add_argument(
        "-c",
        "--carbon",
        action="store_true",
        help="Send source code to Carbon.now.sh.",
    )
    parser.add_argument(
        "-g",
        "--github",
        action="store_true",
        help="Generate an image from a GitHub repository.",
    )
    parser.add_argument(
        "-gc",
        "--gcarbon",
        action="store_true",
        help="Send GitHub content to Carbon.now.sh.",
    )
    return parser.parse_args()
