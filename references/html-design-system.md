# HTML Design System - Audit Marketing Copy House

**Reference complète** pour générer le rapport HTML Phase 5. Reproduire CES patterns sur chaque nouvel audit.

Template gold standard : `templates/report-reference-v4.html` (rapport SKL CLUB validé). Le lire AVANT de générer un nouveau rapport. Reproduire sa structure et son style avec les nouvelles données de l'audit en cours.

## 1. Palette DA Copy House (obligatoire, jamais déroger)

```css
/* Background principal - blanc cassé chaud */
--bg-page: #F9F9F2;

/* Texte primaire + cards sombres + éléments forts (JAMAIS #000) */
--text-primary: #212121;

/* Accent bronze Cupra Cobre - mises en avant, scores forts, CTAs */
--accent-bronze: #B07C5E;
--accent-bronze-dark: #8E5F44;   /* hover */
--accent-bronze-light: rgba(176, 124, 94, 0.08);  /* hover bg */

/* Blanc pur - cards alternatives, contrastes */
--white: #FFFFFF;

/* États (cohérents avec bronze, pas criards) */
--success: #5C8B5C;   /* vert sage, score 75+ */
--warning: #D8945A;   /* orange, score 40-60 */
--danger:  #C04A3A;   /* terra-cotta, score <40 */

/* Bordures */
--border-light: #E5E5DC;   /* sur fond clair */
--border-dark:  #3A3A3A;   /* sur cards 212121 */

/* Texte secondaire / muted */
--text-muted: #6B6B63;
--text-on-dark-secondary: #D7D7CF;
--num-muted: #B5B5AC;
```

INTERDITS : `#000` noir pur, gradients violets, gris uniforme, palettes "AI-typiques".

## 2. Typographie

```css
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "Inter", "Segoe UI", Roboto, sans-serif;
font-feature-settings: 'ss01', 'cv02', 'cv03', 'cv04', 'cv11';  /* style Inter natif */

/* Body */
body { font-size: 16px; line-height: 1.65; color: var(--text-primary); }

/* Hierarchy */
h1 { font-size: clamp(40px, 6vw, 64px); font-weight: 700; letter-spacing: -0.025em; }
h2 { font-size: clamp(28px, 3.5vw, 40px); font-weight: 700; letter-spacing: -0.02em; }
h3 { font-size: 20px; font-weight: 700; }

/* Chiffres - tabular nums obligatoire */
.score-number, .gauge-text, td.number { font-variant-numeric: tabular-nums; }
```

PAS de Graveur ni autre font custom embed. Inter system stack suffit (validé par utilisateur).

## 3. Layout

```css
.shell { max-width: 1280px; margin: 0 auto; padding: 0 32px; }
main { max-width: 1100px; margin: 0 auto; padding: 0 0 120px; }

section {
  padding: 80px 0;
  border-bottom: 1px solid var(--border-light);
}
section:first-of-type { padding-top: 48px; }
section:last-of-type { border-bottom: none; }
```

Spacing rhythm : 4 / 8 / 16 / 24 / 32 / 48 / 64 / 96 px.

## 4. Header sticky (CSS Grid 2 lignes - PATTERN OBLIGATOIRE)

```css
.topnav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(249, 249, 242, 0.88);
  backdrop-filter: saturate(180%) blur(14px);
  border-bottom: 1px solid rgba(229, 229, 220, 0.6);
  box-shadow: 0 1px 0 rgba(33, 33, 33, 0.04);
}
.topnav-inner {
  max-width: 1280px; margin: 0 auto;
  padding: 10px 32px 12px;
  display: grid;
  grid-template-columns: auto 1fr auto;
  grid-template-rows: auto auto;
  align-items: center;
  column-gap: 24px;
  row-gap: 6px;
}
.brand-block { grid-column: 1; grid-row: 1; display: flex; align-items: center; gap: 10px; }
.topnav-cta-wrap { grid-column: 3; grid-row: 1; justify-self: end; }
.topnav-links {
  grid-column: 1 / -1; grid-row: 2;
  display: flex; flex-wrap: wrap; gap: 2px 4px;
  padding-top: 4px; border-top: 1px solid rgba(229, 229, 220, 0.5);
}

/* Mobile <600px : nav scrollable horizontale */
@media (max-width: 600px) {
  .topnav-links { flex-wrap: nowrap; overflow-x: auto; }
}
```

