#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 12:48:57 2024

@author: etudiant
"""
import sys 
sys.path.append('../icalendar_se/')
import unittest
from unittest.mock import mock_open, patch
from module_traitement import extract_data #importation de la fonction tester

class TestExtractData(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='file_content') #partie réalisé avec la fonction avec l'ouverture et l'extraction des données
    def test_extract_data_solo_file(self, mock_open_file): #fonction pour un fichier
        file_path = 'test_file.ics'
        file_list = [file_path]

        result = extract_data(file_list)

        mock_open_file.assert_called_once_with(file_path, 'r') #partie réalisé avec des assert. Ce qu'on devrait avoir.
        self.assertEqual(result, ['file_content'])

    @patch('builtins.open', new_callable=mock_open, read_data='file_content')
    def test_extract_data_multi_files(self, mock_open_file): #fonction pour plusieurs fichier
        file_list = ['file1.ics', 'file2.ics', 'file3.ics']

        result = extract_data(file_list)

        expected_calls = [unittest.mock.call(file_path, 'r') for file_path in file_list]
        mock_open_file.assert_has_calls(expected_calls, any_order=True)
        self.assertEqual(result, ['file_content', 'file_content', 'file_content'])

if __name__ == '__main__':
    unittest.main()
