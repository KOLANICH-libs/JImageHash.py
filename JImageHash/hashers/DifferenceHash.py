from enum import Enum

from ..ji import ji
from ..JImageHash import JImageHash


class DifferenceHash(JImageHash):
	__slots__ = ()

	class Precision(Enum):
		simple = Simple = ji.DifferenceHash.Precision.Simple
		double = Double = ji.DifferenceHash.Precision.Double
		triple = Triple = ji.DifferenceHash.Precision.Triple

	def __init__(self, bitsInHash: int = 64, precision: Precision = Precision.triple):
		super().__init__(ji.DifferenceHash(bitsInHash, precision.value))
