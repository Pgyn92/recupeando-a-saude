# Recuperando a Saúde — redesign editorial

Branch de trabalho: `redesign-editorial`

## Objetivo

Transformar o site de uma landing page orientada a conversão numa experiência editorial de saúde e ciência, mantendo produtos e materiais existentes acessíveis, mas separados da narrativa científica.

## Nova estrutura

- `index.html` — nova homepage editorial
- `assets/css/site.css` — design system global
- `assets/js/site.js` — menu móvel, animações leves e filtros
- `entender/racio-omega-6-3.html` — introdução ao tema
- `ciencia/` — hub e páginas por área da saúde
- `testar-e-acompanhar.html` — processo de medição e acompanhamento
- `biblioteca.html` — biblioteca filtrável de materiais existentes
- `metodologia.html` — política editorial
- `sobre.html` — projeto e transparência
- `produtos/index.html` — área comercial separada
- `en/index.html` — homepage inglesa no novo padrão

## Decisões visuais

- Paleta principal: navy, teal, off-white e uma cor de alerta usada com parcimónia.
- Tipografia: Source Serif 4 em títulos e Source Sans 3 em interface/corpo.
- Mais espaço em branco e menos sombras/gradientes.
- Sem CTA flutuante de compra na experiência editorial.
- Sem emojis como principal sistema de iconografia.
- Hero visual construído em CSS, portanto não depende de imagem externa.
- Navegação responsiva e foco em acessibilidade.

## Materiais antigos

Os HTMLs antigos de apresentações e produtos foram mantidos sem exclusão para preservar todo o conteúdo. As novas páginas temáticas funcionam como camada editorial antes desses documentos.

## Assets ainda não enviados

Quando disponíveis, guardar preferencialmente em:

- `assets/images/` — fotografias e ilustrações editoriais
- `assets/video/` — vídeos
- `assets/images/social/` — imagens Open Graph 1200x630

### Sugestões de assets prioritários

1. Imagem/ilustração institucional para o hero (opcional; o hero atual funciona sem ela).
2. Thumbnail do vídeo principal em 16:9.
3. Imagens editoriais para cardiovascular, cérebro, pele, desempenho e inflamação.
4. Fotografias dos produtos apenas dentro da área comercial.
5. Imagem Open Graph PT e EN.

## Próxima migração técnica recomendada

As apresentações legadas ainda têm estilos embutidos próprios. Depois da aprovação visual da nova camada editorial, migrar gradualmente esses documentos para componentes do novo design system, preservando referências e conteúdo científico.
