# Jobeet – Django Edition

> Une réinterprétation Django du projet **Jobeet**, initialement popularisé par le tutoriel **Symfony 1.4**.
>
> Ce projet est à la fois **pédagogique**, **nostalgique** et **fonctionnel** : il vise à démontrer comment les concepts fondateurs de Jobeet peuvent être implémentés aujourd’hui avec Django, tout en respectant les bonnes pratiques modernes.

---

## 🧠 À propos de Jobeet

Jobeet est un site d’offres d’emploi fictif utilisé comme fil conducteur dans le célèbre tutoriel Symfony 1.4.  
À une époque où les frameworks PHP structuraient la pensée MVC de toute une génération, Jobeet a servi de **référence didactique** pour comprendre :

- la structuration d’une application web
- la séparation des responsabilités
- les environnements (dev / prod)
- les bonnes pratiques de développement

Ce dépôt propose une **transposition fidèle de ces idées en Django**, sans chercher à faire du Django “magique”, mais plutôt du Django **lisible, explicite et formateur**.

---

## ⚙️ Stack technique

- **Python** 3.11+
- **Django**
- **uv** (gestion des dépendances et environnements)
- **Faker** (données de test)
- **SQLite** (dev) / configurable pour la prod
- **Linux (Xubuntu)** comme environnement de développement

---

## 📁 Structure du projet

```text
project/
├── config/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── dev.py
│   │   └── prod.py
│   ├── urls.py
│   └── wsgi.py
├── jobs/
├── manage.py
├── requirements.txt
└── README.md
```
