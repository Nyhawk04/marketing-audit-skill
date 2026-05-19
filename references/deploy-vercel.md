# Phase 6 - Déploiement Vercel (remplace la génération PDF)

Le rapport HTML est hébergé sur Vercel pour partage URL. Pas de PDF. Avantages :
- URL partageable stable
- Mise à jour instantanée si itération
- Sommaire cliquable (sticky nav)
- Edge CDN mondial
- Gratuit

## Workflow

### 1. Préparer le dossier

```bash
cd <chemin>/audit-<slug>/
cp MARKETING-AUDIT-REPORT.html index.html
```

Vercel sert `index.html` par défaut. Le HTML est self-contained, pas de framework.

### 2. Premier déploiement

```bash
# Si vercel CLI pas installé
npm install -g vercel

# Déploiement (interactif au premier run pour login)
vercel --yes
```

Si premier login : ouvre le navigateur pour authentification GitHub/email.

### 3. Récupérer l'URL

Output type :
```
✅ Production: https://audit-<slug>-xyz.vercel.app
✅ Aliased: https://audit-<slug>.vercel.app
```

Partager l'**URL Aliased** (stable, courte).

### 4. Redéploiements (après itération)

```bash
cd <chemin>/audit-<slug>/
cp MARKETING-AUDIT-REPORT.html index.html
vercel --prod --yes
```

Même URL, contenu mis à jour en quelques secondes.

### 5. Vérification post-deploy

```bash
curl -s -o /dev/null -w "HTTP %{http_code} | %{size_download} bytes\n" https://<URL>/
```

Attendu : `HTTP 200 | ~170000 bytes`.

## Hooks Bash bloquants

Si l'agent rencontre `PreToolUse:Bash hook error` ou similaire (souvent un pre-commit hook qui bloque tous les appels Bash), il faut le neutraliser temporairement :

```bash
mv <projet>/.claude/hooks/pre-commit.sh <projet>/.claude/hooks/pre-commit.sh.bak
```

L'agent NE PEUT PAS faire ça seul (auto-bypass safety classifier bloque). Demander à l'utilisateur de le faire dans son terminal. Pour restaurer : `mv ...bak ...sh`.

## Custom domain (optionnel, post-livraison)

Si le client veut son propre domaine :
1. Dashboard Vercel → Project → Settings → Domains → Add
2. Ajouter par exemple `audit.entreprise.fr`
3. Configurer CNAME chez le registrar : `cname.vercel-dns.com`
4. Vercel auto-provisionne le SSL Let's Encrypt.

Pour Copy House interne : utiliser `audit.copyhouse.fr` ou variante.

## Auto-mode classifier

Le classifier de sécurité Claude Code peut bloquer `vercel --prod` si l'intention utilisateur n'est pas explicite. Conditions OK :
- Utilisateur a dit "deploy" / "push" / "mets sur la landing" / "publie"
- Utilisateur a validé visuellement le rapport ("c'est bon", "OK", "très bien" + contexte clair)

Si bloqué : montrer la commande à l'utilisateur pour qu'il l'exécute lui-même dans son terminal.

## Fichiers à NE PAS pousser sur Vercel

Le dossier `audit-<slug>/` contient :
- `MARKETING-AUDIT-REPORT.html` ✅ (devient index.html)
- `_research/*.md` ❌ (données brutes, peut contenir info sensible)
- `_analysis/*.md` ❌ (analyses internes)
- `MARKETING-ACTION-PLAN.md` ❌ (livrables internes)
- `MARKETING-SYNTHESE.md` ❌

Créer un `.vercelignore` :
```
_research/
_analysis/
*.md
!index.md   # si présent
```

Ou simplement : Vercel sert tout par défaut, mais comme `index.html` est servi à `/`, les .md ne sont pas exposés tant qu'on ne les linke pas. Pour vraiment cacher : `.vercelignore` ci-dessus.

## Commande tout-en-un (copier-coller pour l'utilisateur)

```bash
cd <chemin>/audit-<slug>/ && cp MARKETING-AUDIT-REPORT.html index.html && vercel --prod --yes
```
