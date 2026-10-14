import re

print("Please insert the text you want to convert, followed by the input format and output format. " \
"\n Choose between the following formats: markdown, html, latex. Each input should be on a new line.")

text_input = input();

print("You entered the following text:\n" + text_input + "\n Please now specify the input format \n Remember there are only three formats to choose from: markdown, html, latex. Each input should be on a new line.")

format_input = input().strip().lower();  # "markdown", "html" or "latex"

print("You entered the following input format:\n" + format_input + "\n Please now specify the output format \n Remember there are only three formats to choose from: markdown, html, latex. Each input should be on a new line.")

format_output = input().strip().lower();    # "markdown", "html" or "latex"

print("You entered the following output format: " + format_output)

### Format conversion logic
# (.+) / (.*?) captures the text in the middle, and \1 puts it back between the new tags.
# Headers (## before #) and bold (** before *) are always handled before the shorter pattern.

textreplaced = None;

if format_input == format_output:

    print("\n The input and output formats are the same. No conversion needed.")

    textreplaced = text_input

elif format_input == "markdown" and format_output == "html":

    print("Converting from markdown to html...");

    textreplaced = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text_input, flags=re.M)
    textreplaced = re.sub(r'^# (.+)$', r'<h1>\1</h1>', textreplaced, flags=re.M)
    textreplaced = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', textreplaced)
    textreplaced = re.sub(r'\*(.+?)\*', r'<em>\1</em>', textreplaced)


elif format_input == "html" and format_output == "markdown":

    print("Converting from html to markdown...")

    textreplaced = re.sub(r'<h1>(.*?)</h1>', r'# \1', text_input)
    textreplaced = re.sub(r'<h2>(.*?)</h2>', r'## \1', textreplaced)
    textreplaced = re.sub(r'<strong>(.*?)</strong>', r'**\1**', textreplaced)
    textreplaced = re.sub(r'<em>(.*?)</em>', r'*\1*', textreplaced)


elif format_input == "markdown" and format_output == "latex":

    print("Converting from markdown to latex...")

    textreplaced = re.sub(r'^## (.+)$', r'\\subsection{\1}', text_input, flags=re.M)
    textreplaced = re.sub(r'^# (.+)$', r'\\section{\1}', textreplaced, flags=re.M)
    textreplaced = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', textreplaced)
    textreplaced = re.sub(r'\*(.+?)\*', r'\\textit{\1}', textreplaced)


elif format_input == "latex" and format_output == "markdown":

    print("Converting from latex to markdown...")

    textreplaced = re.sub(r'\\section\{(.*?)\}', r'# \1', text_input)
    textreplaced = re.sub(r'\\subsection\{(.*?)\}', r'## \1', textreplaced)
    textreplaced = re.sub(r'\\textbf\{(.*?)\}', r'**\1**', textreplaced)
    textreplaced = re.sub(r'\\textit\{(.*?)\}', r'*\1*', textreplaced)


elif format_input == "html" and format_output == "latex":

    print("Converting from html to latex...")

    textreplaced = re.sub(r'<h1>(.*?)</h1>', r'\\section{\1}', text_input)
    textreplaced = re.sub(r'<h2>(.*?)</h2>', r'\\subsection{\1}', textreplaced)
    textreplaced = re.sub(r'<strong>(.*?)</strong>', r'\\textbf{\1}', textreplaced)
    textreplaced = re.sub(r'<em>(.*?)</em>', r'\\textit{\1}', textreplaced)


elif format_input == "latex" and format_output == "html":

    print("Converting from latex to html...")

    textreplaced = re.sub(r'\\section\{(.*?)\}', r'<h1>\1</h1>', text_input)
    textreplaced = re.sub(r'\\subsection\{(.*?)\}', r'<h2>\1</h2>', textreplaced)
    textreplaced = re.sub(r'\\textbf\{(.*?)\}', r'<strong>\1</strong>', textreplaced)
    textreplaced = re.sub(r'\\textit\{(.*?)\}', r'<em>\1</em>', textreplaced)

else:
    print("\n Invalid format, please re-run the program and try again. \n");



if textreplaced is not None:
    print("Conversion complete! Here is the converted text:\n" + textreplaced);

print("\n Thank you for using the Language Converter. Goodbye!");
