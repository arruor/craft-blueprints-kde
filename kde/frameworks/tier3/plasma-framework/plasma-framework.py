import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.versionInfo.setDefaultValues()

        self.description = "Plugin based UI runtime used to write primary user interfaces"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = "default"
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kactivities"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kconfig"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kconfigwidgets"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kdbusaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kdeclarative"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kglobalaccel"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kguiaddons"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kio"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kservice"] = "default"
        self.runtimeDependencies["kde/frameworks/tier1/kwindowsystem"] = "default"
        self.runtimeDependencies["kde/frameworks/tier3/kxmlgui"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kdoctools"] = "default"
        self.runtimeDependencies["kde/frameworks/tier2/kpackage"] = "default"


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)