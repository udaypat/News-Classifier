<template>
    <head>
        <meta http-equiv="Content-Security-Policy" content="upgrade-insecure-requests">
    </head>
    <div class="container">
        <h1>Prediction Page</h1>
        <form @submit.prevent="submitUrl">
            <div class="form-group">
                <label for="articleUrl">Enter Article URL:</label>
                <input type="text" class="form-control" v-model="articleUrl" required>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>

        <h3 v-if="predictedCategory">Predicted Category: {{ predictedCategory }}</h3>

        <!-- <h4>Classification History:</h4>
        <table class="table">
            <thead>
                <tr>
                    <th>Article URL</th>
                    <th>Predicted Category</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="history in classificationHistory" :key="history.id">
                    <td>{{ history.articleUrl }}</td>
                    <td>{{ history.predictedCategory }}</td>
                </tr>
            </tbody>
        </table> -->
    </div>
</template>
  
<script>
export default {
    name: "Home",
    data() {
        return {
            articleUrl: '',
            predictedCategory: '',
            classificationHistory: []
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

            fetch('64.227.158.87/predict', options)
                .then(response => response.json())
                .then(response => {
                    this.predictedCategory = response['predicted_category']
                })
                .catch(err => console.error(err));
        }

    },
    created() {
        //   localStorage.clear();

    },
};
</script>
  
<style scoped></style>
  