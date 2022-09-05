class colors:
    default = 0
    teal = 0x1abc9c
    dark_teal = 0x11806a
    green = 0x2ecc71
    dark_green = 0x1f8b4c
    blue = 0x3498db
    dark_blue = 0x206694
    purple = 0x9b59b6
    dark_purple = 0x71368a
    magenta = 0xe91e63
    dark_magenta = 0xad1457
    gold = 0xf1c40f
    dark_gold = 0xc27c0e
    orange = 0xe67e22
    dark_orange = 0xa84300
    red = 0xe74c3c
    dark_red = 0x992d22
    lighter_grey = 0x95a5a6
    dark_grey = 0x607d8b
    light_grey = 0x979c9f
    darker_grey = 0x546e7a
    blurple = 0x7289da
    greyple = 0x99aab5
class icon():
    icon_url= 'https://cdn-lost.reload-dev.ml/public/Lost.png'
    guide_icon_url='https://cdn-lost.reload-dev.ml/public/guide.gif'
class utils():
    @classmethod
    def processesBar(self,level:int,style=['[','#','-',']'],multiple=2):
        """
        style format example
        if style input is like this

            level=50
            multiple=1
            style=['[','#','-',']']

        output: [######-----]
        
        """
        if level>100 or level<0 or multiple<=0:
            raise ValueError('level limt is 0~100,multiple must above 1.')
        else:
            level//=10

            string=''
            string+=style[0]
            for i in range(level*multiple):
                string+=style[1]
            for i in range((10-level)*multiple):
                string+=style[2]
            string+=style[3]

            return string
    @classmethod
    def showinfo(self,tip, info):
        print("{}:{}".format(tip,info))


