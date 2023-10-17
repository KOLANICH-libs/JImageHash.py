JImageHash.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
=============
~~[wheel (GHA via `nightly.link`)](https://nightly.link/KOLANICH-libs/JImageHash.py/workflows/CI/master/JImageHash-0.CI-py3-none-any.whl)~~
~~[![GitHub Actions](https://github.com/KOLANICH-libs/JImageHash.py/workflows/CI/badge.svg)](https://github.com/KOLANICH-libs/JImageHash.py/actions/)~~
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH-libs/JImageHash.py.svg)](https://libraries.io/github/KOLANICH-libs/JImageHash.py)
[![Code style: antiflash](https://img.shields.io/badge/code%20style-antiflash-FFF.svg)](https://codeberg.org/KOLANICH-tools/antiflash.py)

**We have moved to https://codeberg.org/KOLANICH-libs/JImageHash.py (the namespace has changed to `KFmts`, which groups packages related to parsing or serialization), grab new versions there.**

Under the disguise of "better security" Micro$oft-owned GitHub has [discriminated users of 1FA passwords](https://github.blog/2023-03-09-raising-the-bar-for-software-security-github-2fa-begins-march-13/) while having commercial interest in success and wide adoption of [FIDO 1FA specifications](https://fidoalliance.org/specifications/download/) and [Windows Hello implementation](https://support.microsoft.com/en-us/windows/passkeys-in-windows-301c8944-5ea2-452b-9886-97e4d2ef4422) which [it promotes as a replacement for passwords](https://github.blog/2023-07-12-introducing-passwordless-authentication-on-github-com/). It will result in dire consequencies and is competely inacceptable, [read why](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

If you don't want to participate in harming yourself, it is recommended to follow the lead and migrate somewhere away of GitHub and Micro$oft. Here is [the list of alternatives and rationales to do it](https://github.com/orgs/community/discussions/49869). If they delete the discussion, there are certain well-known places where you can get a copy of it. [Read why you should also leave GitHub](https://codeberg.org/KOLANICH/Fuck-GuanTEEnomo).

---

Python bindings to [JImageHash Java library](https://github.com/KilianB/JImageHash).


Needed jars
-----------

You need the following jars (currently they are hardcoded, we need to decouple, to do it properly we need a special package for doing this):

* `JImageHash-1.0.0.jar` - can be built from https://github.com/KilianB/JImageHash
* `UtilityCode-2.0.1.jar` - can be built from https://github.com/KilianB/UtilityCode
* `JLargeArrays-1.7-SNAPSHOT.jar` - can be built from https://gitlab.com/visnow.org/JLargeArrays , but you need the 2 patches available in `patches` dir of this repo. One fixes building for OpenJDK >11, another one renames the package back.
* `JTransforms-3.2-SNAPSHOT.jar` - can be built from https://github.com/wendykierp/JTransforms
* `commons-math3-debian.jar` - can be installed from `libcommons-math3-java` on Debian/Ubuntu

You can download some prebuilt jars [here](https://github.com/KOLANICH-libs/JImageHash.py/files/8116829/jars.zip) (SHA256: 614ff6ba6712f147ab65d220debb996b7d60e6ca989033776ce33a03db2a407a).

Currently the paths to jars are hardcoded (so you will likely have to change them before building the lib according to your needs), a proper solution requires a separate package discovering jars available in system, such as distro-provided maven repo.
