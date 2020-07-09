<template>
    <div class="spinner"></div>
</template>
<style scoped>
    .spinner{
        width: 2em;
        height: 2em;
        border: 0.5em solid transparent;
        border-color: #eee;
        border-top-color: rgb(24, 50, 165);
        border-radius: 50%;
        animation: spin 0.5s linear infinite;
    }

    @keyframes spin {
        100% {
            transform: rotate(360deg);
        }
    }
</style>