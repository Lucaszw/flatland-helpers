import sys

import setuptools as st

sys.path.insert(0, '.')
import version

st.setup(name='flatland-helpers',
         version=version.getVersion(),
         description='Helpers functions, etc. for Flatland.',
         keywords='',
         author='Lucas Zeer',
         author_email='lucas@sci-bots.com',
         url='https://github.com/Lucaszw/flatland-helpers',
         license='BSD',
         packages=['flatland_helpers'],
         install_requires=['conda-helpers'],
         # Install data listed in `MANIFEST.in`
         include_package_data=True)
