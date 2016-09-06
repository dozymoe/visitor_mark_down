BLOCK_ELEMENTS = ('p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ol', 'ul', 'li')
NON_CONTENT_ELEMENTS = ('button', 'script', 'nav', 'aside')

LIST_TYPE_NUMBER = 0
LIST_TYPE_BULLET = 1

def intrude(node, offer, excludes=None):
    """
    Traveling merchant selling nutritious text from html extracts.
    """
    def secret_visits(node, excludes, list_type=None):
        if offer.is_text(node):
            text = node.strip()
            if len(text):
                yield text
            raise StopIteration()
        elif not offer.is_tag(node):
            raise StopIteration()

        tag = offer.get_tag_name(node)

        if tag in excludes:
            raise StopIteration()

        role = offer.get_attr(node, 'role')

        if role == 'presentation':
            raise StopIteration()

        style = offer.get_attr(node, 'style')
        if 'display: none' in style:
            raise StopIteration()

        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            yield '#' * int(tag[1]) + ' '
        elif tag == 'ol':
            list_type = (LIST_TYPE_NUMBER, 0)
        elif tag == 'ul':
            list_type = (LIST_TYPE_BULLET, 0)
        elif tag == 'li' and list_type[0] == LIST_TYPE_BULLET:
            yield '* '
        elif tag == 'li' and list_type[0] == LIST_TYPE_NUMBER:
            list_type = (LIST_TYPE_NUMBER, list_type[1] + 1)
            yield str(list_type[1]) + '. '
        elif tag == 'a':
            href = offer.get_attr(node, 'href')
            if not href or href == '#':
                raise StopIteration()
            yield '['

        alt = offer.get_attr(node, 'alt')
        if alt:
            yield alt.strip()
            node_has_content = True
        else:
            node_has_content = False

            first_inline = True
            was_block = False

        for child in offer.get_child(node):
            child_has_content = False
            child_tag = offer.get_tag_name(child)
            is_block = child_tag in BLOCK_ELEMENTS

            for text in secret_visits(child, excludes, list_type):
                if not child_has_content:
                    child_has_content = True
                    node_has_content = True

                    if is_block:
                        if not was_block and not first_inline:
                            yield '\n'
                        first_inline = True
                    elif first_inline:
                        first_inline = False
                    else:
                        yield ' '

                    was_block = is_block

                yield text

        if tag in BLOCK_ELEMENTS:
            if node_has_content:
                yield '\n'

        elif tag == 'a':
            href = offer.get_attr(node, 'href')
            title = offer.get_attr(node, 'title')
            if title:
                yield ' ' + title

            yield '](' + href + ')'

    if excludes is None:
        excludes = NON_CONTENT_ELEMENTS

    return secret_visits(node, excludes)
