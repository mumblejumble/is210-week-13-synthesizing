#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Work with pickle file """


import os
import pickle


class PickleCache(object):
    """PickleCache class"""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """PickleCache Class contructor

        Args:
            file_path(str): file name defaults to datastore.pkl.
            autosync(bool): defaults to False

        Attributes:
            __file_path(str): pseudo-private attribute, assigned with file_path
            __data(dict): pseudo-private, stores data in a file as dictionary
            autosync(bool): non-private, assigned by autosync bool value
        """
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """This function creates and updates dictionary in dataset.

        Args:
            key(mixed): key of dictionary.
            value(mixed): values of dictionary

        Returns:
            value or values of specific key.

        Examples:
            >>> pcacher = PickleCache()
            >>> pcacher['a'] = ['b']
            >>> print pcacher._PickleCache__data['a']
            ['b']
        """
        self.__data[key] = value
        if self.autosync is True:
            self.flush()

    def __len__(self):
        """This function measures length of dictionary dataset.

        Returns:
            length of dictionary dataset.

        Examples:
            >>> pcacher = PickleCache()
            >>> pcacher['a'] = ['b']
            >>> print pcacher._PickleCache__data['a']
            ['b']
            >>> len(pcacher)
            1
       """
        sdata_length = len(self.__data)
        return sdata_length

    def __getitem__(self, key):
        """This function tests whether key exist in file dictionary.

        Args:
            key(mixed): key used to access dict key's value

        Returns:
            key's value if key found, otherwise raises errors.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['apple'] = 'banana'
            >>> print pcache['apple']
            'banana'
            >>> pcache['pie']

            Traceback (most recent call last):
              File "<pyshell#14>", line 1, in <module>
                pcache['pie']
            KeyError: 'pie'
        """
        try:
            if self.__data[key]:
                return self.__data[key]
        except (TypeError, KeyError) as errors:
            raise errors

    def __delitem__(self, key):
        """This function deletes dictionary by key.

        Args:
            key(mixed): key used to access dict key's value

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['apple'] = 'banana'
            >>> print len(pcache)
            1
            >>> del pcache['apple']
            >>> print len(pcache)
            0
        """
        if self.__data[key]:
            del self.__data[key]
        if self.autosync is True:
            self.flush()

    def load(self):
        """This function reads and tests pickle file, and loads it into
        file path.

        Examples:
            >>> import pickle
            >>> fh = open('datastore.pk1', 'w')
            >>> pickle.dump({'foo': 'car'}, fh)
            >>> fh.close()
            >>> pcache = PickleCache('datastore.pkl')
            >>> print pcache['foo']
            'car'
        """
        if os.path.exists(self.__file_path) and\
           os.path.getsize(self.__file_path) > 0:
            read_file = open(self.__file_path, 'r')
            self.__data = pickle.load(read_file)
            read_file.close()

    def flush(self):
        """This function saves data found in __data to __file_path.

        Examples:
            >>> pcache = PickleCache()
            >>> pcache['foo'] = 'bar'
            >>> pcache.flush()
            >>> fhandler = open(pcache._PickleCache__file_path, 'r')
            >>> data = pickle.load(fhandler)
            >>> print data
            {'foo': 'bar'}
        """
        write_file = open(self.__file_path, 'w')
        pickle.dump(self.__data, write_file)
        write_file.close()
