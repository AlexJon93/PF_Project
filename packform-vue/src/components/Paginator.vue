<template>
    <div>
        <button v-if="currentPage > 0" v-on:click="setPage($event)" id="decrement">&lt;</button>
        <input v-on:change="setPage($event)" type="number" v-bind:placeholder="this.currentPage" id="change">
        <button v-if="currentPage < totalPages-1" v-on:click="setPage($event)" id="increment">&gt;</button>
    </div>
</template>
<script>
export default {
    name: 'Paginator',
    props: {
        currentPage: Number,
        totalPages: Number
    },
    methods: {
        setPage: function(event){
            switch(event.target.id){
                case 'increment':
                    this.$emit('change-page', this.currentPage+1)
                    break
                case 'decrement':
                    this.$emit('change-page', this.currentPage-1)
                    break
                default:
                    this.$emit('change-page', Number(event.target.value))
            }
            
        }
    }
}
</script>