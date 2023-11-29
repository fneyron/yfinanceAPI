# Stock Data API

## Description
Stock Data API est une application Flask qui fournit des données financières en temps réel en utilisant YFinance. Cette API permet aux utilisateurs de récupérer des données historiques, des informations sur les dividendes, les splits d'actions, et plus encore pour différents symboles boursiers.

## Fonctionnalités
- Récupération des données historiques des actions.
- Consultation des informations sur les dividendes et les splits d'actions.
- Accès aux bilans, aux flux de trésorerie, et aux données sur les bénéfices.

## Installation
Pour utiliser cette API, suivez ces étapes :

1. Clonez le dépôt :
   ```K
   git clone 
   ```
2. Installez les dépendances :
   ```
   pip install -r requirements.txt
   ```
3. Lancez le serveur Flask :
   ```
   python app.py
   ```

## Utilisation

### Endpoints
- `/historical-data`: Récupère les données historiques pour un symbole donné.
- `/dividends`: Obtient les informations sur les dividendes pour un symbole spécifique.
- `/splits`: Récupère les données sur les splits d'actions pour un symbole donné.
- `/balance-sheet`: Accède au bilan d'un symbole spécifique.
- `/cash-flow`: Obtient les informations sur les flux de trésorerie.
- `/earnings`: Récupère les données sur les bénéfices.
- `/financials`: Accède aux informations financières détaillées.

### Exemples de Requêtes
Pour effectuer une requête à l'API, utilisez le format suivant :
```
GET /historical-data?symbol=AAPL
```
Remplacez `AAPL` par le symbole boursier de votre choix.

## Contributions
Les contributions à ce projet sont les bienvenues. Veuillez suivre les bonnes pratiques de développement et soumettre des pull requests pour toute proposition de modification ou d'ajout de fonctionnalités.

