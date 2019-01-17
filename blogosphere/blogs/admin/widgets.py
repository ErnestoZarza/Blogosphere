from django.contrib.admin import widgets


class MiniTextArea(widgets.AdminTextareaWidget):
    """
    Vertically shorter version of the admin textarea widget.
    """
    rows = 3

    def __init__(self, attrs=None):
        super(MiniTextArea, self).__init__(
            {'rows': self.rows})
