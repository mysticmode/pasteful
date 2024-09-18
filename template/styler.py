import pygments
import pygments.lexers
from pygments.formatters import HtmlFormatter

code = """\
func main() {
    fmt.Println("Hello")
}
"""
lexer = pygments.lexers.get_lexer_for_filename("main.go")
formatter = HtmlFormatter(linenos=True, style="xcode", noclasses=True)
highlighted_text = pygments.highlight(code, lexer, formatter)

with open("out.html", "w") as f:
    f.write(highlighted_text)