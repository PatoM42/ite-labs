import re

print("Please insert the text you want to convert, followed by the input format and output format. " \
"\n Choose between the following formats: markdown, html, latex. Each input should be on a new line.")

text_input = input();

print("You entered the following text:\n" + text_input + "\n Please now specify the input format \n Remember there are only three formats to choose from: markdown, html, latex. Each input should be on a new line.")

format_input = input();  # "markdown", "html" or "latex"

print("You entered the following input format:\n" + format_input + "Please now specify the output format \n Remember there are only three formats to choose from: markdown, html, latex. Each input should be on a new line.")

format_output = input();    # "markdown", "html" or "latex"

print("You entered the following output format:" + format_output)

### Format conversion logic

textreplaced = "No text converted";

if format_input == format_output:

    print("\n The input and output formats are the same. No conversion needed.")

elif format_input == "markdown" and format_output == "html":

        print("Converting from markdown to html...");

        textreplaced = text_input.replace("#", "<h1>").replace("##", "<h2>").replace("**", "<strong>").replace("*", "<em>")


elif format_input == "html" and format_output == "markdown":

        print("Converting from html to markdown...")

        textreplaced = text_input.replace("<h1>", "#").replace("<h2>", "##").replace("<strong>", "**").replace("<em>", "*")


elif format_input == "markdown" and format_output == "latex":

    print("Converting from markdown to latex...")

    textreplaced = text_input.replace("#", "\\section{").replace("##", "\\subsection{").replace("**", "\\textbf{").replace("*", "\\textit{")


elif format_input == "latex" and format_output == "markdown":

    print("Converting from latex to markdown...")

    textreplaced = text_input.replace("\\section{", "#").replace("\\subsection{", "##").replace("\\textbf{", "**").replace("\\textit{", "*")


elif format_input == "html" and format_output == "latex":

    print("Converting from html to latex...")

    textreplaced = text_input.replace("<h1>", "\\section{").replace("<h2>", "\\subsection{").replace("<strong>", "\\textbf{").replace("<em>", "\\textit{")


elif format_input == "latex" and format_output == "html":

    print("Converting from latex to html...")

    textreplaced = text_input.replace("\\section{", "<h1>").replace("\\subsection{", "<h2>").replace("\\textbf{", "<strong>").replace("\\textit{", "<em>")

else:
     print("\n Invalid format, please re-run the program and try again. \n");



print("Conversion complete! Here is the converted text:\n" + textreplaced);

print("\n Thank you for using the Language Converter. Goodbye!");
