# 🚢 Analyse des données du Titanic – README

## 🎯 Objectif du projet

Ce projet vise à explorer les facteurs ayant influencé la survie des passagers du Titanic. À travers une analyse statistique et visuelle, l’objectif est de dégager des tendances liées à la classe sociale, l’âge, le sexe, et les relations familiales à bord.

---

## 📁 Description des variables

Le tableau ci-dessous présente les colonnes du dataset et leur signification :

| Colonne         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `survived`      | Statut de survie : `1` = survécu, `0` = décédé                             |
| `pclass`        | Classe du billet : `1` = première, `2` = deuxième, `3` = troisième          |
| `sex`           | Sexe de la personne (`male` ou `female`)                                   |
| `age`           | Âge du passager                                                            |
| `sibsp`         | Nombre de frères/sœurs ou conjoints à bord                                 |
| `parch`         | Nombre de parents ou enfants à bord                                        |
| `fare`          | Tarif du billet payé                                                       |
| `embarked`      | Port d’embarquement (`C` = Cherbourg, `Q` = Queenstown, `S` = Southampton) |
| `class`         | Classe sous forme textuelle (`First`, `Second`, `Third`)                  |
| `who`           | Type de personne (`man`, `woman`, `child`) basé sur l’âge et le sexe      |
| `adult_male`    | Booléen : est-ce un homme adulte (`True` ou `False`)                      |
| `deck`          | Pont de la cabine (`A`, `B`, ..., `NaN` = inconnu)                         |
| `embark_town`   | Ville d’embarquement (`Cherbourg`, `Southampton`, ...)                    |
| `alive`         | Statut (`yes` pour vivant, `no` pour décédé)                              |
| `alone`         | Booléen : voyageait-il seul ? (`True` ou `False`)                         |

---

## 🔍 Pistes d’analyse

- Taux de survie par classe (`pclass`) et par sexe (`sex`)
- Influence de l’âge (`age`) sur la probabilité de survie
- Impact des relations à bord (`sibsp`, `parch`) sur le statut `alone`
- Répartition des survivants par pont (`deck`) et port d’embarquement (`embarked`)
- Visualisation des profils types (`who`) et leur lien avec la survie

---
