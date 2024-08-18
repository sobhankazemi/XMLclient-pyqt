class mapper():
    def __init__(self):
        self.functions={
            "text" : "setText(",
            "icon" : "setIcon(QIcon(",
            "iconsize" : "setIconSize(QSize(",
            "down" : "setDown(",
            "checked" : "setChecked(",
            "ontoggle" : "toggled.connect(self.",
            "style" : "setStyleSheet(\"QRadioButton\"\n\"{\"\n"
        }
        self.doubleQoutes=["icon","iconsize"]
        self.special =["iconsize","down","checked","ontoggle"]
        self.actions=["ontoggle"]