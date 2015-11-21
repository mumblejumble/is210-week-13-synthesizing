#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Work with pickle file """


import os
import pickle


class PickleCache(object):
    """PickleCache class"""
    def __init__(self, file_path='datastore.pkl', autosync=False):
        """Class contructor"""
        self.__file_path = file_path
        self.__data = {}
        self.autosync = autosync
        self.load()

    def __setitem__(self, key, value):
        """This function creates or updates dictionary dataset."""
        self.__data[key] = value

    def __len__(self):
        """This function measures length of data."""
        sdata_length = len(self.__data)
        return sdata_length

    def __getitem__(self, key):
        """This function tests whether key exist in file dictionary."""
        try:
            if self.__data[key]:
                return self.__data[key]
        except (TypeError, KeyError) as errors:
            raise errors
        if self.autosync == True:
            self.flush()

    def __delitem__(self, key):
        """This function deletes dictionary by key."""
        if self.__data[key]:
            del self.__data[key]
        if self.autosync == True:
            self.flush()

    def load(self):
        """This function reads and tests pickle file, and loads it into
        file path"""
        if os.path.exists(self.__file_path) and\
           os.path.getsize(self.__file_path) > 0:
            read_file = open(self.__file_path, 'r')
            self.__data = pickle.load(read_file)
            read_file.close()

    def flush(self):
        """This function writes data in pickle file"""
        write_file = open(self.__file_path, 'w')
        pickle.dump(self.__data, write_file)
        write_file.close()
