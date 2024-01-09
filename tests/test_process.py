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
from module_traitement import process_data 

class TestProcessData(unittest.TestCase):


    def test_process_data_valid_data(self): #partie traitement de donnée: donnée valide
        data = [
            "BEGIN:VEVENT\nSUMMARY:Event 1\nLOCATION:Salle RT101\nDESCRIPTION:Groupe A\\nTeacher: Tremblais\\nExtra info\nDTSTART:20220101T090000Z\nDTEND:20220101T100000Z\nEND:VEVENT",
            "BEGIN:VEVENT\nSUMMARY:Event 2\nLOCATION:Salle RT102\nDESCRIPTION:Groupe B\\nTeacher: Verdon\\nMore info\nDTSTART:20220102T110000Z\nDTEND:20220102T120000Z\nEND:VEVENT",
        ]
        module_code = "Event 1"

        resultat = process_data(data, module_code)

        expected_resultat = [
            {
                'summary': 'Event 1',
                'location': 'Salle RT101',
                'group': 'Groupe A',
                'teacher': 'Tremblais',
                'start_time': '10:00',
                'date': '01/01/2022',
                'end_time': '11:00',
            }
        ]

        self.assertEqual(resultat, expected_resultat)

    def test_process_data_invalid_module_code(self):  #partie traitement de donnée: donnée non valide
        data = [
            "BEGIN:VEVENT\nSUMMARY:Event 1\nLOCATION:Salle RT101\nDESCRIPTION:Groupe A\\nTeacher: Tremblais\\nExtra info\nDTSTART:20220101T090000Z\nDTEND:20220101T100000Z\nEND:VEVENT",
            "BEGIN:VEVENT\nSUMMARY:Event 2\nLOCATION:Salle RT102\nDESCRIPTION:Groupe B\\nTeacher: Verdon\\nMore info\nDTSTART:20220102T110000Z\nDTEND:20220102T120000Z\nEND:VEVENT",
        ]
        module_code = "Event 3"

        resultat = process_data(data, module_code)

        self.assertEqual(resultat, [])

if __name__ == '__main__':
    unittest.main()
