import base64
from dataclasses import dataclass, field
from pathlib import Path

from rich.traceback import install
from rich import print
import typer

from font_embedder.template import CSS_TEMPLATE

install()

app = typer.Typer(
    context_settings={
        "help_option_names": ["--help", "-h"],
    },
)


@dataclass
class Embedder:
    font_name: str = field(default=None)
    font_files: dict[str:str] = field(default=None)
    encoded_files: dict[str:str] = field(default=None)

    def __post_init__(self) -> None:
        self.font_files = dict()
        self.encoded_files = dict()

    def prompt(self) -> None:
        """
        TODO - Figure out how to add path completion
        TODO - Input validaton/ Filetype validation
        """
        self.font_name = typer.prompt("Font Family Name")

        print(f"\nPlease enter file names with extensions for font weights:")
        self.font_files["regular"] = typer.prompt("Regular")
        self.font_files["italic"] = typer.prompt("Italic")
        self.font_files["bold"] = typer.prompt("Bold")
        self.font_files["bold_italic"] = typer.prompt("Bold-Italic")

    def encode_files(self) -> None:
        cwd = Path.cwd()

        for k, v in self.font_files.items():
            file_path = cwd / v
            self.encoded_files[k] = self._encode(str(file_path))

    def _encode(self, file_path: str) -> str:
        with open(file_path, "rb") as file:
            encoded = base64.b64encode(file.read()).decode("utf-8")

        return encoded

    def generate_CSS(self) -> None:
        """
        TODO - Add field in CSS_TEMPLATE for file type
               Currently it is only '.ttf' but has worked
               fine with '.otf' but may cause issues with
               '.woff' or other font file types
        """
        args = dict()

        args["name"] = self.font_name

        for k, v in self.encoded_files.items():
            args[k] = v

        with open(f'{args["name"].replace(" ", "")}.css', "w") as file:
            file.write(CSS_TEMPLATE.format(**args))

        print(f'\n{args["name"].replace(" ", "")}.css created!')

    def run(self) -> None:
        self.prompt()
        self.encode_files()
        self.generate_CSS()


@app.command("create")
def create() -> None:
    """
    Create new css file with embedded fonts
    """
    print(Path.cwd())
    embedder = Embedder()
    embedder.run()


@app.callback()
def callback() -> None:
    """
    Create CSS file with embedded font files
    """
    ...


if __name__ == "__main__":
    app()
