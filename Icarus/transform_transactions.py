import pandas

class Transform(object):

    def __init__(self, df):
        self.df = df

    def _build_schema(self):
        pass

    def round_difference(self, amount='Amount') -> float:
        """
        Determine difference between a value in Amount and the next nearest dollar. This assumes all transactions are
        negative in the df[amount] column

        for example {amount: 13.56} would result in:
        1. self.df['round_difference'] = .44
        2. assuming there was only one record in the dataframe it will return float

        :param amount:
        :return:
        """
        self.df['round_difference'] = self.df[amount].apply(lambda a: 1 - (-1 + ((int(str(a).split('.')[0]) + 1 )
                                                                                   - a)))
        return float(format(self.df['round_difference'].sum(), '.2f'))

    def add_self_fee(self, fee, amount='Amount', max=None, override=False) -> float:
        """

        :param fee:
        :return:
        """
        if fee > 1 and not override:
            raise ValueError('{0} is greater than 1. This would cause a fee of {0}%. If this is intended set '
                             'override to True: foo.add_self_fee(..., override = True)')

        self.df['self_fee'] = self.df[amount].apply(lambda a: -1 * (a * fee))

        return float(format(self.df['self_fee'].sum(), '.2f'))