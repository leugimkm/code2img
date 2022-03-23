#!/user/bin/env python
# -*- coding: utf-8 -*-

"""CodeSeeker

Code2img is a simple tool to generate an image from source
code using Carbon.now.sh. Also, it can be used to generate
an image from a GitHub repository or from a local file.

Usage example:
    > python -m code2img soluciones/fibonacci.py -g
    Created image in current directory: fibonacci.png

    > python -m carbony fibonacci.py -c
    Opening in a web browser...

For more information:
https://leugimkm.github.io/code2img/
"""
import webbrowser
from .base import parse_args
from .api import Carbon
from .utils import parse_str, read_file, split_path, job_done
from .constants import URL
from .creator import ImgCreator, GitHubContent


def main():
    args = parse_args()
    query = Carbon().build_query()
    img = ImgCreator()

    filename = split_path(args.file)

    if args.github:
        content = GitHubContent(args.file)
        img.create(content.get_content(), filename)
        job_done(filename)
    if args.gcarbon:
        content = GitHubContent(args.file)
        code = parse_str(content.get_content())
        webbrowser.open_new_tab(URL.format(query=query, code=code))
        print("Sent to Carbon.now.sh")
        print()
    if args.carbon:
        code = parse_str(read_file(args.file))
        webbrowser.open_new_tab(URL.format(query=query, code=code))
        print("Sent to Carbon.now.sh")
        print()
    if args.save:
        code = read_file(args.file)
        img.create(code, filename)
        job_done(filename)


if __name__ == "__main__":
    main()
