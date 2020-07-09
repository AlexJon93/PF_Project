<template>
    <tr>
        <td>{{ order.customer_company }}</td>
        <td>{{ order.customer_name }}</td>
    </tr>
</template>

<script>
export default {
    name: "OrderListItem",
    props: {
        order: Object
    }
}
</script>