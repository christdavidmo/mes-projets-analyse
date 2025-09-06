---

# 🥂 Analyse des Vins et Spiritueux – README

## 📌 Objectif du projet

Ce projet vise à analyser les performances commerciales et logistiques des produits de la catégorie vins et spiritueux, en croisant les données issues de l’ERP interne et du site web marchand. L’objectif est de mieux comprendre les dynamiques de vente, les préférences des clients, et les enjeux de stock.

---

## 📁 Sources de données

### **0.1.1 Données issues de l’ERP (gestion interne)**  
Ces données reflètent la gestion interne des produits, notamment leur disponibilité, leur coût et leur statut de vente.

| Colonne         | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `product_id`    | Identifiant unique du produit dans le système ERP                          |
| `onsale_web`    | Indique si le produit est en vente sur le site web (1 = oui, 0 = non)      |
| `price`         | Prix de vente affiché sur le site web                                       |
| `stock_quantity`| Quantité de stock disponible                                                |
| `stock_status`  | État du stock (`instock`, `outofstock`, etc.)                              |
| `purchase_price`| Prix d’achat du produit (coût pour l’entreprise)                           |

---

### **0.1.2 Données issues du site web**  
Ces données proviennent de la plateforme e-commerce et permettent d’analyser la visibilité, la popularité et les ventes des produits.

| Colonne              | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| `sku`                | Code produit unique utilisé sur le site web                                 |
| `virtual`            | Produit virtuel (non physique), booléen                                     |
| `downloadable`       | Produit téléchargeable (ex. : PDF, logiciel)                                |
| `rating_count`       | Nombre total d’avis/notes reçues                                            |
| `average_rating`     | Note moyenne attribuée (sur 5)                                              |
| `total_sales`        | Nombre total d’unités vendues                                               |
| `tax_status`         | Statut fiscal (`taxable`, `none`, etc.)                                     |
| `tax_class`          | Classe de taxe applicable                                                   |
| `post_author`        | ID de l’auteur (créateur/modificateur du produit)                          |
| `post_date`          | Date de création de la fiche produit                                        |
| `post_date_gmt`      | Date de création (heure GMT)                                                |
| `post_content`       | Description longue du produit                                               |
| `product_type`       | Type de produit (`simple`, `variable`, etc.)                                |
| `post_title`         | Titre du produit                                                            |
| `post_excerpt`       | Description courte (extrait)                                                |
| `post_status`        | Statut de publication (`publish`, `draft`, etc.)                            |
| `comment_status`     | Autorisation des commentaires (`open`, `closed`)                            |
| `ping_status`        | Notifications externes (peu utilisé)                                        |
| `post_password`      | Mot de passe d’accès (rarement utilisé)                                     |
| `post_name`          | Slug du produit (nom SEO-friendly dans l’URL)                               |
| `post_modified`      | Date de dernière modification                                               |
| `post_modified_gmt`  | Idem, en heure GMT                                                          |
| `post_content_filtered`| Contenu nettoyé (souvent vide ou non utilisé)                            |
| `post_parent`        | ID du parent (produits enfants ou groupés)                                  |
| `guid`               | Lien unique généré automatiquement par WordPress                           |
| `menu_order`         | Ordre d’affichage dans les menus                                            |
| `post_type`          | Type d’objet (`product`, `page`, etc.)                                      |
| `post_mime_type`     | Type MIME du fichier joint (souvent vide)                                   |
| `comment_count`      | Nombre de commentaires ou d’avis laissés                                    |

---

### **0.1.3 Données de liaison entre ERP et site web**  
Ces données permettent de faire le lien entre les deux bases pour une analyse croisée.

| Colonne      | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `id_web`     | Identifiant du produit dans la base web (souvent équivalent à `sku`)       |
| `product_id` | Identifiant du produit dans la base ERP (pour la correspondance interne)   |

---

## 🔍 Pistes d’analyse

- Comparaison entre le prix d’achat (`purchase_price`) et le prix de vente (`price`)
- Corrélation entre la note moyenne (`average_rating`) et les ventes (`total_sales`)
- Analyse du stock (`stock_quantity`, `stock_status`) vs. performance commerciale
- Identification des produits virtuels ou téléchargeables les plus populaires
- Suivi des modifications et publications (`post_modified`, `post_status`)

---

