from django.utils.safestring import mark_safe
from markdown import Extension, markdown


class EscapeHtml(Extension):
    def extendMarkdown(self, md, md_globals):
        del md.preprocessors['html_block']
        del md.inlinePatterns['html']


def markdownify(s):
    """ converts markdown to html """
    return mark_safe(markdown(s,
                              extensions=[
                                  EscapeHtml(),
                                  'markdown.extensions.nl2br',
                                  'markdown.extensions.fenced_code'
                              ]))
