from setuptools import setup

setup(
    name="gasper",
    version="1.0.1",
    description="A static site generator, that will allow you to generate content from database or remote.",
    url="https://github.com/whoisjeeva/gasper",
    author="Jeeva",
    author_email="support@gumify.me",
    license="MIT",
    packages=["gasper"],
    install_requires=[
        "Jinja2==3.1.3",
        "Markdown==3.6",
        "MarkupSafe==2.1.5",
        "peewee==3.17.3",
        "PyMySQL==1.1.0",
        "python-slugify==8.0.4",
        "PyYAML==6.0.1",
        "text-unidecode==1.3",
        "watchdog==4.0.0",
        "requests==2.31.0"
    ],
    entry_points={
        "console_scripts": [
            "gasper = gasper.gasper:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10'
)
