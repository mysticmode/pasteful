import argparse
import pygments
import pygments.lexers
from pygments.formatters import HtmlFormatter


# Instantiate the parser
parser = argparse.ArgumentParser(description='Styler syntax highlights the string and convert the output to html formatted file')
parser.add_argument('value', type=str,
                    help='A required value to style the given code')
parser.add_argument('output', type=str,
                    help='An output path value including filename to save the output of Styler')
args = parser.parse_args()

code = args.value
lexer = pygments.lexers.get_lexer_for_filename("main.go")
formatter = HtmlFormatter(linenos=True, style="xcode", noclasses=True)
highlighted_text = pygments.highlight(code, lexer, formatter)

with open(args.output, "w") as f:
    f.write(highlighted_text)