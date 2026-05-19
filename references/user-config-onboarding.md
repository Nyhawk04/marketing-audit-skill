# Onboarding personnalisé - Configuration utilisateur

Le skill `marketing-audit` est distribué avec la DA Copy House et le service AI-CMO en exemple. Au PREMIER usage, chaque utilisateur du skill doit créer SA propre config pour personnaliser :
- Sa direction artistique (couleurs, logo, font)
- Son offre commerciale (CTA fin de rapport, lien externe, pitch)
- Son URL de déploiement Vercel

## Fichier de config

Chemin : `~/.claude/skills/marketing-audit/user-config/brand.json`

Ce fichier est **gitignored** (chaque user a le sien, jamais committed dans le repo public).

## Structure du fichier (schema)

```json
{
  "brand": {
    "name": "Copy House",
    "tagline": "Audit Marketing",
    "logo_path": "../templates/copyhouse-logo.svg",
    "website": "https://copyhouse.fr",
    "report_footer_signature": "Copy House · Audit Marketing"
  },
  "palette": {
    "bg_page":         "#F9F9F2",
    "text_primary":    "#212121",
    "accent":          "#B07C5E",
    "accent_dark":     "#8E5F44",
    "white":           "#FFFFFF",
    "success":         "#5C8B5C",
    "warning":         "#D8945A",
    "danger":          "#C04A3A",
    "border_light":    "#E5E5DC",
    "border_dark":     "#3A3A3A",
    "text_muted":      "#6B6B63"
  },
  "typography": {
    "stack": "-apple-system, BlinkMacSystemFont, \"SF Pro Text\", \"Inter\", \"Segoe UI\", Roboto, sans-serif",
    "feature_settings": "'ss01', 'cv02', 'cv03', 'cv04', 'cv11'",
    "custom_font": null
  },
  "offer": {
    "section_tag":     "Travailler ensemble",
    "section_title":   "Vous voulez faire passer {ENTREPRISE} au niveau supérieur ?",
    "service_name":    "AI-CMO",
    "tagline":         "Un bras droit marketing augmenté par IA.",
    "one_liner":       "Un seul profil hautement qualifié, dédié à votre entreprise, qui gère la stratégie, la production et l'automatisation.",
    "handles": [
      "Stratégie et positionnement",
      "Production de contenu et copy",
      "SEO, ads, lifecycle",
      "Site, landing pages, funnels",
      "Automatisation et workflows IA"
    ],
    "replaces": [
      "Agence marketing",
      "Agence SEO",
      "Agence publicité",
      "Agence site internet",
      "Agence automatisation IA"
    ],
    "target_label":    "Pour qui",
    "target_value":    "TPE et PME entre 500 k€ et 30 M€ de CA annuel",
    "cta_text":        "Découvrir l'offre, remplir le questionnaire de qualification et bloquer un créneau.",
    "cta_button":      "Découvrir l'AI-CMO",
    "cta_url":         "https://ai-cmo.fr",
    "cta_sub":         "ai-cmo.fr · service Copy House"
  },
  "deploy": {
    "platform": "vercel",
    "team_slug": "copy-house",
    "url_pattern": "https://audit-{slug}.vercel.app"
  }
}
```

## Workflow first-run (à exécuter dans Phase 0)

Au tout début de l'exécution du skill, AVANT de lancer Phase 0 (Intake) :

### 1. Détecter premier usage

```python
# Pseudo-code
config_path = os.path.expanduser("~/.claude/skills/marketing-audit/user-config/brand.json")
if not os.path.exists(config_path):
    run_onboarding()
```

Si `brand.json` existe : charger les valeurs et continuer normalement.

### 2. Onboarding interactif (premier usage uniquement)

Afficher message :
```
Premier lancement du skill marketing-audit.

Avant ton premier audit, je dois savoir 3 choses :
1. Ta marque (nom, couleurs, logo)
2. Ton offre commerciale (le CTA en fin de rapport)
3. Tes options de déploiement

Tout ça sera sauvegardé dans user-config/brand.json et ne changera plus
(éditable manuellement ensuite).

C'est parti ?
```

Puis batches de questions via AskUserQuestion :

**Batch 1 - Marque**
- Nom de ta marque ?
- Site web principal ?
- Tagline rapport (ex. "Audit Marketing", "Diagnostic Croissance") ?
- Chemin local du logo SVG ou PNG ? (option : utiliser le logo par défaut Copy House)

**Batch 2 - Palette (présenter options par défaut)**
- Tu veux : (a) garder la palette Copy House (bronze/cream) (b) palette dark mode classique (c) palette personnalisée (j'extrais d'une image de marque) (d) je te demande chaque couleur une par une

**Batch 3 - Offre commerciale (CTA fin de rapport)**
- Nom de ton service / produit principal ?
- Tagline en 1 phrase ?
- Liste 3-5 livrables / capacités du service ?
- Liste 3-5 choses que tu remplaces / surclasses ?
- Cible idéale (taille entreprise, CA) ?
- URL de destination du CTA (ex. https://ton-service.com) ?
- Texte du bouton CTA (ex. "Réserver un appel", "Découvrir l'offre") ?

**Batch 4 - Déploiement**
- Tu veux qu'on déploie automatiquement chaque audit sur Vercel ?
- Si oui : team Vercel slug ?

### 3. Sauvegarder

Écrire `~/.claude/skills/marketing-audit/user-config/brand.json` avec les réponses.

Confirmation :
```
Config sauvée dans user-config/brand.json.

Pour modifier plus tard, édite ce fichier directement.

On démarre ton audit pour [entreprise] maintenant.
```

## Utilisation des valeurs dans le rapport

### Phase 5 (rapport HTML)

Au lieu de hardcoder `#F9F9F2`, `#B07C5E`, etc., lire `brand.json` et injecter les valeurs dans les CSS variables / styles inline du template.

Exemple :
```html
<style>
:root {
  --bg-page:     {{palette.bg_page}};
  --text:        {{palette.text_primary}};
  --accent:      {{palette.accent}};
  /* etc. */
}
</style>
```

Logo : lire `brand.logo_path`, l'embed inline (lire le fichier SVG ou base64 si PNG).

### Phase 6 (section work-together)

Au lieu d'utiliser le pitch AI-CMO hardcodé, remplir la section depuis `offer.*` :
- `offer.section_title` → remplacer `{ENTREPRISE}` par le nom audité
- `offer.service_name` en gros wordmark
- `offer.handles` → 3 cards "ce qu'il fait"
- `offer.replaces` → 3 cards "ce qu'il remplace"
- `offer.target_value` → bandeau cible
- `offer.cta_*` → bouton final + sous-texte

### Phase 6 (déploiement Vercel)

`deploy.team_slug` injecté dans la commande `vercel --scope <slug>` si présent.

## Reset config

Pour reset la config (changer de DA / offre) :
```bash
rm ~/.claude/skills/marketing-audit/user-config/brand.json
```

Le prochain run relancera l'onboarding.

## Édition manuelle

Pour ajuster un champ sans repasser l'onboarding :
```bash
code ~/.claude/skills/marketing-audit/user-config/brand.json
```

## Multi-clients (avancé)

Si un utilisateur audite plusieurs marques différentes (agences, freelances) :

Créer plusieurs profils :
```
user-config/
├── brand.json              # actif par défaut
├── profiles/
│   ├── copy-house.json
│   ├── client-acme.json
│   └── client-globex.json
```

Au lancement, si `profiles/` contient plusieurs fichiers : demander quel profil utiliser pour cet audit, copier le profil choisi en `brand.json` actif.
