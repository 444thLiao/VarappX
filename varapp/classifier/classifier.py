import abc

class Classifier:
    __metaclass__ = abc.ABCMeta
    method_class = ''  # the category of classifier

    def __init__(self, name='', filters='', db=None, ss=None):
        """

        :param name:
        """
        self.db = db
        self.ss = ss
        self.filters = filters
        self.name = name

    def shor_str(self):
        return "{}{} in {}".format(self.name, self.db)

    def __str__(self):

        return "<Classifier {}, using filters {} ".format(self.name,self.filters)

    def predict(self):
        """
        A classifier fundmental function it need.
        :return: A series equal to len(data)
        """

