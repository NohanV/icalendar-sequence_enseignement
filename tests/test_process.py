#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:29:15 2024

@author: etudiant
"""
import sys 
sys.path.append('../icalendar_se/')
import unittest
from datetime import datetime
import pytz
from unittest.mock import mock_open, patch
from module_traitement import extract_data, process_data 

class TestProcessData(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='file_content') #Partie extraction de donnée
    def test_extract_data_solo_file(self, mock_open_file):
        file_path = 'test_file.ics'
        file_list = [file_path]

        result = extract_data(file_list)

        mock_open_file.assert_called_once_with(file_path, 'r')
        self.assertEqual(result, ['file_content'])

    @patch('builtins.open', new_callable=mock_open, read_data='file_content')
    def test_extract_data_multi_files(self, mock_open_file):
        file_list = ['file1.ics', 'file2.ics', 'file3.ics']

        result = extract_data(file_list)

        expected_calls = [unittest.mock.call(file_path, 'r') for file_path in file_list]
        mock_open_file.assert_has_calls(expected_calls, any_order=True)
        self.assertEqual(result, ['file_content', 'file_content', 'file_content'])

    def test_process_data_valid_data(self): #partie traitement de donnée: donnée valide
        data = [
            "BEGIN:VEVENT\nSUMMARY:Event 1\nLOCATION:Room 101\nDESCRIPTION:Group A\\nTeacher: John Doe\\nExtra info\nDTSTART:20220101T090000Z\nDTEND:20220101T100000Z\nEND:VEVENT",
            "BEGIN:VEVENT\nSUMMARY:Event 2\nLOCATION:Room 102\nDESCRIPTION:Group B\\nTeacher: Jane Smith\\nMore info\nDTSTART:20220102T110000Z\nDTEND:20220102T120000Z\nEND:VEVENT",
        ]
        module_code = "Event 1"

        resultat = process_data(data, module_code)

        expected_resultat = [
            {
                'summary': 'Event 1',
                'location': 'Room 101',
                'group': 'Group A',
                'teacher': 'John Doe',
                'start_time': '10:00',
                'date': '01/01/2022',
                'end_time': '11:00',
            }
        ]

        self.assertEqual(resultat, expected_resultat)

    def test_process_data_invalid_module_code(self):  #partie traitement de donnée: donnée non valide
        data = [
            "BEGIN:VEVENT\nSUMMARY:Event 1\nLOCATION:Room 101\nDESCRIPTION:Group A\\nTeacher: John Doe\\nExtra info\nDTSTART:20220101T090000Z\nDTEND:20220101T100000Z\nEND:VEVENT",
            "BEGIN:VEVENT\nSUMMARY:Event 2\nLOCATION:Room 102\nDESCRIPTION:Group B\\nTeacher: Jane Smith\\nMore info\nDTSTART:20220102T110000Z\nDTEND:20220102T120000Z\nEND:VEVENT",
        ]
        module_code = "Event 3"

        resultat = process_data(data, module_code)

        self.assertEqual(resultat, [])

if __name__ == '__main__':
    unittest.main()
