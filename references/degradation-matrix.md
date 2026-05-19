# Matrice de Dégradation — Audit Marketing

Quand une source de données est indisponible, le skill ne doit JAMAIS échouer complètement (sauf site inaccessible). Cette matrice définit le comportement de fallback pour chaque scénario.

---

## 1. Pas d'accès Meta Ads MCP

**Trigger** : l'utilisateur n'a pas fourni d'accès Meta Business Manager pendant l'intake.

**Impact** : pas de métriques de performance live (CPA, ROAS, CTR, CPM, créas détaillées).

**Fallback** :
- Analyser la bibliothèque publique Meta Ad Library uniquement
- WebFetch sur `facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&q=<entreprise>`
- Extraire : nombre de pubs actives, hooks (premières lignes), formats visuels, CTAs, longévité des pubs
- Si WebFetch bloqué : utiliser agent-browser. Si aussi bloqué : demander screenshots.

**Message rapport** :
> Analyse publicitaire basée sur la bibliothèque publique Meta uniquement. Les métriques de performance (CPA, ROAS, CTR) ne sont pas disponibles sans accès au Business Manager.

**Score** : catégorie Publicité maintenue à 15% mais score plafonné à 70/100.

---

## 2. Pas de handles sociaux

**Trigger** : aucun handle de réseau social fourni pendant l'intake.

**Impact** : section réseaux sociaux vide.

**Fallback** :
- Score social fixé à 0/100
- Recommander d'établir une présence sur minimum Instagram + LinkedIn
- Rechercher si des comptes existent via WebSearch `"nom entreprise" site:instagram.com`

**Message rapport** :
> Aucun réseau social identifié. Score social fixé à 0. Recommandation prioritaire : établir une présence sur au minimum Instagram et LinkedIn.

**Poids** : redistribuer les 10% proportionnellement aux autres catégories.

---

## 3. Pas d'API SEO (DataForSEO)

**Trigger** : DataForSEO MCP non disponible.

**Impact** : pas de données CWV terrain, pas de profil de backlinks, pas de positions SERP.

**Fallback** :
- Audit SEO en mode lab (fetch + analyse HTML directe)
- Analyse centrée sur la homepage et les pages clés
- Core Web Vitals estimés via analyse du code (taille images, scripts bloquants, etc.)

**Message rapport** :
> Audit SEO réalisé en mode lab (sans données terrain). Les Core Web Vitals field et le profil de backlinks nécessitent un accès API DataForSEO pour une analyse complète.

**Poids** : maintenu à 15%, confiance "Partiel".

---

## 4. Site inaccessible

**Trigger** : WebFetch retourne une erreur (DNS failure, connection refused, timeout, 5xx).

**Impact** : CRITIQUE - impossible d'auditer sans accès au site web.

**Fallback** : **ABORT IMMÉDIAT**
- Ne PAS deviner le contenu du site
- Ne PAS tenter d'extrapoler depuis d'autres sources
- Message clair à l'utilisateur

**Message rapport** :
> Site inaccessible. Impossible de réaliser l'audit. Vérifiez l'URL et réessayez.

**Poids** : N/A - l'audit ne peut pas continuer.

---

## 5. Pas de concurrents nommés

**Trigger** : l'utilisateur n'a pas fourni de concurrents pendant l'intake.

**Impact** : pas de benchmark concurrentiel direct.

**Fallback** :
- Utiliser les benchmarks industrie depuis `references/benchmarks.md`
- Tenter une recherche automatique : WebSearch `"top [industrie] [pays]"`
- Proposer les 3 premiers résultats comme concurrents potentiels

**Message rapport** :
> Aucun concurrent direct identifié. Benchmarks basés sur les moyennes de l'industrie [X]. Pour un benchmark concurrentiel personnalisé, fournir 2-3 noms de concurrents.

**Poids** : pas de changement. Les données concurrentielles enrichissent mais ne pilotent pas le scoring.

