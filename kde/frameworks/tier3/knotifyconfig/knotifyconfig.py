import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "Configuration system for KNotify"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["libs/qt5/qtbase"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kcompletion"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kservice"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
