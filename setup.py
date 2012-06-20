from setuptools import setup, find_packages
import os

version = '1.1'

<<<<<<< HEAD
setup(name='vindula.themedefault',
      version=version,
      description="Vindula Theme Default",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
=======
setup(name='vindula.myvindula',
      version=version,
      description="Vindula MyVindula",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
>>>>>>> b6f654b7ba9cf143fff1bd235b03f9c240db5826
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['vindula'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
<<<<<<< HEAD
          'plone.app.theming',
=======
          'plone.app.dexterity',
          'storm',
          
          'plone.namedfile[blobs]',
          #'megrok.z3cform.crud'
>>>>>>> b6f654b7ba9cf143fff1bd235b03f9c240db5826
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
<<<<<<< HEAD

=======
>>>>>>> b6f654b7ba9cf143fff1bd235b03f9c240db5826
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
<<<<<<< HEAD
      paster_plugins=["ZopeSkel"],
=======
      paster_plugins = ["ZopeSkel"],

>>>>>>> b6f654b7ba9cf143fff1bd235b03f9c240db5826
      )
