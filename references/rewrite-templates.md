# Templates de Rewrites

Instructions et formats pour générer des rewrites concrets dans le rapport d'audit.

Toutes les règles anti-AI-tells s'appliquent (voir SKILL.md Phase 4).

---

## 1. Rewrite Publicitaire

### Format de sortie

Pour chaque pub réécrite, produire :

```markdown
### Publicité réécrite #X — Angle : [nom de l'angle]

**Pub originale analysée** :
> [Copier le texte original de la pub]

**Diagnostic** :
- Hook : [force 1-10] — [commentaire]
- Body : [force 1-10] — [commentaire]
- CTA : [force 1-10] — [commentaire]
- Problème principal : [en 1 phrase]

**Rewrite — Version longue (Meta primary text)**

[Texte complet réécrit, prêt à publier]

**Rewrite — Version courte**

[Version condensée, 2-3 lignes + CTA]

**5 variations de hooks**

| # | Hook | Chars | Levier psychologique |
|---|------|-------|---------------------|
| 1 | "..." | XX | Curiosité |
| 2 | "..." | XX | Douleur |
| 3 | "..." | XX | Stat/preuve |
| 4 | "..." | XX | Identité |
| 5 | "..." | XX | Contrarian |

**Headline** : "..." (40 chars max)
**Description** : "..." (30 chars max)
**CTA recommandé** : [bouton]
```

### Règles de rewrite publicitaire

1. **Le hook EST la pub**. 80% du travail est sur les 2 premières lignes.
2. Le hook entre dans la tête du prospect, pas celle de la marque. Pas de nom de marque dans le hook.
3. Garder la curiosité intacte : ne pas révéler le mécanisme/méthode.
4. Chaque variation de hook utilise un levier psychologique différent :
   - Curiosité : "Ce que [groupe] ne vous disent pas sur..."
   - Douleur : "[problème spécifique] ? Voici pourquoi..."
   - Stat/preuve : "[chiffre vérifiable] [résultat]..."
   - Identité : "Pour les [rôle/profil] qui..."
   - Contrarian : "Arrêtez de [croyance commune]..."
   - FOMO : "[X personnes] ont déjà..."
   - Reframe : "Le problème n'est pas [ce qu'ils pensent]..."
5. Body : 1 idée par phrase. Paragraphes courts (1-3 lignes). Mobile-first.
6. Social proof intégrée si disponible (pas plaquée).
7. CTA communique la valeur, pas l'action.

### Trigger

Générer des rewrites publicitaires quand :
- Score publicité < 70
- Des pubs actives ont été collectées en Phase 1
- Les hooks identifiés sont faibles (score < 5/10)

Minimum 2 rewrites, maximum 3.

---

## 2. Rewrite Headlines Site

### Format de sortie

```markdown
### Headlines — Avant/Après

#### Homepage hero
- **Avant** : "{{headline actuel}}"
- **Diagnostic** : [clarté X/10, bénéfice X/10, spécificité X/10]
- **Après — Option A** : "{{rewrite}}"
- **Après — Option B** : "{{rewrite}}"
- **Après — Option C** : "{{rewrite}}"
- **Justification** : [pourquoi c'est mieux, en 1 phrase]

#### Sous-titre hero
- **Avant** : "{{sous-titre actuel}}"
- **Après** : "{{rewrite}}"

#### [Page secondaire — ex: Services]
- **Avant** : "{{headline actuel}}"
- **Après — Option A** : "{{rewrite}}"
- **Après — Option B** : "{{rewrite}}"
```

### Règles de rewrite headline

1. La headline communique le bénéfice principal en 1 phrase.
2. Spécifique > clever. Si le lecteur doit réfléchir pour comprendre, c'est raté.
3. Inclure au moins un élément concret : chiffre, délai, résultat.
4. Tester mentalement : "est-ce que je pourrais mettre le nom d'un concurrent à la place et que ça marche ?" Si oui, c'est trop générique.
5. Format de scoring pour chaque headline :
   - Clarté (0-3) : compréhension immédiate sans contexte
   - Bénéfice (0-3) : le client comprend ce qu'il gagne
   - Spécificité (0-2) : éléments concrets et vérifiables
   - Mémorabilité (0-2) : formulation qu'on retient

### Trigger

Générer des rewrites de headlines quand :
- Score copywriting < 60
- Headline homepage score < 6/10 (via grille CP-08)

Toujours proposer 3 alternatives pour le hero.

---

## 3. Rewrite CTAs

### Format de sortie

