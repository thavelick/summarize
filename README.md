summarize
=========

A python library for simple text summarization

Installation 
============

First install nltk and numpy:

    sudo pip install nltk
    sudo pip install numpy

Then install the punkt and stopwords nltk packages:

    sudo python -m nltk.downloader -d /usr/share/nltk_data punkt
    sudo python -m nltk.downloader -d /usr/share/nltk_data stopwords

Then, run the tests:

    python run-tests.py

If nothing is output, you're good to go!

Examples
========

See `test/summarize.doctest` for a few simple usage examples


