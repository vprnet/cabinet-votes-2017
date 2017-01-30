#!/usr/bin/python

from sheet import get_google_sheet

def get_votes():
    full_list = get_google_sheet()
    return full_list
