
// Wait for DOM
document.addEventListener("DOMContentLoaded", function() {
    console.log("Main JS Loaded");

    // Hamburger Menu Logic
    var nav = document.querySelector('.main-nav');
    if(nav && !document.querySelector('.menu-toggle')) {
        var toggle = document.createElement('div');
        toggle.className = 'menu-toggle';
        toggle.innerHTML = '<span></span><span></span><span></span>';
        var links = document.querySelector('.nav-links');
        
        toggle.onclick = function() {
            if(links) links.classList.toggle('active');
        };
        if(links) nav.insertBefore(toggle, links);
    }

    // Filter Logic (for explore.html)
    const filterContainer = document.getElementById("filterBtnContainer");
    if (filterContainer) {
        function applyFilter(category, activeBtn) {
            let items = document.querySelectorAll(".grid-item");
            items.forEach(item => {
                if (category === "all" || item.classList.contains(category)) {
                    item.style.display = "block";
                } else {
                    item.style.display = "none";
                }
            });

            let btns = document.querySelectorAll(".filter-chip");
            btns.forEach(b => b.classList.remove("active"));
            if (activeBtn) {
                activeBtn.classList.add("active");
            }
        }

        let buttons = document.querySelectorAll(".filter-chip");
        buttons.forEach(btn => {
            btn.addEventListener("click", function(e) {
                let cat = this.getAttribute("data-filter");
                if(cat) applyFilter(cat, this);
            });
        });

        let hash = window.location.hash;
        let validHash = false;
        if (hash) {
            let filterMap = {
                '#filter-sinai': 'item-sinai',
                '#filter-desert': 'item-desert',
                '#filter-nile': 'item-nile'
            };
            if (filterMap[hash]) {
                let catClass = filterMap[hash];
                let targetBtn = document.querySelector(`.filter-chip[data-filter="${catClass}"]`);
                if(targetBtn) {
                    applyFilter(catClass, targetBtn);
                    validHash = true;
                }
            }
        }
        
        if(!validHash) {
            let allBtn = document.querySelector(`.filter-chip[data-filter="all"]`);
            if(allBtn) applyFilter('all', allBtn);
        }
    }
});
