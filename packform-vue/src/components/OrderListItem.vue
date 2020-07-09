<template>
    <div>
        {{ customer.customer_name }}
    </div>
</template>

<script>
export default {
    name: "OrderListItem",
    props: {
        customer: Object
    }
}
</script>