from lxml import etree
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="filename")

(options, args) = parser.parse_args()
if options.filename:
    filename = options.filename
else:
    filename = 'input.html'

file = open(filename, 'r')
html = file.read()

etree_object = etree.fromstring(html)
result = {}
for node in etree_object.iter(): #loop through all tags
    if not(result.has_key(node.tag)): #make sure that we don't repeat same tags many times
        result[node.tag] = []
    for child in node.iterchildren(): #loop through all child tags
        if not(child.tag in result[node.tag]): #make sure that we don't repeat same child tags many times
            result[node.tag].append(child.tag)

for tag in result: #just prints our result
    current_line = tag + ' ->'
    for child_tag in result[tag]:
        current_line += ' ' + child_tag
    print current_line