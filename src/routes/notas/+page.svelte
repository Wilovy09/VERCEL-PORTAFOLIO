<script>
    import Layout from '../../layouts/Layout.svelte';
    import LinkNotas from '../../components/notas/LinkNotas.svelte';
</script>

<Layout>
    <h2 class="text-[#26bb80] text-5xl font-bold py-12 uppercase text-center">Mis Notas</h2>
    <section class="min-h-screen">
        <LinkNotas title="Prisma" link="https://github.com/Wilovy09/Prisma-Curso-ORM/blob/main/README.md"/>
        <LinkNotas title="Express & Prisma" link="https://github.com/Wilovy09/NodeJS_Prisma_API/blob/main/README.md"/>
    </section>
</Layout>