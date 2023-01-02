# Pipeline de filtrage de donnes avec Spark
Ce projet présente un exemple de pipeline Spark permettant de filtrer les lignes d'un fichier de données en fonction de leur valeur de colonne. Le pipeline lit un fichier de données enregistré en local, filtre les lignes qui ont une valeur de colonne supérieure à 50.


# Pipeline Spark
Ce projet contient un exemple de pipeline Spark qui lit un fichier de données enregistré en local, filtre les lignes qui ont une valeur de colonne supérieure à 50 et enregistre le résultat dans un nouveau fichier de données en local.

## Prérequis
Python 3.x
Apache Spark 2.x
Exécution
Pour exécuter le pipeline Spark, utilisez la commande suivante :

## Copy code
spark-submit pipeline.py
Le fichier de données en entrée et le fichier de données en sortie peuvent être modifiés en modifiant les variables input_file et output_file dans le code.

## Résultats
Le fichier de données en sortie contiendra uniquement les lignes qui ont une valeur de colonne supérieure à 50.

## Auteur
BENZEKRI
