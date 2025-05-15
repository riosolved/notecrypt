<template>
    <!-- <Notebook /> -->
    <Enter
        @registered="enter_handle_registered"
        @entered="enter_handle_entered"
    />
</template>

<script setup>
    // import Notebook from './components/Notebook.vue';
    import Enter from './components/Enter.vue';

    const enter_handle_registered = (data) => {
        // console.log("DEBUG::enter::handle_registered::this", this);
        // console.log("DEBUG::enter::handle_registered::data", data);
        // console.log("DEBUG::enter::handle_registered::document.cookies", document.cookies);
    };

    const enter_handle_entered = (data) => {
        // console.log("DEBUG::enter::handle_entered::this", this);
        // console.log("DEBUG::enter::handle_entered::data", data);
        // console.log("DEBUG::enter::handle_entered::document.cookies", document.cookies);
    };
</script>

<!--
<script>
// import Notebook from './components/Notebook.vue';
import Enter from './components/Enter.vue';

const enter_handle_registered = (data) => {
    console.log("DEBUG::enter::handle_registered::this", this);
    console.log("DEBUG::enter::handle_registered::data", data);
    console.log("DEBUG::enter::handle_registered::document.cookies", document.cookies);
};

const enter_handle_entered = (data) => {
    console.log("DEBUG::enter::handle_entered::this", this);
    console.log("DEBUG::enter::handle_entered::data", data);
    console.log("DEBUG::enter::handle_entered::document.cookies", document.cookies);
};

export default {
    name: 'Main',
    components: {
        // Notebook
        Enter
    },
}
</script>
-->
