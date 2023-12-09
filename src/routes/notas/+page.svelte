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

<style>
    h2{
        --bg-size: 400%;
        --color-one: #26bb80;
        --color-two: #12543a;
        background: linear-gradient(90deg,var(--color-one),var(--color-two),var(--color-one)) 0 0 / var(--bg-size) 100%;
        color: transparent;
        background-clip: text;
        -webkit-background-clip: text;
        animation: move-bg 8s infinite linear;
    }

    @keyframes move-bg {
        to {
            background-position: var(--bg-size) 0;
        }
    }

    @media (prefers-reduced-motion: no-preference) {
        h2 {
            animation: move-bg 8s linear infinite;
        }
        @keyframes move-bg {
            to {
                background-position: var(--bg-size) 0;
            }
        }
    }
</style>