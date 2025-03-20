const app = Vue.createApp({
    data() {
        return {
            searchQuery: "",
            filteredResults: [],
            isLoading: false,
            debounceTimer: null,
            showResults: false
        };
    },
    methods: {
        fetchDataBasedOnRoute(){
            const path = window.location.pathname;
            if (path === 'http://127.0.0.1:8000/community/discover/'){
                this.filterCommunityResults();
            } else if (path === ''){

            }
        },
        async filterCommunityResults() {
            // Si la búsqueda está vacía, no mostramos resultados
            if (!this.searchQuery.trim()) {
                this.filteredResults = [];
                this.showResults = false;
                return;
            }
            
            this.isLoading = true;
            this.showResults = true;
            
            try {
                const response = await fetch(
                    `http://127.0.0.1:8000/community/api/v1/communitiy/?search=${this.searchQuery}`);
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                console.log("Datos recibidos:", data);
                this.filteredResults = data.results || [];
            } catch (error) {
                console.error("Error al buscar:", error);
                this.filteredResults = [];
            } finally {
                this.isLoading = false;
            }
        },
        // Method to navigate at the community page
        goToCommunity(communityId) {
            window.location.href = `/community/${communityId}/`;
        }
    },
    watch: {
        // Este watcher hará que la búsqueda se active con cada cambio en searchQuery
        searchQuery: function(newVal) {
            // Implementamos un debounce básico para evitar demasiadas solicitudes
            if (this.debounceTimer) clearTimeout(this.debounceTimer);
            this.debounceTimer = setTimeout(() => {
                this.filterCommunityResults();
            }, 300); // Espera 300ms después de que el usuario deje de escribir
        }
    },
});
app.mount("#search-bar-app");