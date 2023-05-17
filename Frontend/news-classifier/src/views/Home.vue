<template>
    <!-- <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid"> -->
    <!-- <a class="navbar-brand" href="/">Home</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button> -->
    <!-- <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" aria-current="page" href="/prediction">Predict</a>
                    </li>

                </ul>

            </div>
        </div>
    </nav> -->
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
            <div class="container">
                <a class="navbar-brand" href="#">News Prediction</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                    aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav ml-auto">
                        <li class="nav-item active">
                            <a class="nav-link" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Predict!</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

    <section id="hero-section" class="py-5 text-center">
        <div class="container py-5">
            <h1>News Category Prediction</h1>
            <p class="lead">Get accurate predictions for all your news articles</p>
            <br>
            <a class="btn btn-dark" href="#">Get Started &raquo;</a>
        </div>
    </section>

    <section id="guide-section" class="py-5 bg-light">
        <div class="container">
            <h2 class="text-center">How to Use</h2>
            <div class="row p-5">
                <div class="col-4">
                    <h1 class="blog-post-title">1</h1>
                    <!-- <h2>Step 1</h2> -->
                    <p>Enter the URL of the news article from any website for which you want a prediction.</p>
                </div>
                <div class="col-4">
                    <h1 class="blog-post-title">2</h1>
                    <!-- <h2>Step 2</h2> -->
                    <p>Click on the "Predict" button to generate the category prediction for the article in the
                        categories of sports, business, politics, tech, and entertainment.</p>
                </div>
                <div class="col-4">
                    <h1 class="blog-post-title">3</h1>
                    <!-- <h2>Step 3</h2> -->
                    <p>Scroll down to view your previous predictions and their corresponding article URLs.</p>
                </div>
            </div>
        </div>
    </section>

    <footer class="py-3 bg-dark text-white">
        <div class="container text-center">
            <p>Footer stuff.</p>
        </div>
    </footer>
</template>
  
<script>
export default {
    name: "Home",
    data() {
        return {
            a: ''
        };
    },
    methods: {


    },
    created() {
        //   localStorage.clear();

    },
};
</script>
  
<style scoped></style>
  