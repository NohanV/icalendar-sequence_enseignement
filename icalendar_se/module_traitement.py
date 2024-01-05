"""
.. module:: module_traitement
   :platform: Unix, windows
   :synopsis: module du projet

.. moduleauthor:: VIOT Nohan <nohan.viot@etu.univ-poitiers.fr>


"""

from datetime import datetime
import pytz

def extract_data(file_list):
    """Cette fonction extrait les données des fichiers .ics.

    :param file_list: Liste des chemins des fichiers .ics.
    :type file_list: list
    :returns: Liste des contenus des fichiers .ics.
    :rtype: list
    
    """
    data = []
    for file_path in file_list:
        with open(file_path, 'r') as file:
            data.append(file.read())
    return data

def calculate_duration(start_time, end_time):
    """Calculer la durée entre deux horaires.

    Cette fonction prend deux horaires au format HH:MM et calcule la durée
    entre ces deux horaires. La durée est retournée sous la forme d'une chaîne
    de caractères au format "hh:mm".

    :param start_time: Horaire de début au format HH:MM.
    :type start_time: str
    :param end_time: Horaire de fin au format HH:MM.
    :type end_time: str
    :return: Durée entre l'horaire de début et l'horaire de fin au format "hh:mm".
    :rtype: str
    :raises: ValueError si les horaires sont mal formatés.
    :example:

    .. code-block:: python

        duration = calculate_duration("09:00", "10:30")
        # Résultat attendu : "1h30"
        
    """
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')
    duration = end - start
    hours, remainder = divmod(duration.seconds, 3600)
    minutes = remainder // 60
    return f"{hours}h{minutes:02d}"

def extract_course_type(summary):
    """Extraire le type de cours à partir du nom du cours.

    :param summary: Nom du cours.
    :type summary: str
    :return: Type de cours (TD, TP, CM, ctrl TP, ctrl).
    :rtype: str
    """
    course_types = ['TD', 'TP', 'CM', 'ctrl TP', 'ctrl tp', 'ctrl']
    
    terms = summary.split()
    if len(terms) >= 2:
        last_two_terms = ' '.join(terms[-2:])
        if last_two_terms in course_types:
            return last_two_terms

    if len(terms) >= 1 and terms[-1] in course_types:
        return terms[-1]

    return ''

def process_data(data, module_code):
    """Cette fonction traite les données extraites des fichiers .ics.

    :param data: Données extraites des fichiers .ics.
    :type data: list
    :param module_code: Code du module à filtrer.
    :type module_code: str
    :returns: Liste des séances d'enseignement du module spécifié.
    :rtype: list
    
    """
    processed_data = []

    for ics_content in data:
        lines = ics_content.split('\n')
        events = []
        current_event = None

        for line in lines:
            if line.startswith('BEGIN:VEVENT'):
                current_event = {}
            elif line.startswith('SUMMARY:'):
                current_event['summary'] = line.split(':')[-1]
            elif line.startswith('LOCATION:'):
                current_event['location'] = line.split(':')[-1]
            elif line.startswith('DESCRIPTION:'):
                   description_parts = line.split('\\n')
                   if len(description_parts) >= 4:
                          current_event['group'] = description_parts[2].strip()
                          current_event['teacher'] = description_parts[3].strip()
            elif line.startswith('DTSTART:'):
                start_time = line.split(':')[-1]
                utc_start_time = datetime.strptime(start_time, '%Y%m%dT%H%M%SZ')
                paris_timezone = pytz.timezone('Europe/Paris')
                local_start_time = utc_start_time.replace(tzinfo=pytz.utc).astimezone(paris_timezone)      
                current_event['start_time'] = local_start_time.strftime('%H:%M')
                current_event['date'] = local_start_time.strftime('%d-%m-%Y')
            elif line.startswith('DTEND:'):
                end_time = line.split(':')[-1]
                utc_end_time = datetime.strptime(end_time, '%Y%m%dT%H%M%SZ')
                paris_timezone = pytz.timezone('Europe/Paris')
                local_end_time = utc_end_time.replace(tzinfo=pytz.utc).astimezone(paris_timezone)
                current_event['end_time'] = local_end_time.strftime('%H:%M')
            elif line.startswith('END:VEVENT'):
                events.append(current_event)

        for event in events:
            if module_code in event.get('summary', ''):
                summary = event.get('summary', '')
                course_type = extract_course_type(summary)
                event['course_type'] = course_type
                start_time = event.get('start_time', '')
                end_time = event.get('end_time', '')
                event['duration'] = calculate_duration(start_time, end_time)
                processed_data.append(event)

    processed_data.sort(key=lambda x: datetime.strptime(x['date'], '%d-%m-%Y'))

    return processed_data

def generate_html(data, output_dir, module_code):
    """Cette fonction génère une page HTML à partir des données traitées.

    :param data: Données traitées des séances d'enseignement.
    :type data: list
    :param output_dir: Répertoire de sortie pour la page web.
    :type output_dir: str
    :param module_code: Code du module affiché dans le titre de la page HTML.
    :type module_code: str
    
    """
    html_content = f"""
    <html>
    <head>
        <style>
            table {{
                border-collapse: collapse;
                width: 100%;
                font-family: Arial, sans-serif;
                margin-top: 20px;
            }}
            th, td {{
                border: 1px solid #dddddd;
                text-align: left;
                padding: 8px;
            }}
            th {{
                background-color: #f2f2f2;
            }}
            tr:nth-child(even) {{
                background-color: #f9f9f9;
            }}
            h1 {{
                text-align: center;
            }}
        </style>
    </head>
    <body>
        <h1>Emploi du temps - Module {module_code}</h1>
        <table>
            <tr>
                <th>Date</th>
                <th>Horaire de début</th>
                <th>Horaire de fin</th>
                <th>Durée</th>
                <th>Type de cours</th>
                <th>Salle</th>
                <th>Groupe</th>
                <th>Enseignant</th>
            </tr>
    """

    for event in data:
        html_content += f"""
            <tr>
                <td>{event['date']}</td>
                <td>{event['start_time']}</td>
                <td>{event['end_time']}</td>
                <td>{event['duration']}</td>
                <td>{event.get('course_type', '')}</td>
                <td>{event.get('location', '')}</td>
                <td>{event.get('group', '')}</td>
                <td>{event.get('teacher', '')}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_dir + 'page1.html', 'w') as file:
        file.write(html_content)