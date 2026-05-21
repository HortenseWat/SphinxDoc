document.addEventListener("DOMContentLoaded", function() {
    const sidebarTitle = document.querySelector(".sidebar-brand-text");
    
    if (sidebarTitle) {
        // On change le curseur pour montrer que c'est cliquable
        sidebarTitle.style.cursor = "pointer"; 
        
        sidebarTitle.addEventListener("click", function(event) {
            
            event.preventDefault();


            // Cette ligne renvoie TOUJOURS à la page d'accueil du site, peu importe l'URL
            window.location.href = window.location.origin + window.location.pathname.split('/').slice(0, 2).join('/') + '/';
        });
    }
});
