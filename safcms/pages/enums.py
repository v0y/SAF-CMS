class PageContentTypes:
    MARKDOWN = 1
    HTML = 2
    MARKDOWN_URL = 3


CONTENT_TYPE_CHOICES = (
    (PageContentTypes.MARKDOWN, 'markdown'),
    (PageContentTypes.HTML, 'html'),
    (PageContentTypes.MARKDOWN_URL, 'markdown from url'),
)
