from pathlib import Path

from JavaImageTools import JavaImageToolsInitializer

__all__ = ("ji",)

JIMHns = "dev.brachtendorf.jimagehash."
JIMHnsH = JIMHns + "hash."
JIMHnsHA = JIMHns + "hashAlgorithms."
JIMHnsHAExp = JIMHnsHA + "experimental."
JIMHnsHAFilter = JIMHnsHA + "filter."

classList = (
	[JIMHnsH + el for el in ("FuzzyHash", "Hash", "HashUtil")] +
	[JIMHnsHA + el for el in ("AverageColorHash", "AverageHash", "AverageKernelHash", "DifferenceHash", "MedianHash", "PerceptiveHash", "RotAverageHash", "RotPHash", "WaveletHash")] +
	[JIMHnsHAExp + el for el in ("HogHash", "HogHashAngularEncoded", "HogHashDual")] +
	[JIMHnsHAFilter + el for el in ("Kernel", "MaximumKernel", "MedianKernel", "MinimumKernel", "NonAveragingKernel", "MultiKernel")]
)

# Currently hardcoded, proper solution requires a separate package discovering jars available in system, such as distro-provided maven repo
ji = JavaImageToolsInitializer(
	(
		Path("./JImageHash-1.0.0.jar"),
		Path("./UtilityCode-2.0.1.jar"),
		Path("./JLargeArrays-1.7-SNAPSHOT.jar"),  # for JTransforms
		Path("./JTransforms-3.2-SNAPSHOT.jar"),  # for PerceptiveHash
		Path("/usr/share/maven-repo/org/apache/commons/commons-math3/debian/commons-math3-debian.jar")  # libcommons-math3-java
	) + tuple(Path("/usr/share/openjfx/lib/").glob("*.jar")
), classList)
