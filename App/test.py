from pygments import highlight
from pygments.lexers import get_lexer_by_name
from PIL import Image
from io import BytesIO
from pygments.formatters import HtmlFormatter, TerminalFormatter, BmpImageFormatter, ImageFormatter

def test_main():
    languageName = input("Enter language name: ")
    Code = input("Enter code: ")
    print("your code will be generated in 4-5 seconds")

def htmlformater():
    code = '''
    def hello():
        print("Hello, world!")
    '''
    lexer = get_lexer_by_name('python')
    formatter = HtmlFormatter(style='xcode')
    highlighted_code = highlight(code, lexer, formatter)
    css_styles = formatter.get_style_defs('.highlight')
    print(highlighted_code, css_styles)

def terminalformater():
    code = '''
    def hello():
        print("Hello, world!")
    '''
    lexer = get_lexer_by_name('python')
    formatter = TerminalFormatter(style='xcode')
    highlighted_code = highlight(code, lexer, formatter)
    # css_styles = formatter.get_style_defs('.highlight')
    print(highlighted_code)

def bmp_test():
    code = '''
    def hello():
        print("Hello, world!")
    '''

    lexer = get_lexer_by_name('python')
    formatter = BmpImageFormatter(style='xcode')
    highlighted_code = highlight(code, lexer, formatter)
    # css_styles = formatter.get_style_defs('.highlight')
    with open("test.bmp", "a") as f:
        f.write(str(highlighted_code))

    stream = BytesIO(highlighted_code)
    stream = Image.open(stream)
    stream.save("sd.bmp")
    stream.show("sd")
    print(stream)

def img_format():
    # Define your code and the lexer for it
    code = '''
    package main

    import (
        "fmt"
        "os"
        "path/filepath"
    )

    func check(e error) {
        if e != nil {
            panic(e)
        }
    }

    func main() {

        f, err := os.CreateTemp("", "sample")
        check(err)

        fmt.Println("Temp file name:", f.Name())

        defer os.Remove(f.Name())
    }
    '''
    lexer = get_lexer_by_name('go')

    # Create the image formatter
    formatter = ImageFormatter(font_name='Courier New', font_size=24, style="dracula", line_number_fg="#7e748a", line_number_bg="#3e304e")
    # formatter.style = 

    # Highlight the code and generate the image
    highlighted_code = highlight(code, lexer, formatter)

    # Convert the image data to a stream
    stream = BytesIO(highlighted_code)

    # Open the image from the stream
    image = Image.open(stream)

    # Save or display the image
    image.save('highlighted_code.png')
    image.show()

if __name__ == '__main__':
    # test_main()
    htmlformater()
    terminalformater()
    bmp_test()
    img_format()
