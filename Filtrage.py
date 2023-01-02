from pyspark import SparkContext

# Créer un contexte Spark
sc = SparkContext()

# Lire le fichier de données en utilisant un RDD
lines = sc.textFile("data.txt")

# Filtrer les lignes qui ont une valeur de colonne supérieure à 50
filtered_lines = lines.filter(lambda x: int(x.split(",")[1]) > 50)

# Enregistrer le résultat dans un nouveau fichier de données
filtered_lines.saveAsTextFile("filtered_data.txt")

# Arrêter le contexte Spark
sc.stop()
