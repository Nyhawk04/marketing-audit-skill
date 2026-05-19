# Section "Travailler ensemble" - OBLIGATOIRE en fin de rapport

Cette section conclut TOUS les rapports d'audit marketing Copy House. Pitch du service AI-CMO + CTA vers ai-cmo.fr.

## Pitch AI-CMO (texte canonique)

**Tagline** : "Un bras droit marketing augmenté par IA."

**Pitch en 1 phrase** : Un seul profil hautement qualifié, dédié à votre entreprise, qui gère la stratégie, la production et l'automatisation marketing.

**Ce qu'il prend en charge** :
- Stratégie et positionnement
- Production de contenu et copy
- SEO, ads, lifecycle
- Site, landing pages, funnels
- Automatisation et workflows IA

**Ce qu'il remplace (5 agences en 1 profil)** :
- Agence marketing
- Agence SEO
- Agence publicité
- Agence site internet
- Agence automatisation IA

**Cible (pour qui)** : TPE et PME entre 500 k€ et 30 M€ de CA annuel.

**CTA final** : Bouton bronze "Découvrir l'AI-CMO →" pointant vers `https://ai-cmo.fr` (target blank). Sous-texte : "ai-cmo.fr · service Copy House".

**Friction qualification** : Préciser "Découvrir l'offre, remplir le questionnaire de qualification et bloquer un créneau." (pas "réserver un appel" direct - filtre par questionnaire d'abord).

## Structure HTML (à inclure tel quel, adapter headline au contexte audit)

```html
<section id="work" class="work-section">
  <div class="work-tag">Travailler ensemble</div>
  <h2 class="work-title">Vous voulez faire passer [ENTREPRISE] <br/>au niveau supérieur ?</h2>
  <p class="work-lede">
    Cet audit liste [X] actions prioritaires et 90 jours de roadmap. Reste à les exécuter.
    Copy House place un <strong>AI-CMO</strong> dans votre équipe pour porter le marketing
    de bout en bout, sans empiler les agences.
  </p>

  <div class="work-grid">
    <div class="work-card">
      <h3>L'AI-CMO en 1 phrase</h3>
      <p>
        Un bras droit marketing augmenté par IA. Un seul profil hautement
        qualifié, dédié à votre entreprise, qui gère la stratégie,
        la production et l'automatisation.
      </p>
    </div>
    <div class="work-card">
      <h3>Ce qu'il prend en charge</h3>
      <ul class="work-list">
        <li>Stratégie et positionnement</li>
        <li>Production de contenu et copy</li>
        <li>SEO, ads, lifecycle</li>
        <li>Site, landing pages, funnels</li>
        <li>Automatisation et workflows IA</li>
      </ul>
    </div>
    <div class="work-card">
      <h3>Ce qu'il remplace</h3>
      <ul class="work-list">
        <li>Agence marketing</li>
        <li>Agence SEO</li>
        <li>Agence publicité</li>
        <li>Agence site internet</li>
        <li>Agence automatisation IA</li>
      </ul>
    </div>
  </div>

  <div class="work-target">
    <span class="work-target-label">Pour qui</span>
    <span class="work-target-value">TPE et PME entre 500 k€ et 30 M€ de CA annuel</span>
  </div>

  <div class="work-cta-block">
    <p class="work-cta-text">
      Découvrir l'offre, remplir le questionnaire de qualification et bloquer un créneau.
    </p>
    <a href="https://ai-cmo.fr" target="_blank" rel="noopener noreferrer" class="work-cta">
      Découvrir l'AI-CMO
      <span class="work-cta-arrow">&rarr;</span>
    </a>
    <p class="work-cta-sub">ai-cmo.fr · service Copy House</p>
  </div>
</section>
```

## CSS (extrait, voir template référence pour version complète)

```css
.work-section {
  background: #212121;
  color: #F9F9F2;
  margin: 80px -32px 0;
  padding: 88px 32px 96px;
  border-radius: 24px;
  border-bottom: none;
}
.work-section h2, .work-section h3 { color: #F9F9F2; }
.work-tag {
  display: inline-block;
  font-size: 11px; letter-spacing: 0.22em; text-transform: uppercase;
  color: #B07C5E; font-weight: 700;
  padding: 6px 12px;
  border: 1px solid rgba(176, 124, 94, 0.4);
  border-radius: 999px;
  margin-bottom: 24px;
}
.work-title {
  font-size: clamp(32px, 5vw, 52px);
  line-height: 1.1;
  letter-spacing: -0.02em;
  margin: 0 0 24px;
  font-weight: 700;
}
.work-lede {
  font-size: 18px; line-height: 1.6;
  color: #D7D7CF;
  max-width: 720px;
  margin: 0 0 56px;
}
.work-lede strong { color: #B07C5E; font-weight: 700; }
.work-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  margin-bottom: 48px;
}
.work-card {
  background: #2A2A2A;
  border: 1px solid #3A3A3A;
  border-radius: 16px;
  padding: 28px 24px;
}
.work-card h3 {
  font-size: 15px; letter-spacing: 0.04em; text-transform: uppercase;
  color: #B07C5E; margin: 0 0 14px; font-weight: 700;
}
.work-list { list-style: none; margin: 0; padding: 0; }
.work-list li {
  padding: 8px 0;
  border-bottom: 1px solid #3A3A3A;
  color: #E5E5DC;
}
.work-list li::before { content: "•"; color: #B07C5E; margin-right: 10px; font-weight: 700; }
.work-list li:last-child { border-bottom: none; }
.work-target {
  display: flex; align-items: center; gap: 16px;
  padding: 20px 24px;
  background: rgba(176, 124, 94, 0.08);
  border-left: 3px solid #B07C5E;
  border-radius: 8px;
  margin-bottom: 56px;
}
.work-target-label {
  font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
  color: #B07C5E; font-weight: 700;
}
.work-target-value { font-size: 17px; font-weight: 500; color: #F9F9F2; }
.work-cta-block { text-align: center; padding: 32px 0 8px; }
.work-cta-text { font-size: 16px; color: #D7D7CF; margin: 0 0 24px; }
.work-cta {
  display: inline-flex; align-items: center; gap: 12px;
  background: #B07C5E; color: #F9F9F2;
  padding: 18px 36px; border-radius: 999px;
  font-size: 17px; font-weight: 700;
  box-shadow: 0 6px 24px rgba(176, 124, 94, 0.25);
  transition: transform .15s ease, background .15s ease, box-shadow .15s ease;
}
.work-cta:hover {
  background: #C08C6E;
  transform: translateY(-1px);
  box-shadow: 0 10px 32px rgba(176, 124, 94, 0.35);
}
.work-cta-sub { margin: 16px 0 0; font-size: 13px; color: #B5B5AC; letter-spacing: 0.04em; }

@media (max-width: 880px) {
  .work-grid { grid-template-columns: 1fr; }
  .work-section { margin: 48px -20px 0; padding: 56px 24px 72px; border-radius: 16px; }
  .work-target { flex-direction: column; align-items: flex-start; gap: 8px; }
}
```

## CTA dans la nav

Le bouton "Travailler ensemble" dans le top nav doit pointer vers `#work` (anchor cette section). Toujours en dernier item de la nav, après tous les chapitres numérotés.

## Adaptation par audit

**Headline** : adapter au business audité (ex. "Vous voulez faire passer [NOM] au niveau supérieur ?")
**Lede** : intégrer le nombre d'actions du plan d'action + référence à la roadmap 90 jours

Tout le reste (3 cards AI-CMO, target, CTA) est INCHANGÉ.
