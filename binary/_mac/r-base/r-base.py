# -*- coding: utf-8 -*-

import info

PACKAGE_CRAN_MIRROR = 'http://ftp.gwdg.de/pub/misc/cran'
PACKAGE_PATH = '/bin/macosx/'


class subinfo(info.infoclass):
    def setDependencies(self):
        self.runtimeDependencies["virtual/bin-base"] = "default"

    def setTargets(self):
        for version in ['3.3.3']:
            self.targets[version] = PACKAGE_CRAN_MIRROR + PACKAGE_PATH + 'R-' + version + '.pkg'
        self.defaultTarget = '3.3.3'  # NOTE: Last official build to work with MacOS < 10.11
        self.patchLevel['3.3.3'] = 2


from Package.BinaryPackageBase import *


# Apologies: This is a terrible HACK, but the alternatives are not any good, either.
# Buidling from source requires a) fortran b) specific versions of bzip2, and pcre. And
# c) It will result in an installation that cannot install offical R binar packages.
#
# So, instead, we hack the R installation to run from our path, which works - for the time being.
class Package(BinaryPackageBase):
    def __init__(self):
        BinaryPackageBase.__init__(self)
        # don't use shortcut to unpack into imageDir()
        self.buildSystemType = 'custom'
        # create combined package
        self.subinfo.options.package.withCompiler = None

    def unpack(self):
        workdir = self.workDir()
        utils.cleanDirectory(workdir)
        pkgextractdir = os.path.join(workdir, 'pkgextract')
        cpioextractdir = os.path.join(workdir, 'cpioextractdir')
        for filename in self.localFileNames():  # Should be only one
            utils.system('pkgutil --expand ' + os.path.join(CraftCore.standardDirs.downloadDir(), "archives", self.package.path, filename) + " " + pkgextractdir)
            utils.cleanDirectory(cpioextractdir)
            os.chdir(cpioextractdir)
            utils.system('cat ' + pkgextractdir + '/r.pkg/Payload | gzip -dc | cpio -i')

        return True

    def install(self):
        srcdir = cpioextractdir = os.path.join(self.workDir(), 'cpioextractdir')
        dstdir = os.path.join(self.installDir() ,'lib', 'R')

        utils.cleanDirectory(dstdir)
        utils.copyDir(srcdir, dstdir)

        r_wrapper_rel = os.path.join('R.framework', 'Resources' , 'R')
        r_wrapper = os.path.join(dstdir, r_wrapper_rel)
        # make R run from relative path
        with open(r_wrapper, 'r') as file:
           content  = file.read()
        content = content.replace('\n', '\n# NOTE: RINSTDIR inserted by Craft blueprint, in order to make installation movable.\n'
                                        'RINSTDIR="$0"\n'
                                        'if [ -L "$0" ]; then\n'
                                        '   RINSTDIR=$(dirname "$0")/$(readlink "$0")\n'
                                        'fi\n'
                                        'RINSTDIR=$(dirname $(dirname $(dirname $(dirname "${RINSTDIR}"))))\n', 1)
        content = content.replace('/Library/Frameworks', '${RINSTDIR}')
        with open(r_wrapper, 'w') as file:
           file.write(content)

        utils.createShim(os.path.join(self.imageDir(), 'bin', 'R'), os.path.join(self.imageDir(), 'lib', 'R', r_wrapper_rel))

        return True
