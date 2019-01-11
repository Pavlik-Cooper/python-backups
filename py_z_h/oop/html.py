class Tag(object):
    self_closing = ["area","base","br","col","command","embed","hr",
                    "img","input","link","meta","param","source","track","wbr"]

    def __init__(self, name, contents=''):
        tag = name.split()[0]
        if tag not in Tag.self_closing:
            self.end_tag = '</{}>'.format(tag)
        else:
            self.end_tag = ''
        self.start_tag = '<{}>'.format(name)
        self.contents = contents
        self._children = []

    def __str__(self):
        return "{0.start_tag}{0.contents}{0.end_tag}".format(self)

    def add_tag(self, name, contents='', tags=[]):
        new_tag = Tag(name, contents)
        self._children.append(new_tag)
        if len(tags) > 0:
            for tag in tags:
                new_tag.add_tag(tag[0], tag[1]).display()
        return self

    def display(self, file=None):
        for tag in self._children:
            self.contents += str(tag) + "\n"
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE html', '')

class Head(Tag):
    def __init__(self):
        super().__init__('head', '')

class Body(Tag):
    def __init__(self):
        super().__init__('body', '')   # body contents will be built up separately


class HtmlDoc(object):

    def __init__(self, head, body):
        self._doc_type = DocType()
        self._head = head
        self._body = body

    def add_tag(self, name, contents):
        return self._body.add_tag(name, contents)

    def display(self, file=None):
        self._doc_type.display(file=file)
        print('<html>', file=file)
        self._head.display(file=file)
        self._body.display(file=file)
        print('</html>', file=file)


new_header = Head()
new_header.add_tag("title", "Awesome title")
new_header.add_tag("meta charset='utf-8'", "")
new_header.add_tag('link rel="alternate" href="https://ttorial.com/"', "")

new_body = Body()
new_body.add_tag('h1', 'Aggregation')
new_body.add_tag('p', "Unlike <strong>composition</strong>, aggregation uses existing instances"
                      " of objects to build up another object.")
new_body.add_tag('p', "The composed object doesn't actually own the objects that it's composed of"
                      " - if it's destroyed, those objects continue to exist.")

new_body.add_tag("div id='first'",'')\
    .add_tag("p","my p tag",[[
        'span',
        ''
     ]])


my_page = HtmlDoc(new_header, new_body)

with open('test.html', 'w') as test_doc:
    my_page.display(file=test_doc)








