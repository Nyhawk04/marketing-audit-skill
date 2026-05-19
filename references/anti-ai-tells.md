# Regles Anti-AI-Tells

Checklist obligatoire pour tout texte genere dans le rapport d'audit : rewrites, analyses, recommandations, lead magnets, calendrier de contenu, sequences email.

---

## Regles absolues (FAIL = rewrite immediat)

### 1. Tirets cadratins interdits
- Remplacer `—` (em dash) par `:`, `,`, `.` ou restructurer la phrase.
- Le tiret cadratin est le marqueur AI le plus detecte par les lecteurs.

### 2. Pas de cascade "Pas X. Pas Y. Mais Z."
- Ce pattern est un tic de generation. Reformuler.
- FAIL : "Pas de trafic. Pas de leads. Mais un potentiel enorme."
- PASS : "Le trafic et les leads sont faibles, mais le potentiel est reel."

### 3. Pas de fragments sans verbe en serie
- 3+ phrases sans verbe conjugue d'affilee = tic AI.
- FAIL : "Un site clean. Des visuels pros. Une value prop claire."
- PASS : "Le site est clean, les visuels sont pros et la value prop se comprend en 3 secondes."

### 4. Pas de meta-commentaire
- Ne pas commenter le fait qu'on ecrit, qu'on analyse, ou qu'on est un AI.
- FAIL : "Dans cette section, nous allons analyser..."
- FAIL : "Voici notre analyse de..."
- PASS : Commencer directement par le contenu.

### 5. Pas de listes a puces decoratives
- Chaque bullet apporte de l'info nouvelle. Pas de padding.
- FAIL : "- Une approche innovante" / "- Des resultats concrets" / "- Une expertise reconnue"
- PASS : bullets avec des chiffres, des faits, des exemples specifiques.

---

## Patterns a eviter (WARNING)

### 6. Superlatifs vides
- "Exceptionnel", "remarquable", "impressionnant", "revolutionnaire" sans preuve = WARNING.
- Remplacer par un chiffre ou un fait verifiable.

### 7. Adverbes d'intensite en rafale
- "Vraiment", "absolument", "totalement", "fondamentalement" utilises pour gonfler.
- 1 par paragraphe max. Preferer la precision a l'intensite.

### 8. Ouvertures generiques
- FAIL : "Dans le monde du marketing digital d'aujourd'hui..."
- FAIL : "A l'ere du numerique..."
- FAIL : "Il est essentiel de comprendre que..."
- PASS : Commencer par un fait, un chiffre, ou le sujet direct.

### 9. Conclusions en echo
- Ne pas repeter le contenu de la section en conclusion.
- La conclusion ajoute une perspective, pas un resume.

### 10. Fausse personnalisation
- FAIL : "En tant que [industrie], vous savez que..." (presomption)
- PASS : S'appuyer sur les donnees collectees, pas sur des hypotheses.

---

## Patterns valides (a utiliser)

### Ton recommande
- Direct, factuel, ancre dans les donnees.
- Phrases courtes. Un paragraphe = une idee.
- Registre : professionnel-decontracte. Ni robot, ni pote.
- Conjugaisons actives : "le CTA ne communique pas la valeur" > "la valeur n'est pas communiquee par le CTA".

### Transitions naturelles
- Utiliser la logique du raisonnement, pas des connecteurs forces.
- FAIL : "Par consequent", "En outre", "Il convient de noter que"
- PASS : enchainer les idees par leur lien causal naturel.

### Donnees > opinions
- Chaque affirmation forte est soutenue par un element collecte en Phase 1.
- "Le taux d'engagement est a 0.8%, sous le benchmark industrie de 1.5%"
- Pas : "L'engagement pourrait etre ameliore"

### Specifique > generique
- Nommer les elements : page, URL, post, pub, headline.
- FAIL : "Certaines pages manquent d'optimisation"
- PASS : "La page /services n'a pas de meta description et le H1 repete le title"

---

## Self-check avant livraison

Pour chaque bloc de texte genere, verifier :

```
[ ] Aucun tiret cadratin (—)
[ ] Pas de cascade "Pas X. Pas Y. Mais Z."
[ ] Pas de 3+ fragments sans verbe
[ ] Pas de meta-commentaire ("nous allons", "voici")
[ ] Pas d'ouverture generique
[ ] Chaque affirmation est ancree dans des donnees
[ ] Pas de superlatifs sans preuve
[ ] Ton professionnel-decontracte, pas robotique
[ ] Pas de conclusion qui repete l'intro
[ ] Phrases actives, pas passives
```

Si 1+ FAIL : rewrite du passage concerne avant integration au rapport.

---

## Integration dans le workflow

- **Phase 4 (rewrites)** : appliquer le self-check sur chaque rewrite avant inclusion.
- **Phase 5 (rapport)** : scan complet du rapport avant livraison HTML.
- **Phase 6 (PDF)** : re-scan lors de la recreation PDF (le texte est regenre, pas copie).
- **Calendrier de contenu** : chaque hook passe le self-check.
- **Sequences email** : chaque email passe le self-check.
- **Lead magnets** : les titres et outlines passent le self-check.
