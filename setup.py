#!/usr/bin/env python
import os
from setuptools import setup, find_packages

description = "Chrome extension and python server that allows you to play videos in webpages with MPV instead."

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "play-with-mpv-custom",
    description = description,
    license = "MIT",
    keywords = "mpv video play chrome extension",
    url = "http://github.com/duskyBabz/play-with-mpv-custom",
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],

    py_modules=["play_with_mpv"],
    install_requires=['wheel'],
    entry_points={
        'gui_scripts': [
            'play-with-mpv=play_with_mpv:start',
        ],
    },
    setup_requires=['wheel'],
    desktop_entries={
        'play-with-mpv': {
            'filename': 'duskyBabz.play-with-mpv-custom',
            'Name': 'Play With MPV (server)',
            'Categories': 'AudioVideo;Audio;Video;Player;TV',
            'Comment': description,
            'Icon': 'mpv',
        },
    },
)
