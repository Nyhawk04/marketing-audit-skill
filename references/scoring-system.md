# Système de Scoring — Audit Marketing

## Formule globale

```
S_total = Σ(Score_catégorie × Poids) / Σ(Poids_actives) × 100
```

Seules les catégories avec des données disponibles sont incluses dans le calcul (Poids_actives).

---

## Pondérations par catégorie

| Catégorie | Poids | Source de scoring | Checks |
|-----------|-------|-------------------|--------|
| Site & Conversion (CRO) | 20% | page-cro | 12 checks |
| SEO (Technique + Contenu) | 15% | seo-audit | 15 checks |
| Copywriting & Messaging | 15% | copywriting + checklist | 10 checks |
| Publicité payante | 15% | ads-meta + Ad Library | 10 checks |
| Réseaux sociaux | 10% | social-content + checklist | 8 checks par plateforme |
| Stratégie de contenu | 10% | content-strategy | 8 checks |
| Lead Generation & Funnels | 10% | lead-magnets | 8 checks |
| Business Model & Stratégie | 5% | brand + checklist | 7 checks |

---

## Scoring par check individuel

Chaque catégorie contient 5-15 checks individuels. Chaque check est évalué :

| Résultat | Points | Description |
|----------|--------|-------------|
| PASS | 100% des points | Critère rempli correctement |
| WARNING | 50% des points | Partiellement rempli ou améliorable |
| FAIL | 0% des points | Critère non rempli |
| N/A | Exclu du calcul | Non applicable au contexte |

### Multiplicateurs de sévérité

Chaque check a un niveau de sévérité qui pondère son importance dans le score de la catégorie :

| Sévérité | Multiplicateur | Critère |
|----------|---------------|---------|
| Critical | 5.0× | Bloque le revenu ou casse la confiance |
| High | 3.0× | Impact significatif sur la performance |
| Medium | 1.5× | Opportunité d'optimisation |
| Low | 0.5× | Nice-to-have |

### Calcul du score d'une catégorie

```
Score_catégorie = Σ(Score_check × Multiplicateur_sévérité) / Σ(Multiplicateur_sévérité_max) × 100
```

Où :
- `Score_check` = 1.0 (PASS), 0.5 (WARNING), 0.0 (FAIL)
- `Multiplicateur_sévérité_max` = la somme si tous les checks étaient PASS

---

## Échelle de grades

| Grade | Score | Label | Couleur HEX | Emoji |
|-------|-------|-------|-------------|-------|
| A | 90-100 | Excellent | #22c55e | vert |
| B | 75-89 | Bon | #84cc16 | vert-jaune |
| C | 60-74 | À améliorer | #eab308 | jaune |
| D | 40-59 | Faible | #f97316 | orange |
| F | <40 | Critique | #ef4444 | rouge |

---

## Redistribution adaptive des poids

Quand une catégorie n'a pas de données (ex : pas de publicité payante) :

### Formule de redistribution

```
Nouveau_Poids_i = Poids_original_i / (1 - Σ(Poids_retirés))
```

### Exemple : pas de publicité (15% retiré)

| Catégorie | Poids original | Nouveau poids |
|-----------|---------------|---------------|
| Site & CRO | 20% | 23.5% |
| SEO | 15% | 17.6% |
| Copywriting | 15% | 17.6% |
| ~~Publicité~~ | ~~15%~~ | ~~exclu~~ |
| Réseaux sociaux | 10% | 11.8% |
| Stratégie contenu | 10% | 11.8% |
| Lead Generation | 10% | 11.8% |
| Business Model | 5% | 5.9% |

### Exemple : pas de pubs + pas de réseaux sociaux (25% retiré)

| Catégorie | Poids original | Nouveau poids |
|-----------|---------------|---------------|
| Site & CRO | 20% | 26.7% |
| SEO | 15% | 20.0% |
| Copywriting | 15% | 20.0% |
| Stratégie contenu | 10% | 13.3% |
| Lead Generation | 10% | 13.3% |
| Business Model | 5% | 6.7% |

Toujours documenter dans le rapport : "Catégories exclues : [liste]. Poids redistribués proportionnellement."

---

## Identification des Quick Wins

Un finding qualifie comme Quick Win quand :
1. Sévérité >= High
2. Temps de fix estimé < 15 minutes
3. Impact concret et mesurable

### Tri des Quick Wins

```
Score_priorité = Multiplicateur_sévérité × Impact_estimé
```

Trier par `Score_priorité` décroissant. Présenter les 10 premiers.

---

## Synthèse cross-catégories

Après le scoring individuel, analyser :

### Problèmes systémiques
Identifier les patterns qui apparaissent dans 3+ catégories.
Exemple : "Manque de spécificité" detecté dans USP (copy), headlines (ads), bio (social) = problème de positionnement fondamental.

### Effets cascade
Identifier les fixes qui améliorent plusieurs scores simultanément.
Exemple : réécrire la value proposition impacte CRO + Copy + Ads + Lead Gen.

### Contradictions
Identifier les incohérences entre catégories.
Exemple : score SEO élevé mais score contenu faible = trafic organique qui arrive sur du contenu qui ne convertit pas.

### Synthèse stratégique
En 3-5 phrases, résumer :
- La santé marketing globale
- Le problème racine (#1 à résoudre en priorité)
- Le quick win à plus fort impact
- La recommandation stratégique principale

---

## Plafonnement de score

Certaines conditions limitent le score maximum atteignable :

| Condition | Score max |
|-----------|----------|
| Pas d'accès Meta Ads MCP (analyse Ad Library seule) | 70/100 pour la catégorie Publicité |
| agent-browser non disponible (pas de screenshots) | Confiance "Partiel" sur les analyses visuelles |
| Pas de données SEO field (lab only) | 80/100 pour la catégorie SEO |

---

## Format de reporting du score

Pour chaque catégorie dans le rapport :

```
## [Catégorie] — Score : XX/100 (Grade X) [Confiance]

### Détail des checks
| # | Check | Sévérité | Résultat | Commentaire |
|---|-------|----------|----------|-------------|
| 1 | [Description] | Critical | PASS | [Détail] |
| 2 | [Description] | High | FAIL | [Détail + recommandation] |
```
