import requests
from pygments import highlight, lexers
from pygments.formatters.img import ImageFormatter


class GitHubContent:

    def __init__(
        self,
        url: str,
        repo: str = "AyudaEnPython/Soluciones",
    ) -> None:
        self.repo = repo
        self.url = f"https://raw.githubusercontent.com/{repo}/main/{url}"

    def get_content(self) -> str:
        response = requests.get(self.url)
        return response.text


class ImgCreator:

    def __init__(
        self,
        style: str = "dracula",
        language: str = "python",
    ) -> None:
        self.style = style
        self.language = language
        self.lexer = lexers.get_lexer_by_name(self.language)

    def create(self, raw: str, filename: str) -> None:
        formatter = ImageFormatter(
            style=self.style,
            line_number_chars=3,
            line_number_bg=None,
            line_number_fg=None,
            line_number_separator=False,
        )
        with open(f"{filename}.png", "wb") as f:
            f.write(highlight(raw, self.lexer, formatter))
