---

# 🧾 Analyse des données de facturation – README

## 🎯 Objectif du projet

Ce projet vise à explorer les comportements d’achat des clients à travers les données de facturation d’un commerce multi-branches. L’analyse porte sur les ventes, les marges, les types de produits et les préférences de paiement, afin d’identifier des leviers d’optimisation commerciale.

---

## 📁 Description des variables

Le tableau ci-dessous présente les colonnes du dataset et leur signification :

| Colonne                  | Description                                                                 |
|--------------------------|-----------------------------------------------------------------------------|
| `Invoice ID`             | Identifiant unique de la facture                                            |
| `Branch`                 | Code de la succursale (`A`, `B`, `C`, etc.)                                 |
| `City`                   | Ville où la transaction a eu lieu                                           |
| `Customer type`          | Type de client (`Member`, `Normal`)                                        |
| `Gender`                 | Sexe du client (`Male`, `Female`)                                          |
| `Product line`           | Catégorie de produit (ex. : `Health`, `Electronic`, `Food`, etc.)          |
| `Unit price`             | Prix unitaire du produit                                                    |
| `Quantity`               | Quantité achetée                                                            |
| `Tax 5%`                 | Montant de la taxe appliquée (5% du total)                                 |
| `Sales`                  | Montant total de la vente (incluant la taxe)                               |
| `Date`                   | Date de la transaction                                                      |
| `Time`                   | Heure de la transaction                                                     |
| `Payment`                | Mode de paiement (`Cash`, `Credit card`, `Ewallet`, etc.)                  |
| `cogs`                   | Coût des marchandises vendues (Cost of Goods Sold)                         |
| `gross margin percentage`| Pourcentage de marge brute (souvent constant, ex. : 4.76%)                 |
| `gross income`           | Revenu brut généré par la vente (avant impôts et charges)                  |
| `Rating`                 | Évaluation du service par le client (sur 10)                               |

---

## 🔍 Pistes d’analyse

- Comparaison des ventes par ville et par succursale (`City`, `Branch`)
- Analyse des marges par ligne de produit (`Product line`)
- Comportement des clients selon le type (`Customer type`) et le sexe (`Gender`)
- Répartition des modes de paiement (`Payment`)
- Corrélation entre la satisfaction (`Rating`) et les revenus (`gross income`)
- Analyse temporelle des ventes (`Date`, `Time`) pour identifier les heures et jours forts

---