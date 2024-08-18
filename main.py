from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from ASTListener import AST
from mapper import mapper
import os

input_stream = FileStream(r""+"input.xml")

output_address = "genereatedcode.py"
if os.path.exists(output_address):
    os.remove(output_address)

output_stream = open(r""+output_address, "a")

lexer = XMLLexer(input_stream)

#refactoring all radiobuttontags
token = lexer.nextToken()
refactored = []
while token.type != Token.EOF:
    if token.text == "radiobutton":
        text = "<radiobutton "
        token = lexer.nextToken()
        while token.type != lexer.SLASH_CLOSE:
            text += token.text
            token = lexer.nextToken()
        text += token.text
        refactored.append(text)
    token = lexer.nextToken()


# create ast
asts = []
for text in refactored:
    input_stream = InputStream(text)
    lexer = XMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = XMLParser(token_stream)
    parse_tree = parser.document()
    walker = ParseTreeWalker()
    listener = AST()
    walker.walk(t=parse_tree, listener=listener)
    asts.append(listener)

for ast in asts:
    ast.PrintAST()
    print("\n\n")


# generating layout for the code that will be generated
layout = "from PyQt5.QtWidgets import *\nfrom PyQt5.QtCore import QSize\nfrom PyQt5.QtGui import QIcon\nimport sys\n\nclass Window(QWidget):\n\tdef __init__(self):\n\t\tQWidget.__init__(self)\n\t\tlayout = QGridLayout()\n\t\tself.setLayout(layout)\n"
output_stream.write(layout)
output_stream.write("\n# generating radiobuttons\n\n")
mp = mapper()
methods = mp.functions
actions = {}
counter = 1
for ast in asts:
    nm = ast.root+str(counter)
    temp = "\t\t#"+nm+"\n"
    output_stream.write(temp)
    # create an instance of a radiobutton
    temp = "\t\t"+nm+" ="+"QRadioButton()\n"
    output_stream.write(temp)
    for tree in ast.astTree:
        # generate functions of radiobutton
        method = tree.Method
        if method in methods:
            if method in mp.special:
                tree.Value = tree.Value[1:-1]
            if method in mp.actions:
                actions[counter]=tree.Value
            temp = "\t\t"+nm+"."+methods[method]+tree.Value
            if method in mp.doubleQoutes:
                temp += "))\n"
            elif method!="style":
                temp += ")\n"
            else:
                temp+="\n\"}\"\n)\n"
            output_stream.write(temp)
    temp = "\t\tlayout.addWidget("+nm+",0,"+str(counter)+")\n\n"
    output_stream.write(temp)
    counter += 1

for  i in actions:
    temp="\tdef "+actions[i]+"(self):\n"
    temp+="\t\t"+"radioButton = self.sender()\n"
    temp+="\t\t# to be completed\n"
    output_stream.write(temp)
output_stream.write("\n# end of generating\n")
footer = "app = QApplication(sys.argv)\nscreen = Window()\nscreen.show()\nsys.exit(app.exec_())"
output_stream.write(footer)
