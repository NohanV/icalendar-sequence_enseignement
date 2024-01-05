from datetime import datetime
import pytz

def extract_data(file_list):
    # Fonction pour extraire les données des fichiers .ics
    data = []
    for file_path in file_list:
        with open(file_path, 'r') as file:
            data.append(file.read())
    return data

def process_data(data, module_code):
    # Fonction pour traiter les données
    processed_data = []  # Liste stockage des données

    for ics_content in data:
        lines = ics_content.split('\n')
        events = []
        current_event = None

        for line in lines:
            if line.startswith('BEGIN:VEVENT'): # Commencement de l'evenement
                current_event = {}
            elif line.startswith('SUMMARY:'):  # Intitulé de l'événement
                current_event['summary'] = line.split(':')[-1]
            elif line.startswith('LOCATION:'):  # Lieu de l'événement
                current_event['location'] = line.split(':')[-1]
            elif line.startswith('DESCRIPTION:'):  # Description de l'événement
                   description_parts = line.split('\\n')
                   if len(description_parts) >= 4:
                          current_event['group'] = description_parts[2].strip()  # Groupe associé à l'événement
                          current_event['teacher'] = description_parts[3].strip()  # Enseignant associé à l'événement
            elif line.startswith('DTSTART:'):  # Date de début de l'événement
                start_time = line.split(':')[-1]
                utc_start_time = datetime.strptime(start_time, '%Y%m%dT%H%M%SZ')
                paris_timezone = pytz.timezone('Europe/Paris')
                local_start_time = utc_start_time.replace(tzinfo=pytz.utc).astimezone(paris_timezone)      
                current_event['start_time'] = local_start_time.strftime('%H:%M')
                current_event['date'] = local_start_time.strftime('%d/%m/%Y')
            elif line.startswith('DTEND:'):  # Date de fin de l'événement
                end_time = line.split(':')[-1]
                utc_end_time = datetime.strptime(end_time, '%Y%m%dT%H%M%SZ')
                paris_timezone = pytz.timezone('Europe/Paris')
                local_end_time = utc_end_time.replace(tzinfo=pytz.utc).astimezone(paris_timezone)
                current_event['end_time'] = local_end_time.strftime('%H:%M')
            elif line.startswith('END:VEVENT'):  # Fin de l'événement, ajout à la liste
                events.append(current_event)

        processed_data.extend([event for event in events if module_code in event.get('summary', '')])

    processed_data.sort(key=lambda x: datetime.strptime(x['date'], '%d/%m/%Y'))

    return processed_data

def generate_html(data, output_dir):
    # Fonction pour générer la page HTML
    html_content = """
    <html>
    <head>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
            }
            th, td {
                border: 1px solid black;
                padding: 8px;
                text-align: center;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <table border="1">
            <tr>
					 <th>Date</th>                
                <th>Horaire de début</th>
                <th>Horaire de fin</th>
                <th>Nom du cours</th>
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
                <td>{event.get('summary', '')}</td>
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
