# sequence_enseignement.py
import argparse
from nom_module_projet import extract_data, process_data, generate_html

def main():
    parser = argparse.ArgumentParser(description="Création d'un emploi du temps avec des fichiers.ics")
    parser.add_argument("--input-file", nargs="+", help="Liste des fichiers .ics")
    parser.add_argument("--module", help="Code du module")
    parser.add_argument("--output-dir", help="Répertoire de sortie pour la page web")
    args = parser.parse_args()

    # Extraction des données
    data = extract_data(args.input_file)

    # Traitement des données
    processed_data = process_data(data, args.module)

    # Génération de la page HTML
    generate_html(processed_data, args.output_dir)

if __name__ == "__main__":
    main()

