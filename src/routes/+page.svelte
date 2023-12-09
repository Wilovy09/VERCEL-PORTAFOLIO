<script>
    import Layout from '../layouts/Layout.svelte';
    import Soy from '../components/Soy.svelte';
    import Repositorios from '../components/Repositorios.svelte';
    import Tecnologias from '../components/Tecnologias.svelte';
</script>

<Layout>
    <Soy />
    <Tecnologias>
        <Repositorios slot="repositorios" />
    </Tecnologias>
</Layout>