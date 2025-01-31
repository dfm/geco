from setuptools import setup
from os.path import join as pj
from os import listdir

cppfiles = [pj('geco', 'cppcode', f) for f in listdir('geco/cppcode')]
meshfiles = [pj('geco', 'meshes', f) for f in listdir('geco/meshes')]

setup(name='GECo',
      version='1.0.0',
      packages=['geco'],
      scripts=[pj('bin', 'geco'),
               pj('bin', 'geco-postprocess-data'),
               pj('bin', 'geco-postprocess-print'),
               pj('bin', 'geco-postprocess-moments'),
               pj('bin', 'geco-postprocess-convergence'),
               pj('bin', 'geco-postprocess-deficitangle'),
               pj('bin', 'geco-postprocess-deficitangle-polar'),
               pj('bin', 'geco-postprocess-save-exp-fields'),
               pj('bin', 'geco-postprocess-kretschmann'),
               pj('bin', 'geco-postprocess-2d-density'),
               pj('bin', 'geco-postprocess-2d-ergoregion'),
               pj('bin', 'geco-postprocess-3d-density-box'),
               pj('bin', 'geco-postprocess-3d-density-torus'),
               pj('bin', 'geco-postprocess-3d-ergoregion-box'),
               pj('bin', 'geco-postprocess-3d-ergoregion-torus'),
               pj('bin', 'geco-postprocess-3d-pointcloud-box'),
               pj('bin', 'geco-postprocess-3d-pointcloud-torus'),
               pj('bin', 'run-geco-postprocess.sh')],
      data_files=[(pj('geco','cppcode'), cppfiles),
                  (pj('geco','meshes'), meshfiles)],
      license='GPL v3',
      long_description=open('README.md').read(),
      include_package_data=True)
