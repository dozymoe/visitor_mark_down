try:
    from bs4 import Comment, Tag
except ImportError:
    from BeautifulSoup import Comment, Tag


class Door2DoorSoup(object):
    """
    Provides interaction with BeautifulSoup nodes.
    """

    @staticmethod
    def is_text(node):
        """ Is this node a text node? """
        if isinstance(node, Comment):
            return False
        try:
            return isinstance(node, unicode)
        except NameError:
            return isinstance(node, str)


    @staticmethod
    def is_tag(node):
        """ Is this node an html tag node? """
        return isinstance(node, Tag)


    @staticmethod
    def has_attr(node, attrname):
        """ Does node have this html attribute? """
        return node.has_attr(attrname)


    @staticmethod
    def get_attr(node, attrname, default=''):
        """ Give me the attribute value! """
        try:
            return node[attrname]
        except KeyError:
            return default


    @staticmethod
    def get_tag_name(node):
        """ Give me the html tag's name! """
        return node.name


    @staticmethod
    def get_child(node):
        """ Give me iterator to the node's children! """
        return node.contents
