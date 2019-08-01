import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shadow-useragent-lobstr",
    version="0.0.1",
    author="Simon Rochwerg",
    author_email="simon.rochwerg@lobstr.io",
    description="Always get best user-agent",
    long_description="Always keep your user-agent updated with the most recent and most common user-agents",
    long_description_content_type="text/markdown",
    url="https://github.com/Lobstrio/shadow-useragent",
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'pytz',
        'coloredlogs'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)