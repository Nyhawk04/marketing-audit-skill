# Framework Suggestions A/B Test

Generer des suggestions d'A/B tests concretes basees sur les scores de l'audit. Chaque suggestion inclut : quoi tester, hypothese, metrique, et lift attendu.

---

## Regles de declenchement

| Condition | Nombre de suggestions |
|-----------|----------------------|
| Score categorie < 40 (F) | 3 tests pour cette categorie |
| Score categorie 40-59 (D) | 2 tests |
| Score categorie 60-74 (C) | 1 test |
| Score categorie >= 75 | 0 (pas prioritaire) |

Maximum 10 suggestions par rapport. Prioriser les categories a plus fort poids.

---

## Format de sortie

```markdown
### A/B Test #X — [Categorie]

**Element a tester** : [element precis — headline, CTA, layout, hook, format]
**Variante A (controle)** : [version actuelle]
**Variante B (test)** : [version proposee]
**Hypothese** : [Si on change X, alors Y parce que Z]
**Metrique principale** : [CTR, taux de conversion, engagement rate, bounce rate, etc.]
**Lift attendu** : [+X% a +Y%] (base sur les benchmarks industrie)
**Duree recommandee** : [X jours/semaines — basee sur le trafic estime]
**Difficulte d'implementation** : [Facile / Moyen / Complexe]
```

---

## Tests par categorie

### Site & Conversion (CRO)

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| Hero headline score < 6/10 | Headline actuelle vs rewrite proposee | Bounce rate, scroll depth | -10 a -25% bounce |
| CTA generique detecte | CTA oriente valeur vs CTA actuel | Click-through rate | +15 a +40% CTR |
| Pas de trust signals above the fold | Avec vs sans logos/temoignages au-dessus du fold | Conversion rate | +5 a +15% conversion |
| Formulaire > 3 champs | Formulaire court (email seul) vs formulaire actuel | Form completion rate | +20 a +50% completion |
| Pas de sticky CTA mobile | Avec vs sans barre CTA fixe en mobile | Mobile conversion | +10 a +25% conversion |

### SEO

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| Title tags faibles | Title optimise (keyword + benefice) vs actuel | CTR organique | +15 a +30% CTR |
| Meta descriptions manquantes | Meta redigee (avec CTA) vs auto-generee | CTR SERP | +10 a +25% CTR |
| Content thin detecte | Article enrichi (2x longueur + FAQ) vs actuel | Temps sur page, rankings | +20 a +40% temps |
| Pas de FAQ schema | Avec vs sans FAQ schema markup | Impressions SERP | +10 a +30% impressions |

### Copywriting & Messaging

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| USP generique | USP reecrite (specifique + chiffree) vs actuelle | Time on page, conversion | +10 a +20% conversion |
| Promesse non chiffree | Version avec chiffre concret vs sans | Credibilite percue (survey), conversion | +5 a +15% |
| Voix incoherente cross-canal | Ton unifie vs ton actuel (test sur landing page) | Bounce rate | -5 a -15% bounce |
| Objections non adressees | Section FAQ/objections ajoutee vs page actuelle | Conversion | +10 a +20% |

### Publicite

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| Hook pub score < 5/10 | 5 variations de hooks (voir rewrite-templates.md) | Hook rate, CTR | +20 a +50% CTR |
| Copy longue uniquement | Version courte (2-3 lignes) vs longue | CTR, CPA | -10 a -30% CPA |
| Pas de video dans les pubs | Creative video vs statique | ROAS, CPA | +20 a +60% ROAS |
| Meme angle sur toutes les pubs | 3 angles differents (douleur, preuve, identite) | CTR, fatigue creative | +15 a +35% CTR |
| CTA pub generique | CTA oriente benefice vs "En savoir plus" | CTR | +10 a +25% CTR |

### Reseaux sociaux

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| Engagement < benchmark | Hook dans les 2 premieres lignes vs info directe | Engagement rate | +20 a +40% |
| Pas de CTA dans les posts | Post avec CTA clair vs sans | Clicks, saves, shares | +15 a +30% clicks |
| Un seul format utilise | Nouveau format (carrousel, reel, thread) vs habituel | Reach, engagement | +30 a +60% reach |
| Bio incomplete | Bio optimisee (valeur + CTA + social proof) vs actuelle | Profile visits to follow ratio | +10 a +25% |

### Lead Generation

| Trigger | Test | Metrique | Lift typique |
|---------|------|----------|-------------|
| Opt-in headline generique | Headline orientee resultat vs orientee format | Opt-in rate | +20 a +40% |
| Formulaire avec > 2 champs | Email seul vs email + prenom | Opt-in rate | +15 a +30% |
| Pas de micro-copy sous CTA | Avec ("Gratuit, 0 spam") vs sans | Opt-in rate | +5 a +15% |
| Lead magnet type guide PDF | Quiz interactif vs PDF | Opt-in rate, qualification | +30 a +60% opt-in |
| Pas de pop-up exit intent | Pop-up exit intent vs sans | Lead capture rate | +3 a +8% des visiteurs sortants |

---

## Priorisation des tests

Trier les suggestions par score de priorite :

```
Score_priorite = Poids_categorie × (100 - Score_categorie) × Impact_lift_moyen
```

Presenter les 5-10 tests a plus fort score dans la section Plan d'Action du rapport, sous une rubrique "Tests A/B recommandes".

---

## Regles de redaction

1. Chaque test est ancre dans un finding specifique du rapport (pas generique).
2. Variante B = le rewrite propose dans la section correspondante quand disponible.
3. Les lifts attendus sont des fourchettes, pas des chiffres exacts.
4. Mentionner la duree de test recommandee (fonction du trafic estime).
5. Anti-AI-tells appliques (voir anti-ai-tells.md).
