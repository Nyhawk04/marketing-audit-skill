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

### Installer les neuf commandes que l'audit appelle

**Cette étape n'est pas optionnelle.** `marketing-audit` est un chef d'orchestre : il ne
note rien lui-même, il invoque neuf commandes spécialisées et agrège leurs scores. Ces
commandes ne sont PAS dans ce dépôt, elles viennent de deux dépôts publics.

Sans elles, l'audit tourne quand même, sauf qu'il n'a aucune grille de critères pour le
CRO, la pub ou les réseaux sociaux : il invente les siennes à chaque passage, et deux
audits du même site ne donnent pas le même score.

```bash
npx skills@latest add coreyhaines31/marketingskills -g -a claude-code -y \
  -s cro,copywriting,social,content-strategy,lead-magnets,marketing-psychology,competitor-profiling,seo-audit

npx skills@latest add AgriciDaniel/claude-ads -g -a claude-code -y -s ads-meta
```

Vérifie qu'elles sont toutes là avant de lancer ton premier audit :

```bash
for s in cro copywriting social content-strategy lead-magnets \
         marketing-psychology competitor-profiling seo-audit ads-meta; do
  if [ -f ~/.claude/skills/$s/SKILL.md ] || [ -f ~/.agents/skills/$s/SKILL.md ]
    then echo "ok      $s"; else echo "MANQUE  $s"; fi
done
```

Neuf lignes `ok`, et tu peux lancer ton audit. Une ligne `MANQUE`, et c'est cette
catégorie-là que le rapport inventera : relance la commande d'installation avec ce seul
nom derrière `-s`.

⚠️ **Le contrôle porte sur DEUX dossiers, et ce n'est pas un excès de prudence.** Le
résumé affiché par `npx skills` annonce `~/.agents/skills/<nom>`, alors qu'avec
`-a claude-code` il dépose dans `~/.claude/skills/<nom>`. Mesuré le 15/09/2026 : une
vérification qui ne regardait que `~/.agents/skills/` a conclu « rien n'a été installé »
juste après un « Installation complete » parfaitement exact.

⚠️ **Les noms de ces commandes bougent.** `coreyhaines31/marketingskills` a renommé
`page-cro` en `cro` et `social-content` en `social` depuis avril 2026. Si un audit te dit
qu'il ne trouve pas une commande, compare la liste ci-dessus avec
`npx skills@latest add coreyhaines31/marketingskills -l`, qui affiche les noms du jour
sans rien installer.

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
