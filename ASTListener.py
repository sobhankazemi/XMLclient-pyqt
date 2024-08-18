from gen.XMLParserListener import XMLParserListener
from gen.XMLParser import XMLParser


class attributes():
    def __init__(self):
        self.Method = ""
        self.Value = ""


class AST(XMLParserListener):
    def __init__(self):
        self.astTree = []
        self.root = ""

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.root = str(ctx.Name()[0])

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        temp = attributes()
        temp.Method = str(ctx.Name())
        temp.Value = str(ctx.STRING())
        self.astTree.append(temp)

    def PrintAST(self):
        print(self.root)
        print("|")
        print("|")
        for i in range(len(self.astTree)):
            print("|______________________",
            self.astTree[i].Method, "--->", self.astTree[i].Value)
            if i != len(self.astTree)-1:
                print("|")
                print("|")
