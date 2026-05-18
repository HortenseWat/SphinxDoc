document.addEventListener("DOMContentLoaded", function() {
    
    // 1. On cherche l'élément qui contient le texte du titre en haut à gauche
    const sidebarTitle = document.querySelector(".sidebar-brand-text");
    
    // 2. Si on a trouvé ce titre sur la page...
    if (sidebarTitle) {
        
        // 3. On remonte jusqu'à la balise de lien <a> qui l'entoure, 
        // et on change sa destination ("href") pour pointer vers ton résumé.
        sidebarTitle.closest("a").setAttribute("href", "C:/Users/539682/SphinxDoc/docs/build/html/index.html");
    }
});
