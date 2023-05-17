<template>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
        <div class="container-fluid">
            <a class="navbar-brand" href="/">Home</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent"
                aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="/prediction">Predict</a>
                    </li>

                </ul>

            </div>
        </div>
    </nav>
    <h1 class="text-center">Prediction Page</h1>
    <div class="container d-flex justify-content-center mt-5">
        <div class="card p-3" style="width: 400px;">

            <form class="d-flex flex-column" @submit.prevent="submitUrl">
                <div class="form-group m-3">
                    <label for="articleUrl">Enter Article URL:</label>
                    <input type="text" class="form-control" v-model="articleUrl" required>
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
    </div>

    <div class="container d-flex justify-content-center mt-3 mb-5">
        <div class="card p-3">


            <h4>Classification History:</h4>
            <table class="table">
                <thead>
                    <tr>
                        <th>Article URL</th>
                        <th>Predicted Category</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="history in classificationHistory" :key="history.id">
                        <td>{{ history.url }}</td>
                        <td>{{ history.Category }}</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
  
<script>
import swal from 'sweetalert';

export default {
    name: "Home",
    data() {
        return {
            articleUrl: '',
            predictedCategory: '',
            classificationHistory: [],

        };
    },
    methods: {
        submitUrl() {
            // const requestBody = { url: this.articleUrl };
            console.log('clicked')
            const options = {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: `{"url":"${this.articleUrl}"}`
            };

            fetch('http://localhost:5000/predict', options)
                .then(response => response.json())
                .then(response => {
                    console.log(response)
                    this.predictedCategory = response['predicted_category']

                    swal(`This Article is of ${response['predicted_category']} type`);

                    this.get_history()
                })
                .catch(err => {
                    swal({
                        title: "Something Went wrong",
                        text: "Check the url or try again",
                        icon: "warning",
                        button: "Okay",
                        dangerMode: true,
                    })
                });
        },

        get_history() {
            const options = { method: 'GET' };

            fetch('http://localhost:5000/history', options)
                .then(response => response.json())
                .then(response => this.classificationHistory = response)
                .catch(err => console.error(err));
        }

    },
    created() {
        //   localStorage.clear();
        this.get_history()
    },
};
</script>
  
<style scoped></style>
  