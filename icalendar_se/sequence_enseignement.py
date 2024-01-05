import argparse
from module_traitement import extract_data, process_data, generate_html

def main():
	 """
    Fonction principale pour créer un emploi du temps à partir de fichiers .ics.

    Utilisation en ligne de commande avec argparse.
    """
    parser = argparse.ArgumentParser(description="Création d'un emploi du temps avec des fichiers.ics")
    parser.add_argument("--input-file", nargs="+", help="Liste des fichiers .ics")
    parser.add_argument("--module", help="Code du module")
    parser.add_argument("--output-dir", help="Répertoire de sortie pour la page web")
    args = parser.parse_args()

    data = extract_data(args.input_file)

    processed_data = process_data(data, args.module)

    generate_html(processed_data, args.output_dir, args.module)

if __name__ == "__main__":
    main()