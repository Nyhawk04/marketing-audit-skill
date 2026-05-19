# Marketing Audit — Guide d'installation

Skill Claude Code qui genere un audit marketing complet (10-25 pages) pour n'importe quelle entreprise. Analyse site web, SEO, copywriting, publicites, reseaux sociaux, strategie de contenu, lead generation et business model. Produit un rapport HTML interactif puis un PDF professionnel.

---

## Prerequis

| Requis | Detail |
|--------|--------|
| Claude Code | Version Max ou API (le skill utilise des subagents en parallele) |
| Python 3.8+ | Pour les scripts de generation HTML et PDF |
| reportlab | `pip install reportlab` — necessaire uniquement pour la generation PDF |

---

## Installation

```bash
# 1. Copier le dossier du skill dans ton repertoire Claude Code
cp -r marketing-audit/ ~/.claude/skills/marketing-audit/

# 2. Installer la dependance Python pour le PDF
pip install reportlab

# 3. Verifier que tout est en place
ls ~/.claude/skills/marketing-audit/SKILL.md
```

C'est tout. Le skill est pret.

---

## Lancement rapide

Dans Claude Code, tape :

```
/marketing-audit "Nom de l'entreprise" https://www.site.com
```

Claude va te poser quelques questions (industrie, reseaux sociaux, offre principale) puis lancer l'audit automatiquement.

### Avec le dashboard

Ouvre le dashboard pour un intake visuel :

```bash
open ~/.claude/skills/marketing-audit/templates/dashboard.html
```

Remplis le formulaire, copie la commande generee, et colle-la dans Claude Code.

---

## Ce que le skill fait

| Phase | Description | Duree estimee |
|-------|-------------|---------------|
| 0 — Intake | Questions sur l'entreprise (nom, URL, reseaux, offre, audience) | 2 min |
| 1 — Collecte | Scraping du site, reseaux sociaux, Meta Ad Library, concurrents | 3-5 min |
| 2 — Analyse | Invocation des sous-skills (SEO, CRO, copywriting, ads, social, contenu, lead gen, brand) | 5-10 min |
| 3 — Scoring | Calcul des scores par categorie + score global pondere | <1 min |
| 4 — Rewrites | Generation des rewrites (headlines, CTAs, pubs, opt-in, posts sociaux) | 3-5 min |
| 5 — Rapport HTML | Assemblage du rapport complet, ouverture dans le navigateur | 1-2 min |
| 6 — Validation PDF | Apres ta validation : recreation complete en PDF A4 | 1-2 min |

**Temps total : 15-25 minutes** selon la quantite de donnees collectees.

---

## Cles et acces optionnels

| Cle / Acces | Requis ? | Ce que ca debloque |
|-------------|----------|-------------------|
| Claude Code Max ou API | **Requis** | Execution du skill |
| agent-browser | Recommande | Scraping de sites JS-heavy, screenshots, Instagram |
| Meta Business Manager (MCP) | Optionnel | Metriques live des pubs (CPA, ROAS, impressions) |
| Google API credentials | Optionnel | Core Web Vitals field, Google Search Console, Analytics |
| DataForSEO API | Optionnel | Backlinks, positions SERP, donnees concurrentielles |

### Sans acces optionnels

Le skill fonctionne sans aucun acces optionnel. Il utilise :
- `WebFetch` pour le scraping de base
- Meta Ad Library publique (pas besoin de compte)
- Benchmarks par industrie quand les donnees live ne sont pas disponibles

Le rapport indique clairement le niveau de confiance de chaque section (Complet / Partiel / Limite).

---

## Structure des fichiers

```
~/.claude/skills/marketing-audit/
├── SKILL.md                          # Orchestrateur principal (7 phases)
├── ONBOARDING.md                     # Ce fichier
├── references/
│   ├── scoring-system.md             # Algorithme de scoring et grades
│   ├── report-template.md            # Squelette du rapport (11 sections)
│   ├── degradation-matrix.md         # Fallbacks quand des donnees manquent
│   ├── social-media-checklist.md     # 45 checks sur 5 plateformes
│   ├── copywriting-checklist.md      # 20 checks USP/voix/headlines/CTAs
│   ├── business-model-checklist.md   # Questions strategiques par industrie
│   ├── benchmarks.md                 # Benchmarks cross-canal par industrie
│   ├── rewrite-templates.md          # Templates de rewrites (pubs, headlines, CTAs, opt-in)
│   ├── content-calendar-template.md  # Calendrier de contenu 4 semaines
│   └── lead-magnet-framework.md      # Framework de propositions de lead magnets
├── templates/
│   ├── dashboard.html                # Dashboard intake + resultats (dark-mode)
│   └── report.html                   # Template du rapport HTML
└── scripts/
    ├── generate_report_html.py       # JSON → rapport HTML
    └── generate_report_pdf.py        # JSON → rapport PDF A4
```

---

## Scoring

8 categories avec poids adaptatifs :

| Categorie | Poids |
|-----------|-------|
| Site & Conversion (CRO) | 20% |
| SEO | 15% |
| Copywriting & Messaging | 15% |
| Publicite payante | 15% |
| Reseaux sociaux | 10% |
| Strategie de contenu | 10% |
| Lead Generation | 10% |
| Business Model | 5% |

Si une categorie n'a pas de donnees (ex: pas de publicite), son poids est redistribue proportionnellement sur les autres.

**Grades** : A (90-100), B (75-89), C (60-74), D (40-59), F (<40)

---

## FAQ

### Le skill plante au scraping Instagram
Instagram bloque souvent les requetes automatisees. Solutions :
1. Installe `agent-browser` pour un scraping plus fiable
2. Fournis des screenshots de tes 12 derniers posts quand le skill le demande
3. Le skill continuera sans les donnees IG (score social ajuste)

### Le PDF ne se genere pas
Verifie que `reportlab` est installe : `pip install reportlab`. Si ca ne marche toujours pas, le rapport HTML est autonome et imprimable (Cmd+P dans le navigateur).

### Je n'ai pas de compte Meta Business Manager
Pas de probleme. Le skill utilise la Meta Ad Library publique. Tu auras un score pub plafonne a 70/100 (manque de metriques live), mais l'analyse creative et copy reste complete.

### Le rapport est trop long / trop court
Le skill cible 5000-8000 mots. La longueur depend du nombre de canaux actifs. Un business sans reseaux sociaux ni publicite aura un rapport plus court.

### Comment modifier le template du rapport ?
Edite `templates/report.html` pour le HTML ou `scripts/generate_report_pdf.py` pour le PDF. Les deux sont independants — modifier l'un ne casse pas l'autre.

---

## Communaute

- **Copy House** : [copyhouse.fr/communaute](https://www.copyhouse.fr/communaute)
- **Newsletter** : [copyhouse.fr/newsletter](https://www.copyhouse.fr/newsletter)

Partage tes audits et feedbacks dans la communaute pour aider a ameliorer le skill.
