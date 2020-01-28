from googletrans import Translator
import googletrans
from textblob import TextBlob
translator = Translator()
f=open("test.txt","r",encoding='utf8')
co=f.read()
f.close()
co=co.split("\n")
f1=open("out.txt","w+",encoding='utf8')
for do in co:
    ui=do.split("=")
    s=ui[1]
    b = TextBlob(s)
    translated = translator.translate(s, src=b.detect_language(), dest='te')
    translated1 = translator.translate(s, src=b.detect_language(), dest='hi')
    p=ui[0]+"="+translated1.text+"\n"
    f1.write(p)
    p=ui[0]+"="+translated.text+"\n"
    f1.write(p)
f1.close()
    #print(translated1.text,translated.text)
