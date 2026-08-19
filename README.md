# Veille-automatic

Aruba Firmware Monitor

Script Python permettant de surveiller automatiquement les nouvelles versions de firmware Aruba AOS-CX 6000 publiées sur le portail HPE Networking Support et d'envoyer une notification sur Discord lorsqu'une nouvelle version est détectée.

Fonctionnalités
Recherche des firmwares AOS-CX pour la série Aruba 6000.
Vérification automatique des nouvelles versions.
Comparaison avec le dernier état connu.
Notification Discord en cas de nouveau firmware.
Notification Discord en cas d'erreur d'exécution.
Exécution continue avec une vérification toutes les 24 heures.
Fonctionnement

Le script :

Interroge l'API GraphQL de HPE Networking Support.
Récupère les 20 derniers firmwares disponibles pour les switches Aruba 6000.
Compare les résultats avec ceux du précédent scan.
Détecte les nouvelles versions publiées.
Envoie un message Discord contenant :
les nouveaux firmwares détectés ;
les dernières versions disponibles.
Sauvegarde le nouvel état pour les futures comparaisons.