```markdown
### CTAs — Avant/Après

| Emplacement | CTA actuel | Problème | CTA réécrit | Amélioration |
|-------------|-----------|----------|-------------|-------------|
| Hero homepage | "En savoir plus" | Générique, pas de valeur | "Recevoir mon audit gratuit" | Communique la valeur reçue |
| Header sticky | "Contact" | Pas de bénéfice | "Réserver ma démo (15 min)" | Réduit la friction + cadre le temps |
| Fin de page | "Soumettre" | Mot mort | "Envoyer ma demande" | Action claire et humaine |
```

### Règles de rewrite CTA

1. Le CTA communique ce que le client REÇOIT, pas ce qu'il FAIT.
   - FAIL : "S'inscrire", "Soumettre", "Envoyer"
   - PASS : "Recevoir mon guide", "Démarrer mon essai gratuit", "Voir les tarifs"
2. Si possible, réduire l'anxiété dans le CTA : "Gratuit", "Sans engagement", "En 2 min".
3. Un seul CTA primaire par page (visuellement dominant).
4. Le CTA est cohérent avec la page de destination.

### Trigger

Toujours inclus dans la section Copywriting du rapport si des CTAs faibles sont détectés (CP-12 ou CP-13 = FAIL).

---

## 4. Réécriture Opt-in Page

### Format de sortie

```markdown
### Page d'opt-in — Réécriture complète

**Page actuelle** : [URL]
**Lead magnet** : [description]
**Taux de conversion estimé** : [X%] (basé sur benchmarks)

**Diagnostic** :
| Critère | Score | Commentaire |
|---------|-------|-------------|
| Headline | X/10 | ... |
| Promesse | X/10 | ... |
| Preuve sociale | X/10 | ... |
| Friction du formulaire | X/10 | ... |
| CTA | X/10 | ... |

**Réécriture proposée** :

---

# [HEADLINE RÉÉCRITE]

## [SOUS-TITRE AVEC BÉNÉFICE CONCRET]

[1 paragraphe : problème que le lead magnet résout — en langage client]

[1 paragraphe : ce que contient le lead magnet — liste à puces 3-5 items]

**Ce que tu vas apprendre :**
- [Bénéfice concret #1]
- [Bénéfice concret #2]
- [Bénéfice concret #3]

[Preuve sociale si disponible : "Déjà téléchargé par X personnes" ou témoignage]

**[CTA : Recevoir [nom du lead magnet] gratuitement]**

[Micro-copy sous le CTA : "Gratuit. Pas de spam. Désabonnement en 1 clic."]

---

**Améliorations par rapport à l'original** :
1. [Amélioration #1]
2. [Amélioration #2]
3. [Amélioration #3]
```

### Règles de réécriture opt-in

1. Le headline de l'opt-in page parle du RÉSULTAT, pas du format.
   - FAIL : "Téléchargez notre ebook"
   - PASS : "Les 7 erreurs qui plombent vos pubs Meta (et comment les corriger)"
2. Formulaire le plus court possible. Email seul sauf raison business forte.
3. Micro-copy sous le CTA pour réduire l'anxiété.
4. Preuve sociale si disponible (nombre de téléchargements, témoignage).
5. Pas de navigation/menu sur une opt-in page (zéro distraction).

### Trigger

Générer quand :
- Score Lead Generation < 60
- Une page d'opt-in existe et a été collectée en Phase 1
- Ou aucune opt-in page n'existe (en proposer une)

---

## 5. Propositions de Posts Sociaux

### Format de sortie (par plateforme)

```markdown
### [Plateforme] — 3 idées de posts

#### Post #1 — [Pilier de contenu]
**Format** : Reel / Carrousel / Post texte / Thread
**Hook** : "..."
**Contenu** :
[Script ou outline du post complet]
**CTA** : [action souhaitée]
**Pourquoi ça marche** : [lien avec l'audience identifiée en Phase 0]

#### Post #2 — [Pilier de contenu]
[même structure]

#### Post #3 — [Pilier de contenu]
[même structure]
```

### Règles de posts sociaux

1. Chaque post a un objectif clair : éduquer, engager, convertir, ou divertir. Pas de mélange.
2. Le hook des 2 premières lignes (ou 3 premières secondes en vidéo) détermine tout.
3. Les 3 posts couvrent des piliers de contenu DIFFÉRENTS.
4. Adapter le format à la plateforme (Reels pour IG, texte long pour LI, threads pour X).
5. Les posts sont prêts à publier, pas des idées vagues.

### Trigger

Générer quand :
- Score réseaux sociaux < 70
- Au moins un handle social a été fourni

3 posts par plateforme active, maximum 4 plateformes = 12 posts max.
