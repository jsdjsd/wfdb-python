"""
The processing subpackage contains signal-processing tools.
"""
from .basic import (resample_ann, resample_sig, resample_singlechan,
                    resample_multichan, get_filter_gain)
from .evaluate import Comparitor, compare_annotations
from .gqrs import gqrs_detect
from .hr import compute_hr
from .peaks import find_peaks, correct_peaks
from .qrs import XQRS, xqrs_detect
