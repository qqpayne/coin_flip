import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

requires = ["pyTelegramBotAPI"]

setup(
    name="coin_flip",
    version="1.0",
    description="Telegram bot that let's you flip a coin in a dialog",
    classifiers=["Programming Language :: Python"],
    author="",
    author_email="",
    keywords="",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    extras_require={},
    install_requires=requires,
    entry_points={
        "console_scripts": [
            "start_coinflip = bot:main",
        ],
    },
)