---

## 6. Instagram bloque le scraping

**Trigger** : agent-browser ou WebFetch retourne une page vide/bloquée pour l'URL Instagram.

**Impact** : pas d'analyse détaillée IG (posts, engagement, qualité du contenu).

**Fallback** :
1. Demander des screenshots à l'utilisateur via AskUserQuestion :
   - Capture du profil (bio, stats)
   - Captures des 9-12 derniers posts
   - Capture des statistiques (si compte business)
2. Si pas de screenshots : analyser uniquement les données profil-level publiques (bio, nombre de posts, followers visibles sur la page).

**Message rapport** :
> Instagram limite l'accès automatisé. Analyse basée sur les données de profil uniquement. Pour un audit IG complet, fournir des captures d'écran des derniers posts et statistiques.

**Poids** : score IG basé sur les données disponibles. Confiance "Partiel".

---

## 7. agent-browser pas installé

**Trigger** : `which agent-browser` retourne vide ou "command not found".

**Impact** : pas de scraping JS-heavy, pas de screenshots automatiques.

**Fallback** :
- Utiliser WebFetch partout
- Confiance réduite sur les sites JS-heavy (SPAs, React, Angular)
- Pas de screenshots automatiques (demander à l'utilisateur si nécessaire)

**Message rapport** :
> agent-browser non détecté. Analyse limitée aux pages accessibles via HTTP direct. Pour des résultats optimaux, installer : `npm i -g agent-browser && agent-browser install`

**Poids** : pas de changement. Ajouter confiance "Partiel" sur les analyses visuelles.

---

## 8. Pas de newsletter / beehiiv

**Trigger** : l'utilisateur indique qu'il n'a pas de newsletter pendant l'intake.

**Impact** : pas d'analyse email marketing.

**Fallback** :
- Sauter la section email dans l'audit
- Ajouter une recommandation pour mettre en place une capture email
- Proposer un lead magnet d'entrée

**Message rapport** :
> Aucune newsletter détectée. L'email marketing est un canal clé pour la rétention et la monétisation. Recommandation : mettre en place une newsletter avec un lead magnet d'entrée.

**Poids** : pas de catégorie dédiée - inclus dans le scoring Lead Generation.

---

## Niveaux de confiance

Chaque section du rapport reçoit un badge de confiance :

| Badge | Signification | Condition |
|-------|--------------|-----------|
| Complet | Toutes les sources de données disponibles, analyse complète | Toutes les données collectées avec succès |
| Partiel | Certaines sources manquantes, analyse basée sur les données disponibles | 1+ source manquante mais analyse possible |
| Limité | Données critiques manquantes, analyse basée sur des signaux minimaux | Données très partielles, faible confiance |

### Règles d'attribution

- **Complet** : WebFetch OK + agent-browser OK + MCP OK (si applicable)
- **Partiel** : WebFetch OK mais agent-browser ou MCP manquant
- **Limité** : seulement des données partielles (screenshots utilisateur ou profil-level)

---

## Tableau récapitulatif

| Scénario | Bloquant ? | Score impacté | Poids | Action |
|----------|-----------|---------------|-------|--------|
| Pas Meta MCP | Non | Plafond 70 sur Pubs | Maintenu | Ad Library publique |
| Pas handles sociaux | Non | 0 sur Social | Redistribué | Recommandation d'établir présence |
| Pas API SEO | Non | Confiance Partiel | Maintenu | Mode lab |
| Site inaccessible | OUI | N/A | N/A | ABORT |
| Pas de concurrents | Non | Aucun | Aucun | Benchmarks industrie |
| IG bloqué | Non | Confiance Partiel | Aucun | Screenshots ou profil-level |
| Pas agent-browser | Non | Confiance Partiel | Aucun | WebFetch partout |
| Pas newsletter | Non | Inclus dans Lead Gen | Aucun | Recommandation |
