const filterList = {
    template:`
        <div class="filters">
            <label for="options">Filters</label>
            <select id="options" v-model="selection">
            <option value="sports">Sports</option>
            </select>
        </div>
        `,
        data(){
            
        }
};

Vue.createApp(filterList).mount("filters-list");