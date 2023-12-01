from distutils.core import setup

REQUIRES = [
    'records',
    'structlog',
    'allure-pytest'
]

setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/zakharovyn/db_client.git',
    license='MIT',
    author='yanzakharov',
    author_email='-',
    install_requires=REQUIRES,
    description='db client with allure and logger'
)
