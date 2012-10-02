# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

tests_require = ['zope.testing']

setup(name='maurits.i18ntalk',
      version='1.0.dev0',
      description="Demo package for i18n talk of Maurits at ploneconf 2012",
      long_description=(open("README.txt").read() + "\n" +
                        open("CHANGES.rst").read()),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
          'Framework :: Plone',
          "Framework :: Plone :: 4.0",
          "Framework :: Plone :: 4.1",
          "Framework :: Plone :: 4.2",
          "Framework :: Plone :: 4.3",
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          ],
      keywords='i18n locales ploneconf',
      author='Maurits van Rees',
      author_email='m.van.rees@zestsoftware.nl',
      url='https://github.com/mauritsvanrees/cmaurits.i18ntalk',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['maurits', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=['setuptools',
                        # -*- Extra requirements: -*-
                        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      test_suite='maurits.i18ntalk.tests.test_docs.test_suite',
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
