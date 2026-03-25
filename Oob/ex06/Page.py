from elem import *
from elements import *


VALID_TAGS = ['html', 'head', 'body', 'title', 'meta', 'img',
              'table', 'th', 'tr', 'td', 'ul', 'ol', 'li',
              'h1', 'h2', 'p', 'div', 'span', 'br', 'hr']


BODY_OR_DIV_CONTENT = (H1, H2, Div, Table, Ul, Ol, Span, Text)

TEXT_IN_CONTENT = ['title', 'h1', 'h2', 'li', 'th', 'td']

class Page:
    def __init__(self, class_elem):
        self.class_elem = class_elem


    def is_valid(self, class_elem=None):
        if class_elem is None:
            class_elem = self.class_elem

        if not self.tree_path(class_elem):
            print("Invalid tree path")
            return False
        if not isinstance(class_elem, Text):
            if not self.html_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
            if not self.head_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
            if not self.body_or_div_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
            if not self.text_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
            if not self.list_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
            if not self.table_rules(class_elem):
                print(f"Invalid {class_elem.tag} rules")
                return False
        
            for elem in class_elem.content:
                if not self.is_valid(elem):
                    return False

        return True


    def tree_path(self, class_elem):
        if isinstance(class_elem, Text):
            return True
        
        if class_elem.tag not in VALID_TAGS:
            return False
        
        for elem in class_elem.content:
            if isinstance(elem, Text):
                continue
            if elem.tag not in VALID_TAGS:
                return False
        
        return True


    def html_rules(self, class_elem):
        if class_elem.tag == 'html':
            if len(class_elem.content) == 2 and isinstance(class_elem.content[0], Head) and isinstance(class_elem.content[1], Body):
                return True
            else:
                return False
        return True


    def head_rules(self, class_elem):
        if class_elem.tag == 'head':
            if len(class_elem.content) != 1:
                return False
            if not isinstance(class_elem.content[0], Title):
                return False
        return True


    def body_or_div_rules(self, class_elem):
        if class_elem.tag == 'body' or class_elem.tag == 'div':
            if not all(isinstance(elem, BODY_OR_DIV_CONTENT) for elem in class_elem.content):
                return False
        return True


    def text_rules(self, class_elem):
        if class_elem.tag in TEXT_IN_CONTENT:
            if len(class_elem.content) != 1 or not isinstance(class_elem.content[0], Text):
                return False

        if class_elem.tag == 'p':
            if len(class_elem.content) == 0 or len(set(class_elem.content)) != 1:
                return False
            if not all(isinstance(elem, Text) for elem in class_elem.content):
                return False
        
        if class_elem.tag == 'span':
            if len(class_elem.content) == 0 or len(set(class_elem.content)) != 1:
               return False
            if not all(isinstance(elem, (Text, P)) for elem in class_elem.content):
                return False
        return True


    def list_rules(self, class_elem):
        if class_elem.tag == 'ul' or class_elem.tag == 'ol':
            if len(class_elem.content) == 0 or len(set(class_elem.content)) != 1:
                return False
            if not all(isinstance(elem, Li) for elem in class_elem.content):
                return False
        return True


    def table_rules(self, class_elem):
        if class_elem.tag == 'table':
            if len(class_elem.content) == 0 or len(set(class_elem.content)) != 1:
                return False
            if not all(isinstance(elem, Tr) for elem in class_elem.content):
                return False

        if class_elem.tag == 'tr':
            if not all(isinstance(elem, (Td, Th)) for elem in class_elem.content):
                return False
            elif len(set(class_elem.content)) != 1:
                return False
        return True


    def __str__(self):
        return str(self.class_elem)
    

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(str(self.class_elem))


if __name__ == '__main__':
    page_1 = Page(Head(H1()))
    page_2 = Page(Html(Body()))
    page_3 = Page(Body(Head(Title(Text('"Hello ground!"')))))
    page_4 = Page(H1())
    page_5 = Page(Span(H1()))
    page_6 = Page(Ul(Body()))
    page_7 = Page(Table(Th()))
    page_8 = Page(Tr([Th(), Td()]))
    page_1.is_valid()
    page_2.is_valid()
    page_3.is_valid()
    page_4.is_valid()
    page_5.is_valid()
    page_6.is_valid()
    page_7.is_valid()
    page_8.is_valid()