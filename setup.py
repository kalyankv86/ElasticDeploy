from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='ElasticDeploy',
    version='1.0',
    description='Deploy multiple applications/services/websites on a single elastic beanstalk environment.',
    long_description=readme(),
    keywords='aws elastic beanstalk multi deployment',
    url='https://github.com/tscheiki/ElasticDeploy',
    author='Markus Tscheik',
    author_email='markus.tscheik@gmail.com',
    license='MIT',
    packages=['ed'],
    entry_points={
        'console_scripts': ['ed=ed.main:main'],
    },
    include_package_data=True,
    zip_safe=False
)
