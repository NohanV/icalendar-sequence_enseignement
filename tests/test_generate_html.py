#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 11:38:03 2024

@author: etudiant
"""

import unittest
import os
from module_traitement import generate_html

class Test_Generate_Html(unittest.TestCase):

    def test_generate_html(self):
        # Données de test
        data = [
            {
                'date': '01/01/2022',
                'start_time': '10:00',
                'end_time': '11:00',
                'duration': '1 hour',
                'course_type': 'Lecture',
                'location': 'Room 101',
                'group': 'Group A',
                'teacher': 'John Doe',
            },
        ]
        output_dir = '../html/'
        module_code = 'R105'

        #Appel de la fonction à tester
        generate_html(data, output_dir, module_code)

        #Vérification du fichier généré
        file_path = os.path.join(output_dir, 'page2.html')
        self.assertTrue(os.path.exists(file_path))


if __name__ == '__main__':
    unittest.main()
