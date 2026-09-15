# marketing-audit

Skill Claude Code pour générer un audit marketing complet, scoré, avec rewrites et plan d'action sur 90 jours. Rapport HTML éditorial hébergé sur Vercel.

Conçu par Copy House. Personnalisable pour ta propre marque et ton offre.

## Quick start

```bash
# Installation
cd ~/.claude/skills
git clone https://github.com/Nyhawk04/marketing-audit-skill.git marketing-audit

# Premier lancement dans Claude Code
/marketing-audit "Nom Entreprise" "https://exemple.com"
```

Au premier run, le skill te demande de configurer **ta DA** et **ton offre** (sauvé dans `user-config/brand.json`).

Voir [INSTALL.md](./INSTALL.md) pour les détails d'installation, mise à jour et configuration.

## Ce que le skill produit

À chaque audit, dans le dossier `audit-<slug>/` :

- **MARKETING-AUDIT-REPORT.html** - rapport éditorial HTML self-contained, 11 sections + section "Travailler ensemble"
- **MARKETING-SYNTHESE.md** - synthèse + angle radical
- **MARKETING-ACTION-PLAN.md** - 10 actions priorisées + roadmap 90 jours
- **MARKETING-QUICK-WINS.md** - 10 quick wins <15 min
- **MARKETING-REWRITES.md** - hero, hooks, lead magnets, calendrier 4 sem.
- **_research/** - données brutes collectées
- **_analysis/** - analyses par catégorie

Score global sur 100 avec grade A-F, pondéré sur 8 catégories.

## Workflow

7 phases :

1. **Intake** - questions sur l'entreprise (2 min)
2. **Collecte** - scraping site, socials, Meta Ad Library, concurrents (3-5 min)
3. **Analyse** - audit 8 catégories en parallèle (5-10 min)
4. **Scoring** - calcul score pondéré
5. **Rewrites** - réécritures des éléments les plus faibles
6. **Rapport HTML** - compilation éditoriale (style Copy House par défaut, ou ta DA)
7. **Deploy Vercel** - URL partageable stable

Total : ~20 minutes. Mode `--lite` : ~10 min (4 catégories).

## Personnalisation

Au premier lancement, onboarding interactif. Tu peux aussi pré-créer `user-config/brand.json` depuis `brand.example.json` :

- Palette de couleurs (10 tokens)
- Logo (chemin SVG/PNG)
- Typographie (font stack)
- Offre commerciale (section "Travailler ensemble" en fin de rapport)
- URL CTA, texte bouton, cible

Voir [`references/user-config-onboarding.md`](./references/user-config-onboarding.md) pour le schéma complet.

## Mise à jour

```bash
cd ~/.claude/skills/marketing-audit
git pull
```

Ta config personnelle est préservée (gitignored).

## Stack technique

- Skill Claude Code (markdown + scripts Python)
- Génération HTML self-contained (CSS inline, SVG inline, vanilla JS)
- Animations : IntersectionObserver vanilla, transitions CSS
- Hébergement : Vercel (CLI)
- Anti-AI tells scan obligatoire avant livraison

## Licence

À définir.

## Auteur

Copy House - https://copyhouse.fr
