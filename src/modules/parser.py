class Parser:
    """
    Parser for json files
    """
    _formatter = None

    def __init__(self, formatter: object):
        """

        :type formatter: object
        """
        self._formatter = formatter

    @property
    def formatter(self):
        return self._formatter

    def parse(self, data: dict) -> dict:
        return self.formatter.process(data=data)
