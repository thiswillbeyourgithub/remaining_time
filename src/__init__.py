from . import RemainingTime
from .utils import openChangelog
from .utils import uuid  # duplicate UUID checked here

from .utils.JSCallable import JSCallable

from .utils import ankiLocalStorage

from aqt import mw


@JSCallable
def getCurrentRemainingCardCount():
    counts = list(mw.col.sched.counts(mw.reviewer.card))
    nu, lrn, rev = counts[:3]
    return [nu, lrn, rev]
