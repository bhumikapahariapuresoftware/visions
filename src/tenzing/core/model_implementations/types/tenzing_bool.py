import pandas.api.types as pdt

from tenzing.core.model_implementations import tenzing_generic
from tenzing.core.mixins import optionMixin


class tenzing_bool(optionMixin, tenzing_generic):
    """**Boolean** implementation of :class:`tenzing.core.models.tenzing_model`.

    >>> x = pd.Series([True, False, np.nan])
    >>> x in tenzing_bool
    True
    """

    @classmethod
    def contains_op(cls, series):
        if pdt.is_categorical_dtype(series):
            return False

        return pdt.is_bool_dtype(series)

    @classmethod
    def cast_op(cls, series, operation=None):
        return series.astype(bool)

    @classmethod
    def summarization_op(cls, series):
        """Note that frequencies for True/False are in the base summary"""
        summary = super().summarization_op(series)
        return summary
