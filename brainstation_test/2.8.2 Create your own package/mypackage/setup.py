#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

setup(name='mypackage',
      version='0.1',
      description='my awesome package',
      url='www.example.com',
      author='Me',
      packages=['mypackage'],
      install_requires=[
          'numpy',
      ])

