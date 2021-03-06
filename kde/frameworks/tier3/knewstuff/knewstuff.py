import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "Support for downloading application assets from the network"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kcompletion"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kitemviews"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/ktextwidgets"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kwidgetsaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
