const popularApp = Vue.createApp({
    data() {
        return {
            mostPopular: [],
            communities: []
        };
    },
    methods: {
        communitiesList(pageUrl = null) {
            let url = pageUrl || 'http://127.0.0.1:8000/community/api/v1/communitiy/';
            
            console.log("Buscando comunidades en:", url);
            fetch(url)
            .then(response => response.json())
            .then(data => {
                console.log("Datos recibidos:", data);
                this.communities = data.results;
                this.mostPopular = this.getMostPopular();
            })
            .catch(error => {
                console.error("Error:", error);
                this.message = 'Error loading the communities, reload the page';
            });
        },
        goToCommunity(communityId) {
            window.location.href = `/community/${communityId}/`;
        },
        getMostPopular(){
            return this.communities
            .sort((a, b) => b.users_count - a.users_count)
            .slice(0, 4);
        }
    },
    mounted() {
        console.log("Vue montado correctamente en #list");
        this.communitiesList();
    }
});

// Montar la app en el contenedor de la lista
popularApp.mount('#popular-container');