Structure HTML :
```html
<header class="topnav">
  <div class="topnav-inner">
    <div class="brand-block">
      <svg class="ch-logo">[Logo Copy House inline - voir templates/copyhouse-logo.svg]</svg>
      <span class="brand-meta">Audit Marketing</span>
    </div>
    <nav class="topnav-links" id="topnav-links">
      <a href="#cover" data-target="cover"><span class="num">01</span><span class="sep">/</span>Couverture</a>
      <a href="#executive" data-target="executive"><span class="num">02</span><span class="sep">/</span>Résumé</a>
      <!-- ... 11 sections numérotées ... -->
    </nav>
    <div class="topnav-cta-wrap">
      <a href="#work" class="cta-nav">Travailler ensemble</a>
    </div>
    <div class="scroll-progress" id="scroll-progress" aria-hidden="true"></div>
  </div>
</header>
```

Numéros nav 01-11 en gris (#B5B5AC), séparateur "/" gris, texte 12.5px. CTA "Travailler ensemble" toujours en dernier, fond bronze, pilule.

## 5. Logo Copy House

Embed inline le SVG depuis `templates/copyhouse-logo.svg` (Logo_05, wordmark CH + Copy House). Hauteur 30px dans le header. `fill="#212121"` natif, à conserver.

## 6. Scroll progress bar (2px sous header)

```css
.scroll-progress {
  position: absolute; left: 0; bottom: -1px;
  height: 2px; width: 0%;
  background: linear-gradient(90deg, #B07C5E 0%, #D8945A 100%);
  transition: width 0.08s ease-out;
  pointer-events: none;
}
```

JS minimal :
```js
var progress = document.getElementById('scroll-progress');
window.addEventListener('scroll', function() {
  var max = document.documentElement.scrollHeight - window.innerHeight;
  var pct = max > 0 ? (window.scrollY / max) * 100 : 0;
  progress.style.width = pct + '%';
}, { passive: true });
```

## 7. Scroll-spy (lien actif dans nav)

```css
.topnav-links a.is-active {
  color: #B07C5E;
  background: rgba(176, 124, 94, 0.12);
}
.topnav-links a.is-active .num,
.topnav-links a.is-active .sep { color: #B07C5E; }
```

JS via IntersectionObserver vanilla. Voir `templates/report-reference-v4.html` ligne ~4470+.

## 8. Animations - Fade-in au scroll (IntersectionObserver)

```css
.reveal {
  opacity: 0;
  transform: translateY(16px);
  transition: opacity 0.55s ease-out, transform 0.55s ease-out;
}
.reveal.is-visible { opacity: 1; transform: translateY(0); }

@media (prefers-reduced-motion: reduce) {
  .reveal { opacity: 1; transform: none; transition: none; }
}
```

Appliquer la classe `.reveal` aux sections, score-hero, radar, highlights.

## 9. Jauges circulaires SVG animées

Pattern dans `templates/report-reference-v4.html`. Couleur dynamique :
- score >= 75 : `--success` #5C8B5C
- score 60-74 : `--accent-bronze` #B07C5E
- score 40-59 : `--warning` #D8945A
- score < 40 : `--danger` #C04A3A

Animation stroke-dashoffset au scroll-in via IntersectionObserver, 800-1000ms ease-out.

## 10. Barres de scoring horizontales animées

Dans le résumé exécutif, ajouter UNE PAR CATÉGORIE avec animation :
```css
.score-bar-track {
  height: 8px; background: var(--border-light); border-radius: 999px;
  overflow: hidden;
}
.score-bar-fill {
  height: 100%; width: 0; border-radius: 999px;
  transition: width 900ms cubic-bezier(0.22, 1, 0.36, 1);
}
.score-bar-fill.is-animated { width: var(--target-width); }
```

Largeur cible déclenchée par IntersectionObserver quand visible.

## 11. Cards et ombres

```css
.card {
  background: #FFFFFF;
  border-radius: 16px;
  padding: 24px;
  border-left: 4px solid transparent;
  box-shadow: 0 1px 2px rgba(33,33,33,0.04), 0 8px 24px -8px rgba(33,33,33,0.08);
  transition: transform 0.18s ease, box-shadow 0.18s ease;
}
.card:hover {
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(33,33,33,0.06), 0 16px 32px -8px rgba(33,33,33,0.12);
}
.card-accent  { border-left-color: #B07C5E; }
.card-success { border-left-color: #5C8B5C; }
.card-warn    { border-left-color: #D8945A; }
.card-danger  { border-left-color: #C04A3A; }
```

## 12. Tables

Alternance lignes #FFFFFF / #FAFAF4. Header bronze uppercase tracking 0.04em.

## 13. Cards terminal (pour rewrites)

Cards #212121 fond, texte #F9F9F2. Triple-dot macOS rouge/amber/vert en haut gauche. Pour rewrites de hooks/CTAs/emails/headlines.

## 14. Liens

```css
a { color: #B07C5E; text-decoration: none; }
a:hover { color: #8E5F44; }

/* Liens dans paragraphes : underline animé */
p a {
  background-image: linear-gradient(currentColor, currentColor);
  background-size: 0% 1.5px;
  background-position: 0 100%;
  background-repeat: no-repeat;
  transition: background-size 0.25s ease-out;
}
p a:hover { background-size: 100% 1.5px; }
```

Liens externes : `target="_blank" rel="noopener noreferrer"`.

## 15. Anti-AI tells (vérification obligatoire)

Avant de sauvegarder le HTML, scanner et corriger :
- **0 em-dash (—)** : remplacer par "-" ou reformuler
- **0 en-dash (–)** : idem
- **0 emoji** : aucun emoji nulle part (pas même dans nav, bullets, headers)
- **0 cascade "Pas X. Pas Y. Mais Z."** : reformuler en affirmation directe
- **0 fragment-noms sans verbe en chaîne** ("Court. Net. Direct.") : phrase complète
- **0 méta-commentaire vide** ("Le résultat est indéniable")
- **0 opener AI-typique** ("Dans un monde où...", "Voici la vérité sur...", "Spoiler...")

## 16. Print stylesheet

```css
@media print {
  .topnav, .scroll-progress, .reveal { display: none !important; }
  .reveal { opacity: 1 !important; transform: none !important; }
  section { page-break-inside: avoid; }
}
```

## 17. Self-contained

- Tout inline (CSS dans `<style>`, SVG inline, base64 si nécessaire)
- AUCUN CDN, AUCUN Google Fonts via link, AUCUNE lib externe
- 1 seul `<script>` vanilla en fin de body (scroll progress + scroll-spy + IO fade-in + gauge anim + score bars)
- Taille cible : 150-200KB

## 18. Footer

```html
<footer class="page-footer">
  <strong>Copy House · Audit Marketing</strong>
  Rapport généré le [DATE] · [ENTREPRISE]
  <br/>
  <span class="sub">Rapport HTML hosté · Copy House</span>
  <div class="footer-links">
    <a href="#top" class="back-top">↑ Retour en haut</a>
    <a href="https://copyhouse.fr" target="_blank" rel="noopener">copyhouse.fr</a>
    <a href="https://ai-cmo.fr" target="_blank" rel="noopener">ai-cmo.fr</a>
  </div>
</footer>
```

## 19. Workflow Phase 5

1. **Lire** `templates/report-reference-v4.html` intégralement avant de générer.
2. **Reproduire** sa structure (cover, exec summary avec radar SVG, 9 sections catégories scoring, work-together, footer).
3. **Remplacer** uniquement le contenu (noms, scores, textes) avec les données de l'audit en cours.
4. **Inclure obligatoirement** la section "Travailler ensemble" (voir `references/work-together-section.md`).
5. **Scanner anti-AI tells** avant sauvegarde.
6. **Ouvrir** dans le navigateur via `open <chemin>`.
7. **Présenter** à l'utilisateur pour validation.
