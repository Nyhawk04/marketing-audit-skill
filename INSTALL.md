# Installation du skill marketing-audit

## Pour les membres Copy House (utilisateurs finaux)

### Prérequis

- macOS / Linux (Windows via WSL)
- Claude Code installé (https://docs.anthropic.com/claude/docs/claude-code)
- Git
- Node.js 18+ (pour la CLI Vercel utilisée en Phase 6)

### Installation initiale

```bash
# 1. Aller dans le dossier des skills Claude
mkdir -p ~/.claude/skills

# 2. Cloner le repo
cd ~/.claude/skills
git clone https://github.com/charlescopychief/marketing-audit-skill.git marketing-audit

# 3. Optionnel : installer Vercel CLI pour Phase 6
npm install -g vercel
```

Le skill apparaît automatiquement dans Claude Code à la prochaine session.

### Premier lancement

Dans un projet quelconque, tape :

```
/marketing-audit
```

Au premier run, le skill te demande de configurer **TA marque** et **TON offre** (palette, logo, CTA, URL). Ces infos sont sauvées dans `~/.claude/skills/marketing-audit/user-config/brand.json` et ne seront plus redemandées.

### Mettre à jour vers la dernière version

À faire régulièrement (le skill évolue) :

```bash
cd ~/.claude/skills/marketing-audit
git pull
```

Ta config personnelle (`user-config/brand.json`) est préservée — elle est gitignored.

### Reset config personnelle

Pour changer de DA / offre :

```bash
rm ~/.claude/skills/marketing-audit/user-config/brand.json
```

Le prochain run relancera l'onboarding config.

### Pré-créer la config sans onboarding interactif

```bash
cd ~/.claude/skills/marketing-audit/user-config
cp brand.example.json brand.json
code brand.json    # édite à la main
```

Voir `references/user-config-onboarding.md` pour le schéma complet.

### Multi-marques (agences, freelances)

Tu auditess plusieurs marques différentes ? Crée plusieurs profils :

```bash
mkdir ~/.claude/skills/marketing-audit/user-config/profiles
cd ~/.claude/skills/marketing-audit/user-config/profiles
cp ../brand.example.json client-acme.json
cp ../brand.example.json client-globex.json
# édite chaque fichier avec la DA/offre du client
```

Au lancement, le skill te demande quel profil utiliser pour cet audit.

## Pour contribuer (collaborateurs Copy House)

```bash
git clone git@github.com:charlescopychief/marketing-audit-skill.git
cd marketing-audit-skill
# faire des modifs
git add .
git commit -m "feat: ..."
git push
```

Les utilisateurs récupèrent les updates via `git pull`.

## Désinstaller

```bash
rm -rf ~/.claude/skills/marketing-audit
```

## Support

Questions / bugs : ouvre une issue sur https://github.com/charlescopychief/marketing-audit-skill/issues
