const listApp = Vue.createApp({
    data() {
        return {
            communities: [],
            message: '',
            nextPage: null,
            prevPage: null,
            currentPage: 1
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
                this.nextPage = data.next;
                this.prevPage = data.previous;
            })
            .catch(error => {
                console.error("Error:", error);
                this.message = 'Error loading the communities, reload the page';
            });
        },
        nextPageMethod() {
            if (this.nextPage) {
                this.currentPage++;
                this.communitiesList(this.nextPage);
            }
        },
        prevPageMethod() {
            if (this.prevPage) {
                this.currentPage--;
                this.communitiesList(this.prevPage);
            }
        },
        goToCommunity(communityId) {
            window.location.href = `/community/${communityId}/`;
        }
    },
    mounted() {
        console.log("Vue montado correctamente en #list");
        this.communitiesList();
    }
});

// Montar la app en el contenedor de la lista
listApp.mount('#list');
