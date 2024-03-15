from setuptools import setup, find_packages


setup(
    name='django-currency-list',
    version='0.1.1',
    packages=find_packages(),
    license='MIT',
    author='Alex Suvertok',
    author_email='alex.suvertok@gmail.com',
    description='This library simplifies the handling of the currency field in Django projects.',
    long_description=open('README.md').read(),
    url='https://github.com/alex-suvertok/django-currency-list',
    install_requires=[
        'Django>=5.0.1',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.11',
    ],
)
