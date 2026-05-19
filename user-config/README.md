# user-config/

Configuration personnelle de chaque utilisateur du skill.

## Comment ça marche

Au premier lancement du skill, un onboarding interactif te pose des questions pour créer ton `brand.json`. Voir `references/user-config-onboarding.md` pour le workflow complet.

## Fichiers

- `brand.example.json` - Exemple (Copy House defaults). À utiliser comme template.
- `brand.json` - **TON** config personnelle (auto-créé au premier run, gitignored).

## Création manuelle (si tu veux skip l'onboarding)

```bash
cp brand.example.json brand.json
code brand.json   # édite avec tes valeurs
```

Puis lance le skill normalement.

## Reset

```bash
rm brand.json
```

Le prochain run relancera l'onboarding.

## Multi-marques (agences / freelances)

Créer plusieurs profils :

```
user-config/
├── brand.json              # actif
├── profiles/
│   ├── ma-marque.json
│   ├── client-A.json
│   └── client-B.json
```

Au lancement, le skill propose de choisir le profil actif. Choix copié en `brand.json`.

## Important

- `brand.json` est **gitignored**. Ta config reste locale.
- Pour pull une mise à jour du skill : `cd ~/.claude/skills/marketing-audit && git pull`. Ta config personnelle est préservée.
