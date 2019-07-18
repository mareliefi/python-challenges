import markdown
from jinja2 import Template

def markdown_convert_to_html():
  input_file = open("new_file.txt", "r")
  text = input_file.read()
  html = markdown.markdown(text)
  input_file.close() 
  output_file = open("new_file.html", "w")
  output_file.write(html)
  output_file.close()
  print "Converted markdown to html and stored in output_file.html"
  return html

markdown_convert_to_html()



